from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
from uuid import uuid4
from datetime import datetime
from app.db import get_db
from sqlalchemy.future import select
from app.models import Campaign, Recipient
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

ALLOWED = {'.csv', '.xlsx', '.xls'}

def _validate_email(e: str) -> bool:
    return '@' in e and '.' in e

@router.post('/upload')
async def upload(file: UploadFile = File(...)):
    name = file.filename
    ext = name[name.rfind('.'):].lower()
    if ext not in ALLOWED:
        raise HTTPException(400, 'Invalid file type')

    # read bytes into pandas (works for small files)
    contents = await file.read()
    # pandas to parse
    try:
        if ext == '.csv':
            df = pd.read_csv(pd.io.common.BytesIO(contents))
        else:
            df = pd.read_excel(pd.io.common.BytesIO(contents))
    except Exception as e:
        raise HTTPException(400, f"Could not parse file: {e}")

    required = {'name', 'email'}
    if not required.issubset({c.lower() for c in df.columns}):
        raise HTTPException(400, 'Missing required columns: name, email')

    # preview first 50 rows
    preview = []
    for i, row in df.head(50).iterrows():
        email = str(row.get('email') or row.get('Email') or '')
        name_r = str(row.get('name') or row.get('Name') or '')
        preview.append({'row': i+1, 'name': name_r, 'email': email})

    # Create campaign file entry (for this scaffold we return a fake campaign_id)
    campaign_id = str(uuid4())
    return JSONResponse({'campaign_id': campaign_id, 'preview': preview})

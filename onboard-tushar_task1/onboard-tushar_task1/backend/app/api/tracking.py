from fastapi import APIRouter, Response, HTTPException
from fastapi.responses import RedirectResponse
from datetime import datetime
import binascii
router = APIRouter()

# 1x1 PNG binary (minimal valid PNG)
ONE_PIXEL_PNG = (b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01'
           b'\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89'
           b'\x00\x00\x00\nIDATx\x9cc`\x00\x00\x00\x02\x00\x01'
           b'\xe2!\xbc3\x00\x00\x00\x00IEND\xaeB`\x82')

@router.get('/r/{campaign_id}/{recipient_id}')
async def click_redirect(campaign_id: str, recipient_id: str):
    # Log click (scaffold: print)
    print(f"[CLICK] campaign={campaign_id} recipient={recipient_id} at {datetime.utcnow().isoformat()}")
    # In production: update DB event and set clicked_at
    # redirect to AveoEarth
    return RedirectResponse(url="https://aveoearth.com", status_code=302)

@router.get('/pixel/{campaign_id}/{recipient_id}.png')
async def pixel(campaign_id: str, recipient_id: str):
    # Log open (scaffold: print)
    print(f"[OPEN] campaign={campaign_id} recipient={recipient_id} at {datetime.utcnow().isoformat()}")
    headers = {
        "Cache-Control": "no-store, no-cache, must-revalidate, max-age=0",
        "Content-Type": "image/png"
    }
    return Response(content=ONE_PIXEL_PNG, media_type="image/png", headers=headers)

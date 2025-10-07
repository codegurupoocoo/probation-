from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
router = APIRouter()

# For scaffold: simple in-memory map to emulate campaigns started
_started = {}

@router.post("/{campaign_id}/start")
async def start_campaign(campaign_id: str):
    # In a full impl this would enqueue Celery jobs and create DB rows
    _started[campaign_id] = {'started': True}
    return JSONResponse({'started': True})

@router.get("/{campaign_id}/status")
async def campaign_status(campaign_id: str):
    s = _started.get(campaign_id, {'started': False})
    # minimal metrics for scaffold
    metrics = {
        'total_sent': 0,
        'delivered': 0,
        'opened': 0,
        'clicked': 0,
        'ctr': 0.0,
        'reminders_sent': 0
    }
    return {'campaign': {'id': campaign_id, 'status': 'running' if s['started'] else 'draft'}, 'metrics': metrics}

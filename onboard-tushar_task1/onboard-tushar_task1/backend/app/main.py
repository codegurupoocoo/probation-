from fastapi import FastAPI
from app.api import upload, tracking, campaigns
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Onboard Task1 - backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router, prefix="/api")
app.include_router(campaigns.router, prefix="/api")
app.include_router(tracking.router, prefix="")

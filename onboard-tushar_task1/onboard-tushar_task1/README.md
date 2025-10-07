# onboard-tushar — Task 1: Email automation agent + tracking + dashboard

This repository scaffold contains a minimal, production-aligned implementation for **Task 1**:
- FastAPI backend with tracking endpoints (/pixel and /r redirect)
- Upload endpoint accepting CSV/XLSX and returning preview
- Celery task stubs for sending emails & reminder scheduling
- Simple Next.js frontend scaffold (upload + dashboard pages)
- Docker Compose for local development
- sample_recipients.xlsx

**Important:** This is a scaffold to get you started and to meet the assignment deliverables. You will need to:
- Provide SendGrid (or other) API keys in `.env`
- Install Python and Node dependencies (see sections below)
- Optionally run migrations (if you add Alembic)

## Quick start (dev)

1. Copy environment example:
```
cp .env.example .env
```

2. Build & start with Docker Compose (recommended):
```
docker-compose up --build
```

3. Backend docs (when backend is running): `http://localhost:8000/docs`
   Frontend (Next.js dev server): `http://localhost:3000` (if you run `npm install && npm run dev` in the frontend folder)

## Contents
- `backend/` — FastAPI app (tracking endpoints, upload, DB models)
- `frontend/` — Next.js minimal scaffold (pages: upload, dashboard)
- `docker-compose.yml` — services: postgres, redis, backend, celery (stub), frontend
- `sample_recipients.xlsx` — example upload file
- `.env.example` — environment variables example

## Notes
- The Next.js frontend is a scaffold (no Node modules included). Run `npm install` in `frontend/` to install dependencies.
- The backend uses SQLAlchemy + async session patterns and includes endpoints for pixel and click tracking; sending emails is stubbed in `backend/app/email.py`.
- Celery worker is configured in `docker-compose.yml` but you must ensure Celery is installed and configured (Python `requirements.txt` provided).

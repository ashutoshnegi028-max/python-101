# Workforce Tracker (Enterprise Ops Dashboard)

## Stack
- Frontend: React + Tailwind + Recharts
- Backend: FastAPI
- Database: PostgreSQL

## Folder Structure
- `backend/app`: API, schemas, services
- `backend/sql`: schema and seed scripts
- `frontend/src`: dashboard UI

## Setup
### Backend
1. `cd backend`
2. `python -m venv .venv && source .venv/bin/activate`
3. `pip install -r requirements.txt`
4. `cp .env.example .env`
5. `uvicorn app.main:app --reload`

### Frontend
1. `cd frontend`
2. `npm install`
3. `npm run dev`

## Core API Endpoints
- `GET /health`
- `GET /api/v1/dashboard`
- `GET /api/v1/employees`

## API Test Example
```bash
curl http://localhost:8000/api/v1/dashboard
```

## Business Rules
- Utilization % = `(productive_hours / login_hours) * 100`
- Status:
  - `> 90`: Overutilized
  - `70 - 90`: Optimally Utilized
  - `< 70`: Available for More Work

## Planned Enterprise Enhancements
- Role-based JWT auth (Admin/Manager/Viewer)
- CSV/Excel ingestion endpoint
- 1-minute auto-refresh websocket
- PDF/Excel export
- Forecasting and staffing shortage prediction
- Workload redistribution recommendation engine

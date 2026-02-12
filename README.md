# Todo App (Angular 20 + FastAPI + Postgres)

This repo contains a minimal full-stack todo application with an Angular 20 frontend, a FastAPI backend, and Postgres for storage.

## Quick start (Docker)

```bash
docker compose up --build
```

- Frontend: http://localhost:4200
- API: http://localhost:8000

## Local development

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm start
```

## Environment

The API reads `DATABASE_URL`.

Example:

```bash
export DATABASE_URL=postgresql+psycopg://todo:todo@localhost:5432/todo
```

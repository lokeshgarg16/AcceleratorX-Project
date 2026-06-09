# AcceleratorX Program Fit Engine

An AI-powered program recommendation and lead qualification MVP for AcceleratorX.

## What it does

- Captures intake responses from prospective learners and partners
- Recommends the best-fit AcceleratorX program with an explainable reason
- Scores leads out of 100 and classifies them as Hot, Warm, Cold, or Not Suitable
- Generates counsellor notes with safe, practical language
- Stores leads in SQLite for an admin dashboard and follow-up tracking

## Tech Stack

- Frontend: React, Vite, Tailwind CSS
- Backend: FastAPI, SQLAlchemy, SQLite
- AI: Google Gemini API

## Project Structure

- `backend/app/main.py`: FastAPI app entry point
- `backend/app/services/scoring.py`: lead scoring logic
- `backend/app/services/recommendation.py`: program recommendation logic
- `backend/app/services/gemini.py`: Gemini prompt and note generation
- `frontend/src/pages`: landing, assessment, result, admin, and lead detail pages

## Setup

### 1. Backend

```bash
cd backend
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API runs at `http://localhost:8000`.

### 2. Frontend

```bash
cd frontend
npm install
npm run dev
```

The web app runs at `http://localhost:5173`.

## Environment Variables

Copy `.env.example` to `.env` and set:

- `GEMINI_API_KEY`: Google Gemini API key
- `GEMINI_MODEL`: Gemini model name, defaults to `gemini-1.5-flash`
- `DATABASE_URL`: SQLite URL for the backend database
- `VITE_API_BASE_URL`: backend API base URL for the frontend

## Sample Dummy Data

The backend seeds a few example leads on startup when the database is empty, so the admin dashboard has data immediately.

## Safety Notes

- The AI copy avoids guarantees about jobs, salaries, internships, or placements
- Counsellor notes focus on career support, project support, portfolio guidance, and placement assistance
- Recommendations are explainable and practical

## API Endpoints

- `POST /api/assessment/submit`
- `GET /api/leads`
- `GET /api/leads/{id}`
- `PATCH /api/leads/{id}/status`

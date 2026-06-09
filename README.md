# AcceleratorX Program Fit & Lead Qualification Engine

[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-Vite-61DAFB?logo=react&logoColor=000)](https://react.dev/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.x-38B2AC?logo=tailwindcss&logoColor=fff)](https://tailwindcss.com/)
[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=fff)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=fff)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](#license)

> 🚀 An AI-powered lead qualification and program recommendation system built for AcceleratorX.

This project helps students, professionals, colleges, and corporates discover the most suitable AI learning program through a smart assessment workflow. It automatically recommends programs, calculates lead scores, generates counsellor notes, and streamlines admissions follow-up.

## Project Banner / Introduction

**AcceleratorX Program Fit & Lead Qualification Engine** is a full-stack MVP designed to support admissions, counselling, and lead management for AI education programs.

It provides:

- Smart assessment forms for multiple user types
- Explainable AI-driven program recommendations
- Lead scoring from 0 to 100
- Hot, Warm, Cold, and Not Suitable categorization
- AI-generated counsellor notes with safe language
- Admin tools for lead review and follow-up tracking

## Features

- 🧠 Smart AI-powered assessment form
- 🎯 Program recommendation engine
- 📊 Lead scoring system (0–100)
- 🔥 Lead categorization: Hot, Warm, Cold, Not Suitable
- 🤖 AI-generated counsellor notes
- ✅ Readiness assessment
- 🧩 Skill gap analysis
- 🗂️ Admin dashboard
- 👥 Lead management system
- 📌 Follow-up status tracking
- REST API architecture
- 📱 Responsive UI

## Architecture Diagram

```text
┌──────────────────────────────┐
│       React + Vite UI        │
│  Landing / Assessment / Admin│
└──────────────┬───────────────┘
               │ HTTP REST
               ▼
┌──────────────────────────────┐
│        FastAPI Backend       │
│  Routes / Services / Gemini  │
│  Scoring / Recommendation    │
└──────────────┬───────────────┘
               │ SQLAlchemy ORM
               ▼
┌──────────────────────────────┐
│           SQLite             │
│             Leads            │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│     Google Gemini API        │
│   Counsellor Note Generation │
└──────────────────────────────┘
```

## Tech Stack

### Frontend

- React.js
- Vite
- Tailwind CSS

### Backend

- FastAPI
- Python

### Database

- SQLite

### AI

- Google Gemini API

## Folder Structure

```text
AcceleratorX/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── routes/
│   │   └── services/
│   ├── requirements.txt
│   └── runtime.txt
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── index.html
│   ├── package.json
│   └── tailwind.config.js
├── runtime.txt
└── README.md
```

## User Types

- College Students
- Working Professionals
- Beginners Exploring AI
- Faculty Members
- College Administrators
- Corporate HR / L&D Teams

## Project Workflow

1. User completes the assessment.
2. System analyzes profile and goals.
3. AI recommends the most suitable program.
4. Lead score is calculated.
5. Counsellor notes are generated.
6. Lead is stored in the database.
7. Admin team reviews and follows up.

## Lead Scoring Logic

The system calculates a score out of 100 using these components:

- Goal Clarity: 20
- Background Relevance: 15
- Budget Readiness: 15
- Timeline Urgency: 15
- Program Fit: 20
- Engagement Quality: 10
- Contact Completeness: 5

### Lead Categories

- Hot: 80–100
- Warm: 60–79
- Cold: 40–59
- Not Suitable: below 40

## Sample Assessment Flow

```text
User opens assessment
        ↓
Answers 10 smart questions
        ↓
Backend scores profile and evaluates fit
        ↓
Gemini generates counsellor notes
        ↓
Lead is stored in SQLite
        ↓
Admin reviews the lead and updates follow-up status
```

## Installation Guide

### Prerequisites

- Python 3.12+
- Node.js 18+
- npm
- Google Gemini API key

### 1) Clone the repository

```bash
git clone https://github.com/lokeshgarg16/AcceleratorX-Project.git
cd AcceleratorX-Project
```

## Backend Setup

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The backend runs at:

- API: `http://localhost:8000`
- Health check: `http://localhost:8000/`

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

The frontend runs at:

- App: `http://localhost:5173`

## Environment Variables

Create a `.env` file and add the following variables:

```env
GEMINI_API_KEY=
GEMINI_MODEL=gemini-1.5-flash
VITE_API_BASE_URL=
```

### Notes

- `GEMINI_API_KEY` is required for live Gemini responses.
- `GEMINI_MODEL` defaults to `gemini-1.5-flash`.
- `VITE_API_BASE_URL` should point to the deployed backend in production.

## API Endpoints

### Assessment

- `POST /api/assessment/submit`

### Leads

- `GET /api/leads`
- `GET /api/leads/{id}`
- `PATCH /api/leads/{id}/status`

### Example Request

```bash
curl -X POST http://localhost:8000/api/assessment/submit \
  -H "Content-Type: application/json" \
  -d '{
    "user_type": "College Student",
    "current_role": "Final year student",
    "education_background": "Computer Science background",
    "ai_skill_level": "Beginner",
    "goal": "I want to build an AI portfolio and start a career in AI.",
    "timeline": "Within 1-3 months",
    "budget_readiness": "Can pay with planning",
    "weekly_availability": "6-8 hours",
    "preferred_learning_mode": "Live guided sessions",
    "contact_name": "Aarav Sharma",
    "contact_email": "aarav@example.com",
    "contact_phone": "9876543210"
  }'
```

## Screenshots

> 📷 Add project screenshots here after deployment.

Suggested screenshots:

- Landing page
- Assessment form
- Result page
- Admin dashboard
- Lead detail page

## Future Enhancements

- Add authentication for admin access
- Add filters and search for leads
- Add export to CSV / Excel
- Add email notifications for new qualified leads
- Add analytics charts for admissions performance
- Add richer AI notes with configurable tone
- Add multi-tenancy for different programs or branches

## Deployment

### Frontend on Vercel

1. Push the project to GitHub.
2. Import the repository into Vercel.
3. Set the root directory to `frontend`.
4. Add the environment variable:
   - `VITE_API_BASE_URL=https://your-render-backend-url.onrender.com`
5. Deploy the frontend.

### Backend on Render

1. Create a new Render Web Service.
2. Set the root directory to `backend`.
3. Use the build command:

```bash
pip install -r requirements.txt
```

4. Use the start command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

5. Add the environment variables:
   - `GEMINI_API_KEY`
   - `GEMINI_MODEL=gemini-1.5-flash`
6. Ensure Python is pinned with `backend/runtime.txt`.

## Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes.
4. Test locally.
5. Submit a pull request.

## License

This project is licensed under the MIT License. You may adapt and use it for learning, portfolio, and showcase purposes.

## Author

**AcceleratorX Program Fit & Lead Qualification Engine**

Built as a full-stack AI admissions and lead qualification MVP for showcasing modern product engineering, scoring logic, and practical AI integration.

from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine, SessionLocal
from .routes.assessment import router as assessment_router
from .routes.leads import router as leads_router
from .seed_data import seed_demo_leads

app = FastAPI(title="AcceleratorX Program Fit Engine", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(assessment_router)
app.include_router(leads_router)


@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        seed_demo_leads(db)
    finally:
        db.close()


@app.get("/")
def health_check():
    return {"status": "ok", "service": "AcceleratorX Program Fit Engine"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

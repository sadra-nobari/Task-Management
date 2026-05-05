from fastapi import FastAPI
from .routers import tasks
from .database import engine, Base

Base.metadata.create_all(bind=engine)  # ایجاد جدول‌ها در دیتابیس

app = FastAPI(title="Task Manager API", docs_url="/docs", redoc_url="/redoc")

app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "Welcome to Task Manager API"}
from fastapi import FastAPI
from app.database import engine, Base
from app.routers import expense
from app.models import expense as expense_model  # để tạo table

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(expense.router)

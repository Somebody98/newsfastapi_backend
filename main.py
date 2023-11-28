from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse
from starlette.status import HTTP_200_OK
from typing import Union
from datetime import datetime, timedelta
from typing import Annotated
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from models import *
from database35 import *
import uvicorn



# запуск виртуальной среды venv\scripts\activate
# запуск сервера uvicorn main:app --reload
app = FastAPI()
app.mount("/main", StaticFiles(directory="public"))

# Cors Блокировка отключена
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# определяем зависимость
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    html_content = "<h2>Hello World!</h2>"
    return HTMLResponse(content=html_content)

@app.get("/news")
async def root():
    return db.query(News).order_by(News.id).all()

#@app.post("/reg/")
# async def reg(user: FakeUser, db: Session = Depends(get_db)):
#     user = User(email=user.email, hashed_password=user.password)
#     db.add(user)
#     db.commit()
#     return user


from fastapi import FastAPI
from Database.connection import db

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Connected to MongoDB Atlas"}




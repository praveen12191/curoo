from fastapi import FastAPI, APIRouter
from database.connection import db
from middleware.middleware import add_middleware
from routes.doctors import router as doctor_router


app = FastAPI()
base_router = APIRouter(prefix = "/curoo")
add_middleware(app)


base_router.include_router(doctor_router)


from fastapi import APIRouter
from model.model import Doctors

router = APIRouter()

@router.post("/create_doctor")
async def create_doctor(value : Doctors):
    pass


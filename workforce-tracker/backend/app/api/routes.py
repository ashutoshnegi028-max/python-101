from fastapi import APIRouter
from app.services.metrics import get_dashboard_data

router = APIRouter()


@router.get('/dashboard')
def dashboard():
    return get_dashboard_data()


@router.get('/employees')
def employees():
    return get_dashboard_data().employees

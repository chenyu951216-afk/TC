from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.services.ranking_service import generate_stocks

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/")
def dashboard(request: Request):
    stocks = generate_stocks()
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "stocks": stocks},
    )

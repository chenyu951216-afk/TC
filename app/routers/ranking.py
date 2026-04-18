from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.services.ranking_service import generate_stocks

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/ranking")
def ranking(request: Request):
    stocks = generate_stocks()
    return templates.TemplateResponse(
        "ranking.html",
        {"request": request, "stocks": stocks},
    )

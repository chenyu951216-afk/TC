from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

alerts_data = [
    {"stock": "2382", "level": "橘燈", "reason": "跌破短線結構"},
    {"stock": "1519", "level": "黃燈", "reason": "量能下降，需觀察"},
]


@router.get("/alerts")
def alerts(request: Request):
    return templates.TemplateResponse(
        "alerts.html",
        {"request": request, "alerts": alerts_data},
    )

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

watchlist_data = [
    {"stock_id": "2382", "name": "廣達", "status": "強勢追蹤"},
    {"stock_id": "1519", "name": "華城", "status": "黃燈觀察"},
]


@router.get("/watchlist")
def watchlist(request: Request):
    return templates.TemplateResponse(
        "watchlist.html",
        {"request": request, "stocks": watchlist_data},
    )

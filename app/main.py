from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers import dashboard, ranking, watchlist, alerts

app = FastAPI(title="TW Stock AI Bot")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(dashboard.router)
app.include_router(ranking.router)
app.include_router(watchlist.router)
app.include_router(alerts.router)

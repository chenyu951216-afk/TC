import random
from app.services.risk_service import calculate_risk


def generate_stocks() -> list[dict]:
    stocks = []
    sample_ids = ["2330", "2382", "2303", "2454", "3017", "3231", "3661", "1519", "3037", "2383"]
    sample_names = ["台積電", "廣達", "聯電", "聯發科", "奇鋐", "緯創", "世芯-KY", "華城", "欣興", "台光電"]

    for stock_id, name in zip(sample_ids, sample_names):
        price = random.randint(50, 1200)
        score = random.randint(60, 95)
        risk = calculate_risk(price)
        stocks.append({
            "stock_id": stock_id,
            "name": name,
            "score": score,
            "price": price,
            **risk,
        })

    stocks.sort(key=lambda x: x["score"], reverse=True)
    return stocks[:5]

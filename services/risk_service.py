def calculate_risk(price: float) -> dict:
    stop_loss = round(price * 0.95, 2)
    r = round(price - stop_loss, 2)
    return {
        "stop_loss": stop_loss,
        "tp1": round(price + r * 1.5, 2),
        "tp2": round(price + r * 2.5, 2),
        "tp3": round(price + r * 4.0, 2),
        "holding_days": 3 + int(abs(r) % 7),
    }

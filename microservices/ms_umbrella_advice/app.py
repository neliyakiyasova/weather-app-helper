from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Umbrella Advice Service")


class RainRequest(BaseModel):
    rain_chance: float


@app.post("/umbrella")
def umbrella(data: RainRequest):
    p = data.rain_chance
    if p < 30:
        advice = "зонт не обязателен"
    elif p < 60:
        advice = "подумай о зонте"
    else:
        advice = "зонт очень желателен"
    return {"advice": advice, "rain_chance": p}

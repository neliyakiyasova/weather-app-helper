from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Feels Like Service")


class TempRequest(BaseModel):
    temp: float


@app.post("/feels_like")
def feels_like(data: TempRequest):
    t = data.temp
    if t < 0:
        label = "очень холодно"
    elif t < 10:
        label = "прохладно"
    elif t < 20:
        label = "комфортно"
    else:
        label = "тепло"
    return {"label": label, "temp": t}

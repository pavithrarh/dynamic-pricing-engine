from fastapi import FastAPI
from pydantic import BaseModel
from utils import predict, optimize_price

app = FastAPI()

# ✅ ADD HERE
@app.get("/")
def home():
    return {"message": "Dynamic Pricing API is running"}

class InputData(BaseModel):
    product_type: int
    competitor_price: float
    demand: int
    inventory: int
    season: int
    cost: float

@app.post("/predict")
def get_price(data: InputData):
    features = [
        data.product_type,
        data.competitor_price,
        data.demand,
        data.inventory,
        data.season
    ]

    price = predict(features)
    opt_price, opt_profit = optimize_price(price, data.demand, data.cost)

    return {
        "predicted_price": price,
        "optimized_price": opt_price,
        "max_profit": opt_profit
    }
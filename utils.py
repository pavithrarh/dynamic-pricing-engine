import joblib

model = joblib.load("model/model.pkl")

# ✅ FIXED NAME
def predict(data):
    return model.predict([data])[0]

def optimize_price(base_price, demand, cost):
    best_price = base_price
    max_profit = 0

    for p in range(int(base_price - 20), int(base_price + 30)):
        profit = (p - cost) * demand
        if profit > max_profit:
            max_profit = profit
            best_price = p

    return best_price, max_profit
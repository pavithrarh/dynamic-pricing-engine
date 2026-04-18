import joblib

model = joblib.load("model/model.pkl")

def predict_price(competitor_price, demand, day, month):
    price_diff = 0
    data = [[competitor_price, demand, day, month, price_diff]]
    prediction = model.predict(data)
    return round(prediction[0], 2)
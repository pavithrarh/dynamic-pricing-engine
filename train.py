import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
from data_processor import preprocess   # ✅ changed here

df = pd.read_csv("data/data.csv")
df = preprocess(df)

X = df[['product_type','competitor_price','demand','inventory','season']]
y = df['price']

model = RandomForestRegressor(n_estimators=100)
model.fit(X, y)

joblib.dump(model, "model/model.pkl")

print("Model trained successfully ✅")
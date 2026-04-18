import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
import joblib

# Load data
df = pd.read_csv("data/data.csv")

# Convert date
df['date'] = pd.to_datetime(df['date'])

# Create features
df['day'] = df['date'].dt.day
df['month'] = df['date'].dt.month
df['price_diff'] = df['price'] - df['competitor_price']

# Input and output
X = df[['competitor_price', 'demand', 'day', 'month', 'price_diff']]
y = df['price']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = XGBRegressor()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model/model.pkl")

print("Model trained successfully ✅")
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import requests

st.title("💰 Dynamic Pricing Engine")

product_type = st.selectbox("Product Type", [0,1,2])
season = st.selectbox("Season", [0,1,2])

competitor_price = st.number_input("Competitor Price", value=100)
demand = st.number_input("Demand", value=100)
inventory = st.number_input("Inventory", value=50)
cost = st.number_input("Cost", value=50)

if st.button("Predict"):
    data = {
        "product_type": product_type,
        "competitor_price": competitor_price,
        "demand": demand,
        "inventory": inventory,
        "season": season,
        "cost": cost
    }

    res = requests.post("http://127.0.0.1:8000/predict", json=data).json()

    st.success(f"Predicted Price: ₹{res['predicted_price']}")
    st.write(f"Optimized Price: ₹{res['optimized_price']}")
    st.write(f"Max Profit: ₹{res['max_profit']}")
    st.divider()
st.subheader("📈 Demand vs Price Graph")

df = pd.read_csv("data/data.csv")

plt.figure()
plt.scatter(df['demand'], df['price'])

plt.xlabel("Demand")
plt.ylabel("Price")
plt.title("Demand vs Price")

st.pyplot(plt)

import streamlit as st
from utils import predict_price

st.set_page_config(page_title="Dynamic Pricing", layout="centered")

st.title("💰 Dynamic Pricing Engine")
st.markdown("### Predict optimal product price using AI")

st.divider()

competitor_price = st.number_input("🏷 Competitor Price", value=100)
demand = st.number_input("📊 Demand", value=100)
day = st.slider("📅 Day", 1, 31, 1)
month = st.slider("🗓 Month", 1, 12, 1)

if st.button("🚀 Predict Price"):
    result = predict_price(competitor_price, demand, day, month)
    st.success(f"💡 Suggested Price: ₹{result}")
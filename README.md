# 💰 Dynamic Pricing Engine (Advanced)

An AI-powered dynamic pricing system that predicts optimal product prices using machine learning and provides real-time recommendations through a web interface.

---

## 🚀 Project Overview

This project helps businesses automatically determine the best product price based on:

* 📊 Demand
* 🏷 Competitor Pricing
* 📦 Inventory Levels
* 🌦 Seasonal Factors

It also calculates:

* 💰 Revenue
* 📈 Profit
* 🤖 Optimized Price (maximum profit)

---

## 🧠 Features

* ✅ Machine Learning Model (Random Forest)
* ✅ Feature Engineering & Label Encoding
* ✅ FastAPI Backend (Real-time API)
* ✅ Streamlit Frontend (Interactive UI)
* ✅ Profit Optimization Logic
* ✅ Demand vs Price Visualization (Graph)

---

## 🛠 Tech Stack

* Python
* Pandas
* Scikit-learn
* FastAPI
* Uvicorn
* Streamlit
* Matplotlib

---

## 📂 Project Structure

dynamic_pricing/
│
├── data/
│   └── data.csv
├── model/
│   └── model.pkl
├── train.py
├── data_processor.py
├── backend_api.py
├── utils.py
└── app.py

---

## ⚙️ How to Run the Project

### 1️⃣ Install Dependencies

pip install pandas scikit-learn fastapi uvicorn streamlit matplotlib joblib

---

### 2️⃣ Train the Model

python train.py

---

### 3️⃣ Run Backend (API)

python -m uvicorn backend_api:app --reload

Open:
http://127.0.0.1:8000/docs

---

### 4️⃣ Run Frontend (App)

python -m streamlit run app.py

---

## 📊 How It Works

1. Data is preprocessed using label encoding
2. Random Forest model is trained on pricing data
3. FastAPI serves predictions via API
4. Streamlit UI collects user input
5. Model predicts price and calculates profit
6. Optimization logic finds best price
7. Graph shows demand vs price relationship

---

## 🎯 Use Cases

* 🛒 E-commerce pricing
* 🏨 Hotel room pricing
* ✈️ Airline ticket pricing
* 🛍 Retail inventory pricing






import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Smart Energy Optimizer", layout="wide")

st.title("⚡ Smart Energy Optimizer")

st.write("Monitor and optimize your electricity usage intelligently.")

# -------------------------------
# Sidebar Inputs
# -------------------------------
st.sidebar.header("Input Appliance Usage")

hours_fridge = st.sidebar.slider("Fridge Usage (hours/day)", 0, 24, 24)
hours_ac = st.sidebar.slider("AC Usage (hours/day)", 0, 24, 8)
hours_wm = st.sidebar.slider("Washing Machine (hours/day)", 0, 10, 1)
hours_tv = st.sidebar.slider("TV Usage (hours/day)", 0, 24, 4)

# Power ratings (Watts)
power = {
    "Fridge": 150,
    "AC": 2000,
    "Washing Machine": 500,
    "TV": 100
}

# -------------------------------
# Calculate Energy Consumption
# -------------------------------
energy = {
    "Fridge": hours_fridge * power["Fridge"] / 1000,
    "AC": hours_ac * power["AC"] / 1000,
    "Washing Machine": hours_wm * power["Washing Machine"] / 1000,
    "TV": hours_tv * power["TV"] / 1000
}

df = pd.DataFrame(list(energy.items()), columns=["Appliance", "kWh"])

st.subheader("🔋 Daily Energy Consumption (kWh)")
st.dataframe(df)

# -------------------------------
# Visualization
# -------------------------------
st.subheader("📊 Energy Usage Breakdown")

fig, ax = plt.subplots()
ax.pie(df["kWh"], labels=df["Appliance"], autopct='%1.1f%%')
st.pyplot(fig)

# -------------------------------
# Machine Learning Prediction
# -------------------------------
st.subheader("🤖 Future Consumption Prediction")

# Dummy training data
X = np.array([
    [20, 5, 1, 3],
    [24, 8, 2, 4],
    [22, 6, 1, 5],
    [18, 7, 1, 2],
    [23, 9, 2, 6]
])

y = np.array([10, 18, 14, 12, 20])  # Total kWh

model = LinearRegression()
model.fit(X, y)

user_input = np.array([[hours_fridge, hours_ac, hours_wm, hours_tv]])
prediction = model.predict(user_input)

st.success(f"Estimated Daily Consumption: {prediction[0]:.2f} kWh")

# -------------------------------
# Optimization Tips
# -------------------------------
st.subheader("💡 Optimization Suggestions")

tips = []

if hours_ac > 6:
    tips.append("Reduce AC usage or set temperature to 24°C.")

if hours_tv > 5:
    tips.append("Limit TV usage to save electricity.")

if hours_wm > 2:
    tips.append("Use washing machine with full load only.")

if hours_fridge == 24:
    tips.append("Ensure fridge door is properly closed and efficient.")

if not tips:
    tips.append("Great! Your energy usage is already optimized.")

for tip in tips:
    st.write("✔️", tip)

# -------------------------------
# Cost Estimation
# -------------------------------
st.subheader("💰 Cost Estimation")

rate = st.slider("Electricity Rate (₹/kWh)", 1.0, 15.0, 5.0)
total_energy = df["kWh"].sum()
cost = total_energy * rate

st.info(f"Estimated Daily Cost: ₹{cost:.2f}")
import streamlit as st
import pandas as pd
import plotly.express as px

# MUST be the first Streamlit command
st.set_page_config(
    page_title="Enterprise BI Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("Enterprise Business Intelligence Dashboard")
st.caption(
    "This dashboard provides operational and revenue insights "
    "to monitor order performance and delivery SLAs."
)

# --------------------
# LOAD DATA
# --------------------
orders = pd.read_csv("../data/cleaned/orders_cleaned.csv")
payments = pd.read_csv("../data/cleaned/payments_cleaned.csv")

# --------------------
# KPI CALCULATIONS
# --------------------
total_orders = orders["order_id"].nunique()
total_revenue = payments["payment_value"].sum()

orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"])
orders["order_delivered_customer_date"] = pd.to_datetime(
    orders["order_delivered_customer_date"]
)

orders = orders.dropna(subset=["order_delivered_customer_date"])

orders["delivery_time_days"] = (
    orders["order_delivered_customer_date"]
    - orders["order_purchase_timestamp"]
).dt.days

orders["is_late"] = orders["delivery_time_days"] > 7

avg_delivery_time = orders["delivery_time_days"].mean()
late_percentage = orders["is_late"].mean() * 100

# --------------------
# DISPLAY KPIs
# --------------------
st.markdown("### Key Business Metrics")

k1, k2, k3, k4 = st.columns(4)
k1.metric("Total Orders", f"{total_orders:,}")
k2.metric("Total Revenue (₹)", f"{total_revenue:,.0f}")
k3.metric("Avg Delivery Time (Days)", f"{avg_delivery_time:.1f}")
k4.metric("Late Delivery Rate", f"{late_percentage:.1f}%")

# --------------------
# CHARTS
# --------------------
st.markdown("### Operational Insights")

orders["order_month"] = orders["order_purchase_timestamp"].dt.to_period("M").astype(str)
orders_trend = orders.groupby("order_month")["order_id"].nunique()

c1, c2 = st.columns(2)

with c1:
    st.subheader("Orders Trend (Monthly)")
    st.line_chart(orders_trend)

with c2:
    st.subheader("Revenue by Payment Type")
    payment_revenue = payments.groupby("payment_type")["payment_value"].sum()
    payment_df = payment_revenue.reset_index()

fig_revenue = px.bar(
    payment_df,
    x="payment_type",
    y="payment_value",
    color="payment_type",
    title="Revenue by Payment Type",
    labels={"payment_value": "Revenue"}
)

st.plotly_chart(fig_revenue, use_container_width=True)


st.subheader("Delivery SLA Performance")
late_counts = orders["is_late"].value_counts()
late_counts.index = ["On Time", "Late"]
late_df = late_counts.reset_index()
late_df.columns = ["Status", "Count"]

fig_sla = px.bar(
    late_df,
    x="Status",
    y="Count",
    color="Status",
    color_discrete_map={
        "On Time": "#2ecc71",
        "Late": "#e74c3c"
    },
    title="Delivery SLA Performance"
)

st.plotly_chart(fig_sla, use_container_width=True)


#ml model
import joblib

model = joblib.load("../models/delivery_delay_model.pkl")
model_features = joblib.load("../models/model_features.pkl")
# Sidebar for user input

st.sidebar.header("Delivery Delay Prediction")

payment_value = st.sidebar.number_input(
    "Order Value (₹)", min_value=1.0, value=500.0
)

delivery_days = st.sidebar.number_input(
    "Expected Delivery Days", min_value=1, value=5
)



input_data = pd.DataFrame([{
    "payment_value": payment_value,
    "delivery_time_days": delivery_days
}])
expected_features = [
    'order_item_count',
    'order_purchase_hour',
    'payment_type_credit_card',
    'payment_type_debit_card',
    'payment_type_voucher'
]

# Reorder and select only these columns
input_data = input_data[expected_features]

if st.sidebar.button("Predict Delay"):
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ High Risk: Order likely to be DELAYED")
    else:
        st.success("✅ Low Risk: Order likely ON TIME")



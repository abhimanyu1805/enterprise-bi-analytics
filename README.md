# Enterprise Business Intelligence & Delivery Delay Analytics

An end-to-end **Business Intelligence and Analytics project** focused on analyzing e-commerce order data, extracting business KPIs, building an interactive BI dashboard, and applying a machine learning model to predict delivery delays.

---

## Project Overview

This project simulates a **real-world enterprise BI workflow** where raw transactional data is transformed into business insights and operational decision support tools.

The solution covers:
- Data cleaning and transformation
- Business-focused exploratory data analysis (EDA)
- KPI definition and monitoring
- Interactive BI dashboard using Streamlit
- Machine learning–based delivery delay prediction

---

## Dataset Source

The dataset used in this project is derived from the **Brazilian E-Commerce Public Dataset by Olist**, which is publicly available on Kaggle.

- **Source:** Olist (Brazilian e-commerce marketplace)
- **Data Type:** Real-world transactional e-commerce data
- **Scope Includes:**
  - Orders
  - Payments
  - Customers
  - Delivery timelines
  - Order status information

This dataset contains **thousands of real customer orders** and is widely used in **industry-oriented business intelligence, analytics, and data science case studies** to simulate real operational environments.


## Project Workflow

1. Raw Data Ingestion  
2. Data Cleaning & Transformation  
3. Business Exploratory Data Analysis (EDA)  
4. KPI Definition & Operational Insights  
5. Interactive BI Dashboard (Streamlit)  
6. Machine Learning Model for Delivery Delay Prediction  

---

## Key Business Metrics (KPIs)

- Total Orders  
- Total Revenue  
- Average Delivery Time (Days)  
- Late Delivery Rate (SLA Breach %)  

These KPIs help monitor:
- Order volume trends  
- Revenue performance  
- Delivery efficiency  
- Service Level Agreement (SLA) compliance  

---

## Dashboard Features

The Streamlit dashboard provides:

- **KPI Cards** for high-level business monitoring  
- **Orders Trend (Monthly)** to track demand patterns  
- **Revenue by Payment Type** to understand customer payment behavior  
- **Delivery SLA Performance** (On-Time vs Late Orders)  
- **ML-Based Prediction Panel** to assess delivery delay risk for new orders  

---

## Machine Learning Component

A supervised machine learning model is trained to predict whether an order is likely to be **delayed** based on operational features.

### ML Objective
- Binary classification: **Delayed vs On-Time Delivery**

### Features Used
- Order item count  
- Order purchase hour  
- Payment type (one-hot encoded)  

### Model Output
- Risk classification displayed directly in the Streamlit dashboard  
- Used for operational decision support and SLA monitoring  

---

## Technology Stack

- **Programming Language:** Python  
- **Data Analysis:** Pandas, NumPy  
- **Visualization:** Streamlit, Plotly  
- **Machine Learning:** Scikit-learn  
- **Model Persistence:** Joblib  
- **Version Control:** Git, GitHub  

---

## Project Structure

enterprise-bi-analytics/
│
├── data/
│ └── cleaned/
│
├── notebooks/
│ ├── data_cleaning.ipynb
│ ├── business_eda.ipynb
│ └── ml_model.ipynb
│
├── streamlit_app/
│ └── app.py
│
├── models/
│ ├── delivery_delay_model.pkl
│ └── model_features.pkl
│
├── screenshots/
│
└── README.md


---

## Screenshots

Project screenshots are available in the **screenshots/** folder:

- KPI Dashboard View  
- Revenue & Orders Visualizations  
- SLA Performance Chart  
- Delivery Delay Prediction Panel  

(These demonstrate the working dashboard and model integration.)

---

## Industry Relevance

This project reflects **industry-standard BI and analytics practices**, including:

- KPI-driven business analysis  
- Data-backed operational monitoring  
- Interactive dashboards for stakeholders  
- ML integration for predictive insights  
- End-to-end analytics pipeline ownership  

It aligns with roles such as:
- Business Intelligence Analyst  
- Data Analyst  
- Analytics Engineer  
- Junior Data Scientist  

---

## Future Enhancements

- Advanced feature engineering for ML model  
- Time-series forecasting for order demand  
- Deployment-ready dashboard (Docker / Cloud)  
- Integration with Power BI / Tableau for executive reporting  

---

## Author

**Abhimanyu Rajput**  
B.Tech – AI & Data Science  

---


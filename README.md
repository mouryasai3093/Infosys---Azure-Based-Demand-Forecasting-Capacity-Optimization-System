# Azure Demand Forecasting System

##  Project Overview
This project focuses on forecasting Azure cloud demand using time series data and machine learning techniques. The goal is to predict future demand based on historical patterns and improve resource planning.

---

##  Objectives
- Analyze time series demand data  
- Build forecasting models  
- Compare different models  
- Generate predictions for real-world usage  

---

##  Technologies Used
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Scikit-learn  
- XGBoost  
- Statsmodels (ARIMA)  
- Streamlit  

---

##  Dataset
The dataset contains:
- Timestamp (date/time)  
- Demand units  
- Azure region  
- Service type  
- Economic indicators (inflation, GDP, etc.)  

---

##  Project Workflow

###  Milestone 1: Data Collection & Preprocessing
- Loaded dataset  
- Handled missing values  
- Converted timestamp to datetime format  

###  Milestone 2: Feature Engineering & Model Training
- Created time-based features (year, month, day, etc.)  
- Applied lag features  
- Applied rolling mean  
- Trained Random Forest model  

###  Milestone 3: Model Comparison
- Implemented ARIMA model  
- Implemented XGBoost model  
- Compared models using graphs  
- Evaluated performance using R², MAE, RMSE  

###  Milestone 4: Model Integration
- Generated batch predictions  
- Saved output as `forecast_output.csv`  
- Created dashboard for Actual vs Forecast visualization  
- Explained automation and monitoring concepts  

---

##  Results
- Achieved high accuracy with R² score ≈ 0.96  
- XGBoost and Random Forest performed better than ARIMA  
- Forecast closely follows actual demand patterns  

---

##  Live Dashboard

🔗 https://eqjxwtgvajwqm5hesxkxnc.streamlit.app  

This dashboard is deployed using Streamlit and provides an interactive visualization of actual vs predicted demand.


##  Dashboard Features
- Actual vs Forecast comparison  
- Clear visualization of demand trends  
- Key metrics like total and peak forecast  

---

##  Applications
- Cloud resource planning  
- Capacity management  
- Cost optimization  
- Demand prediction  

---

##  Challenges
- Handling time series data  
- Feature engineering (lag & rolling mean)  
- Model selection  

---

##  Future Scope
- Real-time prediction system  
- Integration with cloud platforms  
- Advanced dashboards using Power BI  
- API deployment using Flask/FastAPI  

---

##  Conclusion
This project demonstrates how machine learning and time series forecasting can be used to predict cloud demand. The model achieved high accuracy and is useful for efficient decision-making in cloud environments.

---

##  Files Included
- `notebook.ipynb`  
- `dataset.csv`  
- `forecast_output.csv`  
- `app.py`  
- `requirements.txt`  
- `README.md`  
- `LICENSE`  

---

##  License
This project is licensed under the MIT License.


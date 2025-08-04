# User Behavior Analysis from Web Logs

This project analyzes user behavior using web server log data (e.g., clickstream). It includes data engineering steps to process logs and analytical steps to generate insights.

## 🔧 Tech Stack
- Python
- PySpark
- Pandas
- PostgreSQL (or local CSVs)
- Plotly Dash (for dashboard)

## 📊 Key Insights
- Session duration and frequency
- Bounce rates
- Most visited pages
- User funnel: landing → product → cart → checkout

## 📁 Folder Structure
- `etl/`: Spark ETL script to process raw logs
- `analysis/`: Python notebook with behavioral insights
- `data/`: Sample web logs (CSV format)
- `app/`: Plotly Dash dashboard

## 🚀 How to Run
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run ETL script:
   ```
   spark-submit etl/log_etl.py
   ```
3. Launch dashboard:
   ```
   python app/app.py
   ```

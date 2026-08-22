# NYC 311 Service Operations Analytics

End-to-end Data Analytics and Business Intelligence portfolio project using real NYC 311 service-request data from NYC Open Data.

## Business Objective

This project analyzes public-service demand and operational performance to identify:

- complaint categories driving the highest workload,
- boroughs and agencies with the largest request volume,
- peak demand periods by month, weekday, and hour,
- resolution-time patterns and long-running requests,
- recurring geographic complaint hotspots,
- opportunities for workload prioritization and service improvement.

## Dataset

**NYC 311 Service Requests from 2020 to Present**  
Provider: NYC Open Data / NYC311  
Dataset ID: `erm2-nwe9`

The official dataset is updated daily and contains tens of millions of public service-request records. Each row represents a 311 service request with attributes such as creation/closure timestamps, responding agency, problem/complaint category, status, and geographic location.

The repository does not store the full source dataset because it is very large. Instead, `src/download_data.py` retrieves a reproducible date slice directly from the NYC Open Data API.

Default project scope: **calendar year 2025**.

## Tech Stack

- **Python:** pandas, requests
- **SQL:** SQLite
- **Visualization:** Tableau / Power BI
- **Version Control:** Git + GitHub

## Repository Structure

```text
nyc-311-service-operations-analytics/
├── data/
│   └── README.md
├── dashboard/
│   └── README.md
├── notebooks/
│   └── 01_eda.ipynb
├── sql/
│   └── analysis_queries.sql
├── src/
│   ├── download_data.py
│   ├── prepare_data.py
│   └── build_database.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Data Pipeline

```text
NYC Open Data API
      ↓
src/download_data.py
      ↓
data/raw/nyc_311_2025.csv
      ↓
src/prepare_data.py
      ↓
data/processed/nyc_311_2025_clean.csv
      ↓
src/build_database.py
      ↓
data/processed/nyc_311_analytics.db
      ↓
SQL + EDA + Tableau / Power BI
```

## Core KPIs

1. Total Service Requests
2. Closed Request Rate
3. Average Resolution Time (hours)
4. Median Resolution Time (hours)
5. Open / Pending Requests
6. Requests by Agency
7. Requests by Complaint Type
8. Requests by Borough
9. Top ZIP Codes / Geographic Hotspots
10. Monthly, Weekday, and Hourly Demand Trends

## Key Analysis Questions

1. Which complaint types generate the largest volume of service requests?
2. Which agencies carry the highest workload?
3. Which boroughs generate the most requests?
4. When does service-request demand peak?
5. Which complaint types take the longest to resolve?
6. Which locations repeatedly generate similar complaints?
7. Which agencies or complaint categories show signs of backlog?
8. How does resolution performance differ across boroughs?

## Getting Started

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python src/download_data.py
python src/prepare_data.py
python src/build_database.py
jupyter notebook notebooks/01_eda.ipynb
```

The downloader retrieves 2025 service requests by default and saves them locally to `data/raw/nyc_311_2025.csv`.

## Current Deliverables

- [x] Reproducible API-based extraction
- [x] Data-cleaning and feature-engineering pipeline
- [x] SQLite analytics layer
- [x] SQL KPI and operations-analysis queries
- [x] Exploratory-analysis notebook starter
- [x] Tableau / Power BI dashboard blueprint
- [ ] Final EDA results and business insights
- [ ] Final dashboard
- [ ] Executive recommendations

## Data Ethics

This project uses publicly released government service-request data. Analysis is intended to examine aggregate operational patterns and should not be used to identify individuals.

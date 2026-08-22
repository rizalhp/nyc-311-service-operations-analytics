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

**NYC 311 Service Requests from 2010 to Present**  
Provider: NYC Open Data / NYC311  
Dataset ID: `erm2-nwe9`

The repository does not store the full source dataset because it is very large. Instead, `src/download_data.py` retrieves a reproducible date slice directly from the NYC Open Data API.

Default project scope: **calendar year 2025**.

## Tech Stack

- **Python:** pandas, requests
- **SQL:** SQLite-compatible analytical queries
- **Visualization:** Tableau / Power BI
- **Version Control:** Git + GitHub

## Repository Structure

```text
nyc-311-service-operations-analytics/
├── data/
│   ├── raw/
│   └── processed/
├── dashboard/
├── notebooks/
├── sql/
│   └── analysis_queries.sql
├── src/
│   ├── download_data.py
│   └── prepare_data.py
├── .gitignore
├── requirements.txt
└── README.md
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
```

The downloader retrieves 2025 service requests by default and saves them to `data/raw/nyc_311_2025.csv`.

## Planned Portfolio Deliverables

- reproducible API-based data extraction,
- cleaned analytical dataset,
- SQL KPI and trend analysis,
- exploratory data analysis notebook,
- Tableau / Power BI operations dashboard,
- executive summary with actionable recommendations.

## Data Ethics

This project uses publicly released government service-request data. Analysis is intended to examine aggregate operational patterns and should not be used to identify individuals.

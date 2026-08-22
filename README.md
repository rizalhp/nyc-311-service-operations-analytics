# NYC 311 Service Operations Analytics

[![CI](https://github.com/rizalhp/nyc-311-service-operations-analytics/actions/workflows/ci.yml/badge.svg)](https://github.com/rizalhp/nyc-311-service-operations-analytics/actions/workflows/ci.yml)

End-to-end **Data Analytics and Business Intelligence portfolio project** using real public-service operations data from NYC Open Data.

## Business Objective

This project analyzes NYC 311 demand and operational performance to identify:

- complaint categories driving the highest workload,
- boroughs and agencies with the largest request volume,
- peak demand periods by month, weekday, and hour,
- resolution-time patterns and long-running requests,
- recurring geographic complaint hotspots,
- opportunities for workload prioritization and service improvement.

The project is designed as a reproducible analyst workflow rather than a one-off notebook: API extraction → cleaning and feature engineering → SQLite analytics layer → SQL/Python analysis → BI dashboard → executive recommendations.

## Dataset

**NYC 311 Service Requests from 2020 to Present**  
Provider: NYC Open Data / NYC311  
Dataset ID: `erm2-nwe9`

The repository intentionally does **not** store the full source dataset because it contains tens of millions of records and is updated regularly. `src/download_data.py` retrieves a reproducible date slice directly from the NYC Open Data API.

Default analytical scope: **calendar year 2025**.

## Tech Stack

- **Python:** pandas, requests
- **SQL:** SQLite
- **Visualization:** Tableau / Power BI
- **Testing:** pytest
- **Automation:** GitHub Actions
- **Version Control:** Git + GitHub

## Repository Structure

```text
nyc-311-service-operations-analytics/
├── .github/workflows/
│   └── ci.yml
├── dashboard/
│   └── README.md
├── data/
│   └── README.md
├── docs/
│   └── data_dictionary.md
├── notebooks/
│   └── 01_eda.ipynb
├── sql/
│   └── analysis_queries.sql
├── src/
│   ├── download_data.py
│   ├── prepare_data.py
│   └── build_database.py
├── tests/
│   └── test_prepare_data.py
├── .gitignore
├── LICENSE
├── Makefile
├── requirements-dev.txt
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
SQL + Python EDA
        ↓
Tableau / Power BI
        ↓
Executive Recommendations
```

## Core KPIs

1. Total Service Requests
2. Closed Request Rate
3. Average Resolution Time
4. Median Resolution Time
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

## Quick Start

### 1. Create an environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

### 2. Run the complete pipeline

```bash
make pipeline
```

Equivalent commands:

```bash
python src/download_data.py
python src/prepare_data.py
python src/build_database.py
```

### 3. Run automated tests

```bash
make test
```

### 4. Explore the data

```bash
jupyter notebook notebooks/01_eda.ipynb
```

## Custom Date Range

The extractor is configurable without editing source code:

```bash
python src/download_data.py \
  --start 2025-01-01T00:00:00.000 \
  --end 2025-04-01T00:00:00.000 \
  --output data/raw/nyc_311_q1_2025.csv
```

The downloader writes each API page directly to CSV, avoiding the need to hold the entire dataset in memory.

## SQL Analysis

`sql/analysis_queries.sql` includes queries for:

- overall operational KPIs,
- complaint workload,
- agency workload and resolution performance,
- borough-level performance,
- monthly / weekday / hourly demand,
- longest-resolution complaint categories,
- ZIP-code hotspots,
- potential backlog by agency and complaint type.

## Dashboard Blueprint

The planned BI deliverable contains three views:

1. **Executive Overview** — KPIs, demand trends, boroughs, agencies, complaint categories.
2. **Service Performance** — resolution time, backlog, workload vs. service speed.
3. **Demand & Geography** — temporal patterns and geographic hotspots.

See `dashboard/README.md` for the proposed layout and filters.

## Data Quality & Reproducibility

The cleaning pipeline:

- parses operational timestamps,
- trims categorical text fields,
- removes duplicate `unique_key` records,
- calculates resolution hours and days,
- rejects negative resolution intervals,
- standardizes borough names,
- converts geographic coordinates to numeric values,
- engineers month, weekday, hour, and closed-status features.

Automated tests validate core transformation rules, while GitHub Actions runs compilation and pytest checks on pushes and pull requests.

See `docs/data_dictionary.md` for field definitions and analytical caveats.

## Current Project Status

- [x] Reproducible API-based extraction
- [x] Memory-safe paginated download
- [x] Data cleaning and feature engineering
- [x] SQLite analytics layer
- [x] SQL KPI and operations analysis
- [x] EDA notebook starter
- [x] Tableau / Power BI dashboard blueprint
- [x] Data dictionary
- [x] Automated tests
- [x] GitHub Actions CI
- [ ] Final 2025 analytical results
- [ ] Final BI dashboard
- [ ] Executive findings and recommendations

## Data Ethics

This project uses publicly released government service-request data. Analysis is intended to examine aggregate operational patterns and should not be used to identify individuals. Service-resolution metrics should also be interpreted in context because different agencies and complaint categories can follow different operational workflows.

## License

Project code and documentation are available under the MIT License. Source data remains subject to NYC Open Data terms and policies.

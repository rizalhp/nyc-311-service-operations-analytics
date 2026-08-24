# Analysis Workflow

This document summarizes the recommended workflow for producing reproducible NYC 311 operational analysis from the repository.

## 1. Extract

Use `src/download_data.py` to retrieve the required date range from NYC Open Data. Keep raw extracts in `data/raw/` and avoid committing large source files.

## 2. Transform

Run `src/prepare_data.py` to clean timestamps, normalize categorical fields, remove duplicate service requests, and derive analytical features such as resolution time, month, weekday, hour, and closed status.

## 3. Load

Run `src/build_database.py` to create the SQLite analytical layer used by downstream SQL analysis.

## 4. Validate

Run the automated test suite before interpreting results:

```bash
make test
```

Review row counts, missing values, duplicate `unique_key` records, and invalid or negative resolution intervals when changing the pipeline.

## 5. Analyze

Use `sql/analysis_queries.sql` and the exploratory notebook to answer the project's core operational questions. Compare both demand volume and service speed so high-volume categories are not automatically interpreted as poor-performing categories.

## 6. Visualize

Build the dashboard around three analytical views:

1. Executive Overview
2. Service Performance
3. Demand & Geography

Keep KPI definitions consistent with the SQL layer and document any dashboard-specific calculations.

## 7. Communicate Findings

Translate analysis into concise operational findings. Each recommendation should connect an observed metric or pattern to a practical action, while noting important limitations such as differences in agency workflows and complaint types.

## Reproducibility Checklist

- Use a clearly defined extraction period.
- Keep transformation logic in source-controlled scripts.
- Run tests after pipeline changes.
- Keep KPI definitions consistent across SQL, notebooks, and dashboards.
- Document assumptions and caveats alongside final findings.

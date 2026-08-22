# Data Directory

This project intentionally excludes large generated data files from GitHub.

## Raw data

Run:

```bash
python src/download_data.py
```

Output:

`data/raw/nyc_311_2025.csv`

## Processed data

Run:

```bash
python src/prepare_data.py
python src/build_database.py
```

Outputs:

- `data/processed/nyc_311_2025_clean.csv`
- `data/processed/nyc_311_analytics.db`

Source dataset: NYC Open Data, dataset ID `erm2-nwe9`.

from pathlib import Path
import time

import pandas as pd
import requests

API_URL = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"
OUTPUT = Path("data/raw/nyc_311_2025.csv")

START_DATE = "2025-01-01T00:00:00.000"
END_DATE = "2026-01-01T00:00:00.000"
LIMIT = 50000

SELECT_COLUMNS = [
    "unique_key",
    "created_date",
    "closed_date",
    "agency",
    "agency_name",
    "complaint_type",
    "descriptor",
    "location_type",
    "incident_zip",
    "city",
    "borough",
    "status",
    "due_date",
    "resolution_description",
    "resolution_action_updated_date",
    "community_board",
    "latitude",
    "longitude",
    "open_data_channel_type",
]


def fetch_page(offset: int) -> list[dict]:
    params = {
        "$select": ",".join(SELECT_COLUMNS),
        "$where": (
            f"created_date >= '{START_DATE}' "
            f"AND created_date < '{END_DATE}'"
        ),
        "$order": "created_date, unique_key",
        "$limit": LIMIT,
        "$offset": offset,
    }

    response = requests.get(API_URL, params=params, timeout=60)
    response.raise_for_status()
    return response.json()


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    all_rows: list[dict] = []
    offset = 0

    while True:
        rows = fetch_page(offset)
        if not rows:
            break

        all_rows.extend(rows)
        print(f"Downloaded {len(all_rows):,} rows")

        if len(rows) < LIMIT:
            break

        offset += LIMIT
        time.sleep(0.15)

    df = pd.DataFrame(all_rows)
    df.to_csv(OUTPUT, index=False)
    print(f"Saved {len(df):,} rows to {OUTPUT}")


if __name__ == "__main__":
    main()

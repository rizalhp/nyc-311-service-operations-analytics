from __future__ import annotations

import argparse
import time
from pathlib import Path

import pandas as pd
import requests

API_URL = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"
DEFAULT_START = "2025-01-01T00:00:00.000"
DEFAULT_END = "2026-01-01T00:00:00.000"
DEFAULT_OUTPUT = Path("data/raw/nyc_311_2025.csv")
LIMIT = 50_000

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


def fetch_page(session: requests.Session, offset: int, start_date: str, end_date: str) -> list[dict]:
    params = {
        "$select": ",".join(SELECT_COLUMNS),
        "$where": f"created_date >= '{start_date}' AND created_date < '{end_date}'",
        "$order": "created_date, unique_key",
        "$limit": LIMIT,
        "$offset": offset,
    }
    response = session.get(API_URL, params=params, timeout=90)
    response.raise_for_status()
    return response.json()


def download(start_date: str, end_date: str, output: Path) -> int:
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        output.unlink()

    offset = 0
    total_rows = 0
    write_header = True

    with requests.Session() as session:
        session.headers.update({"User-Agent": "nyc-311-service-operations-analytics/1.0"})

        while True:
            rows = fetch_page(session, offset, start_date, end_date)
            if not rows:
                break

            chunk = pd.DataFrame(rows)
            chunk.to_csv(
                output,
                mode="w" if write_header else "a",
                header=write_header,
                index=False,
            )
            write_header = False

            total_rows += len(chunk)
            print(f"Downloaded {total_rows:,} rows")

            if len(rows) < LIMIT:
                break

            offset += LIMIT
            time.sleep(0.15)

    print(f"Saved {total_rows:,} rows to {output}")
    return total_rows


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Download NYC 311 service requests from NYC Open Data.")
    parser.add_argument("--start", default=DEFAULT_START, help="Inclusive start timestamp.")
    parser.add_argument("--end", default=DEFAULT_END, help="Exclusive end timestamp.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="CSV output path.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    download(args.start, args.end, args.output)


if __name__ == "__main__":
    main()

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

DEFAULT_INPUT = Path("data/raw/nyc_311_2025.csv")
DEFAULT_OUTPUT = Path("data/processed/nyc_311_2025_clean.csv")

DATE_COLUMNS = [
    "created_date",
    "closed_date",
    "due_date",
    "resolution_action_updated_date",
]

TEXT_COLUMNS = [
    "agency",
    "agency_name",
    "complaint_type",
    "descriptor",
    "location_type",
    "city",
    "borough",
    "status",
    "open_data_channel_type",
]


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    for column in DATE_COLUMNS:
        if column in df.columns:
            df[column] = pd.to_datetime(df[column], errors="coerce")

    for column in TEXT_COLUMNS:
        if column in df.columns:
            df[column] = df[column].astype("string").str.strip()

    if "unique_key" in df.columns:
        df = df.drop_duplicates(subset=["unique_key"], keep="last")

    if {"created_date", "closed_date"}.issubset(df.columns):
        df["resolution_hours"] = (
            (df["closed_date"] - df["created_date"]).dt.total_seconds() / 3600
        )
        df.loc[df["resolution_hours"] < 0, "resolution_hours"] = pd.NA
        df["resolution_days"] = df["resolution_hours"] / 24

    if "created_date" in df.columns:
        df["created_year"] = df["created_date"].dt.year
        df["created_month_num"] = df["created_date"].dt.month
        df["created_month"] = df["created_date"].dt.strftime("%Y-%m")
        df["created_weekday"] = df["created_date"].dt.day_name()
        df["created_hour"] = df["created_date"].dt.hour
        df["created_date_only"] = df["created_date"].dt.date

    if "status" in df.columns:
        normalized_status = df["status"].fillna("").str.lower()
        df["is_closed"] = normalized_status.eq("closed")

    if "borough" in df.columns:
        df["borough"] = df["borough"].str.title()
        df.loc[df["borough"].isin(["Unspecified", "0 Unspecified"]), "borough"] = pd.NA

    for column in ["latitude", "longitude"]:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")

    return df


def prepare(input_path: Path, output_path: Path) -> pd.DataFrame:
    if not input_path.exists():
        raise FileNotFoundError(f"Raw dataset not found: {input_path}")

    raw = pd.read_csv(input_path, low_memory=False)
    clean = clean_dataframe(raw)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    clean.to_csv(output_path, index=False)

    print(f"Raw rows: {len(raw):,}")
    print(f"Clean rows: {len(clean):,}")
    print(f"Saved cleaned dataset to {output_path}")
    return clean


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Clean and feature-engineer NYC 311 data.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    prepare(args.input, args.output)


if __name__ == "__main__":
    main()

from pathlib import Path
import sqlite3

import pandas as pd

INPUT = Path("data/processed/nyc_311_2025_clean.csv")
DATABASE = Path("data/processed/nyc_311_analytics.db")
TABLE_NAME = "nyc_311"
CHUNK_SIZE = 100_000


def main() -> None:
    if not INPUT.exists():
        raise FileNotFoundError(
            f"Clean dataset not found: {INPUT}. Run src/prepare_data.py first."
        )

    DATABASE.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DATABASE) as connection:
        first_chunk = True

        for chunk in pd.read_csv(INPUT, chunksize=CHUNK_SIZE, low_memory=False):
            chunk.to_sql(
                TABLE_NAME,
                connection,
                if_exists="replace" if first_chunk else "append",
                index=False,
            )
            first_chunk = False

        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_nyc311_agency ON nyc_311(agency)"
        )
        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_nyc311_complaint ON nyc_311(complaint_type)"
        )
        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_nyc311_borough ON nyc_311(borough)"
        )
        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_nyc311_month ON nyc_311(created_month)"
        )
        connection.commit()

    print(f"SQLite analytics database created at {DATABASE}")


if __name__ == "__main__":
    main()

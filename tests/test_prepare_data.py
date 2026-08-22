import pandas as pd

from src.prepare_data import clean_dataframe


def test_clean_dataframe_engineers_expected_fields():
    raw = pd.DataFrame(
        {
            "unique_key": ["1", "1", "2"],
            "created_date": [
                "2025-01-01T08:00:00",
                "2025-01-01T08:00:00",
                "2025-02-03T10:30:00",
            ],
            "closed_date": [
                "2025-01-01T10:00:00",
                "2025-01-01T11:00:00",
                None,
            ],
            "agency": [" NYPD ", " NYPD ", " DOT "],
            "complaint_type": ["Noise", "Noise", "Street Condition"],
            "borough": ["BROOKLYN", "BROOKLYN", "UNSPECIFIED"],
            "status": ["Closed", "Closed", "Open"],
            "latitude": ["40.1", "40.1", "invalid"],
            "longitude": ["-73.9", "-73.9", "-74.0"],
        }
    )

    clean = clean_dataframe(raw)

    assert len(clean) == 2
    assert clean.loc[clean["unique_key"] == "1", "resolution_hours"].iloc[0] == 3.0
    assert clean.loc[clean["unique_key"] == "1", "agency"].iloc[0] == "NYPD"
    assert clean.loc[clean["unique_key"] == "1", "borough"].iloc[0] == "Brooklyn"
    assert clean.loc[clean["unique_key"] == "1", "is_closed"].iloc[0]
    assert pd.isna(clean.loc[clean["unique_key"] == "2", "borough"].iloc[0])
    assert pd.isna(clean.loc[clean["unique_key"] == "2", "latitude"].iloc[0])
    assert "created_month" in clean.columns
    assert "created_weekday" in clean.columns
    assert "created_hour" in clean.columns


def test_negative_resolution_time_becomes_missing():
    raw = pd.DataFrame(
        {
            "unique_key": ["1"],
            "created_date": ["2025-01-02T12:00:00"],
            "closed_date": ["2025-01-02T10:00:00"],
        }
    )

    clean = clean_dataframe(raw)
    assert pd.isna(clean.loc[0, "resolution_hours"])

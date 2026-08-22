# Analytical Data Dictionary

This document describes the fields used by the portfolio analysis. Source fields originate from NYC Open Data dataset `erm2-nwe9`; engineered fields are created in `src/prepare_data.py`.

| Field | Type | Source / Engineered | Description |
|---|---|---|---|
| `unique_key` | text | Source | Unique identifier for a 311 service request. |
| `created_date` | datetime | Source | Timestamp when the request was created. |
| `closed_date` | datetime | Source | Timestamp when the request was closed, when available. |
| `agency` | text | Source | Acronym of the responding agency. |
| `agency_name` | text | Source | Full responding agency name. |
| `complaint_type` | text | Source | Primary service-request or complaint category. |
| `descriptor` | text | Source | More specific description of the complaint. |
| `location_type` | text | Source | Type of location associated with the request. |
| `incident_zip` | text | Source | ZIP code associated with the request. |
| `city` | text | Source | City reported for the service request. |
| `borough` | text | Source | NYC borough, standardized to title case during cleaning. |
| `status` | text | Source | Current request status. |
| `due_date` | datetime | Source | Target due date when supplied by the source system. |
| `resolution_description` | text | Source | Agency-provided resolution description. |
| `resolution_action_updated_date` | datetime | Source | Last update timestamp for resolution activity. |
| `community_board` | text | Source | NYC community board associated with the request. |
| `latitude` | numeric | Source | Latitude used for geographic analysis. |
| `longitude` | numeric | Source | Longitude used for geographic analysis. |
| `open_data_channel_type` | text | Source | Channel used to create the service request. |
| `resolution_hours` | numeric | Engineered | Hours between creation and closure; negative intervals are treated as missing. |
| `resolution_days` | numeric | Engineered | `resolution_hours / 24`. |
| `created_year` | integer | Engineered | Calendar year of request creation. |
| `created_month_num` | integer | Engineered | Numeric month of request creation. |
| `created_month` | text | Engineered | Year-month key in `YYYY-MM` format. |
| `created_weekday` | text | Engineered | Weekday name of request creation. |
| `created_hour` | integer | Engineered | Hour of day (0-23) when the request was created. |
| `created_date_only` | date | Engineered | Calendar date of request creation. |
| `is_closed` | boolean | Engineered | `True` when normalized status equals `closed`. |

## Analytical Notes

- A missing `closed_date` should not automatically be interpreted as poor performance; some request types may use different lifecycle rules.
- Resolution-time comparisons should be made within operationally comparable complaint categories and agencies.
- Geographic analysis should be presented in aggregate and should not attempt to identify individuals.

# Data Quality Checklist

Use this checklist before refreshing the NYC 311 analysis or publishing dashboard results.

## 1. Record Integrity

- Confirm `unique_key` is populated for every request.
- Check that `unique_key` does not contain unexpected duplicates.
- Confirm the processed dataset contains at least one row.

## 2. Date Validation

- Verify `created_date` is not missing for analytical records.
- Confirm `closed_date >= created_date` whenever both timestamps exist.
- Flag future-dated `created_date` values for review.
- Confirm `resolution_hours` is non-negative when present.

## 3. Category Consistency

- Review null or blank values in `agency`, `complaint_type`, `status`, and `borough`.
- Confirm borough names use a consistent format.
- Review unusually rare complaint categories before grouping or filtering them.

## 4. Geographic Checks

- Validate latitude is between -90 and 90.
- Validate longitude is between -180 and 180.
- Review records with ZIP codes but missing boroughs, or boroughs but missing ZIP codes.

## 5. Analytical Sanity Checks

- Closed requests should generally have a `closed_date`.
- Open requests should not be assigned a positive resolution duration derived from closure time.
- Compare request counts before and after cleaning to quantify removed or transformed records.
- Check whether extreme resolution times materially distort averages; use medians or percentiles when appropriate.

## 6. Before Publishing

Record the following for reproducibility:

- source extract date,
- processed row count,
- duplicate count,
- null-rate summary for critical fields,
- min/max creation dates,
- validation exceptions that were intentionally retained.

A dashboard refresh should only proceed after unexpected validation failures have been investigated.
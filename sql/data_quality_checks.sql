-- NYC 311 Service Operations Analytics
-- Data quality checks for a table named nyc_311.

-- 1) Dataset size
SELECT COUNT(*) AS total_rows
FROM nyc_311;

-- 2) Duplicate request identifiers
SELECT
    unique_key,
    COUNT(*) AS duplicate_count
FROM nyc_311
GROUP BY unique_key
HAVING COUNT(*) > 1
ORDER BY duplicate_count DESC;

-- 3) Missing critical analytical fields
SELECT
    SUM(CASE WHEN unique_key IS NULL OR TRIM(CAST(unique_key AS TEXT)) = '' THEN 1 ELSE 0 END) AS missing_unique_key,
    SUM(CASE WHEN created_date IS NULL THEN 1 ELSE 0 END) AS missing_created_date,
    SUM(CASE WHEN agency IS NULL OR TRIM(agency) = '' THEN 1 ELSE 0 END) AS missing_agency,
    SUM(CASE WHEN complaint_type IS NULL OR TRIM(complaint_type) = '' THEN 1 ELSE 0 END) AS missing_complaint_type,
    SUM(CASE WHEN status IS NULL OR TRIM(status) = '' THEN 1 ELSE 0 END) AS missing_status
FROM nyc_311;

-- 4) Invalid closure chronology
SELECT COUNT(*) AS invalid_close_before_create
FROM nyc_311
WHERE closed_date IS NOT NULL
  AND created_date IS NOT NULL
  AND closed_date < created_date;

-- 5) Invalid engineered resolution duration
SELECT COUNT(*) AS negative_resolution_hours
FROM nyc_311
WHERE resolution_hours < 0;

-- 6) Closed requests without a closure timestamp
SELECT COUNT(*) AS closed_without_closed_date
FROM nyc_311
WHERE LOWER(COALESCE(status, '')) = 'closed'
  AND closed_date IS NULL;

-- 7) Geographic coordinate range checks
SELECT
    SUM(CASE WHEN latitude IS NOT NULL AND (latitude < -90 OR latitude > 90) THEN 1 ELSE 0 END) AS invalid_latitude,
    SUM(CASE WHEN longitude IS NOT NULL AND (longitude < -180 OR longitude > 180) THEN 1 ELSE 0 END) AS invalid_longitude
FROM nyc_311;

-- 8) Category completeness overview
SELECT
    borough,
    COUNT(*) AS requests
FROM nyc_311
GROUP BY borough
ORDER BY requests DESC;

-- 9) Resolution-time distribution sanity check
SELECT
    MIN(resolution_hours) AS min_resolution_hours,
    ROUND(AVG(resolution_hours), 2) AS avg_resolution_hours,
    MAX(resolution_hours) AS max_resolution_hours
FROM nyc_311
WHERE resolution_hours IS NOT NULL;

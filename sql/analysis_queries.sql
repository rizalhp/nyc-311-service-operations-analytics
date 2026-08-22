-- NYC 311 Service Operations Analytics
-- Load data/processed/nyc_311_2025_clean.csv into a table named nyc_311.

-- 1) Overall operational KPIs
SELECT
    COUNT(*) AS total_requests,
    SUM(CASE WHEN LOWER(status) = 'closed' THEN 1 ELSE 0 END) AS closed_requests,
    ROUND(
        100.0 * SUM(CASE WHEN LOWER(status) = 'closed' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS closed_rate_pct,
    ROUND(AVG(resolution_hours), 2) AS avg_resolution_hours
FROM nyc_311;

-- 2) Top complaint types by workload
SELECT
    complaint_type,
    COUNT(*) AS requests,
    ROUND(AVG(resolution_hours), 2) AS avg_resolution_hours
FROM nyc_311
GROUP BY complaint_type
ORDER BY requests DESC
LIMIT 20;

-- 3) Agency workload and resolution performance
SELECT
    agency,
    COUNT(*) AS requests,
    ROUND(AVG(resolution_hours), 2) AS avg_resolution_hours
FROM nyc_311
GROUP BY agency
ORDER BY requests DESC;

-- 4) Borough-level performance
SELECT
    borough,
    COUNT(*) AS requests,
    ROUND(AVG(resolution_hours), 2) AS avg_resolution_hours
FROM nyc_311
WHERE borough IS NOT NULL
GROUP BY borough
ORDER BY requests DESC;

-- 5) Monthly demand trend
SELECT
    created_month,
    COUNT(*) AS requests
FROM nyc_311
GROUP BY created_month
ORDER BY created_month;

-- 6) Weekday demand pattern
SELECT
    created_weekday,
    COUNT(*) AS requests
FROM nyc_311
GROUP BY created_weekday
ORDER BY requests DESC;

-- 7) Hourly demand pattern
SELECT
    created_hour,
    COUNT(*) AS requests
FROM nyc_311
GROUP BY created_hour
ORDER BY created_hour;

-- 8) Complaint types with the longest resolution time
SELECT
    complaint_type,
    COUNT(*) AS closed_requests,
    ROUND(AVG(resolution_hours), 2) AS avg_resolution_hours
FROM nyc_311
WHERE resolution_hours IS NOT NULL
GROUP BY complaint_type
HAVING COUNT(*) >= 100
ORDER BY avg_resolution_hours DESC
LIMIT 20;

-- 9) Geographic hotspots by ZIP code
SELECT
    incident_zip,
    borough,
    COUNT(*) AS requests
FROM nyc_311
WHERE incident_zip IS NOT NULL
GROUP BY incident_zip, borough
ORDER BY requests DESC
LIMIT 25;

-- 10) Potential backlog by agency and complaint type
SELECT
    agency,
    complaint_type,
    COUNT(*) AS open_requests
FROM nyc_311
WHERE LOWER(COALESCE(status, '')) <> 'closed'
GROUP BY agency, complaint_type
HAVING COUNT(*) >= 25
ORDER BY open_requests DESC
LIMIT 30;

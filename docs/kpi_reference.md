# KPI Reference

This reference defines the main operational metrics used in the NYC 311 portfolio analysis.

| KPI | Definition | Suggested Formula | Interpretation |
|---|---|---|---|
| Total Requests | Number of service requests in the selected scope. | `COUNT(*)` | Measures workload or demand volume. |
| Closed Requests | Requests whose normalized status is `closed`. | `SUM(status = 'closed')` | Measures completed request volume. |
| Closed Rate | Share of requests classified as closed. | `closed_requests / total_requests * 100` | Useful for monitoring completion levels, but should be interpreted with request age and category. |
| Average Resolution Hours | Mean time from request creation to closure for records with valid closure timestamps. | `AVG(resolution_hours)` | Indicates typical processing speed, but can be sensitive to extreme values. |
| Requests by Complaint Type | Number of requests grouped by complaint category. | `COUNT(*) GROUP BY complaint_type` | Highlights major demand drivers. |
| Requests by Agency | Number of requests assigned to each agency. | `COUNT(*) GROUP BY agency` | Shows workload distribution across agencies. |
| Monthly Requests | Number of requests created in each calendar month. | `COUNT(*) GROUP BY created_month` | Shows seasonality and demand trends. |
| Open Backlog | Requests that are not classified as closed. | `COUNT(*) WHERE status <> 'closed'` | Indicates unresolved workload at the time represented by the dataset. |
| ZIP Hotspot Volume | Request count by incident ZIP code. | `COUNT(*) GROUP BY incident_zip` | Identifies high-volume geographic areas. |

## Interpretation Guardrails

- Do not compare average resolution times across agencies without considering differences in complaint mix.
- A high open backlog may reflect recent requests rather than poor performance.
- Closed rate is more informative when paired with request age, resolution time, and workload volume.
- Large outliers can distort average resolution time; median and percentile metrics are useful follow-up measures.
- Geographic hotspots represent request volume, not necessarily population-adjusted service intensity.

## Recommended Dashboard Pairings

For portfolio storytelling, pair metrics rather than presenting them in isolation:

- **Demand + speed:** total requests with average resolution hours.
- **Volume + completion:** requests by agency with closed rate.
- **Trend + operations:** monthly requests with backlog trend.
- **Hotspot + category:** ZIP-level volume with dominant complaint types.

These pairings help turn descriptive counts into operational insights that are easier to explain during a portfolio review or interview.
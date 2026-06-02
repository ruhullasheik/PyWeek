# Data Analysis: Weather

**Difficulty**: Medium  
**Skills**: CSV, statistics, matplotlib (optional)

## Spec

Analyze a weather dataset and produce insights.

Download a CSV from: https://www.ncdc.noaa.gov/cdo-web/search
Or use the provided sample: `weather_sample.csv`

### Features

```
python weather.py analyze data.csv
# Output:
# Records: 365
# Date range: 2025-01-01 to 2025-12-31
# Avg temp: 15.3°C (min: -2.1°C, max: 34.7°C)
# Total precipitation: 823.4mm
# Hottest day: 2025-07-15 (34.7°C)
# Coldest day: 2025-01-18 (-2.1°C)

python weather.py monthly data.csv
# Output a monthly summary table

python weather.py plot data.csv
# Save a temperature trend plot as 'weather_trend.png'
```

### Requirements

- Use only stdlib (csv, statistics, datetime) or optionally matplotlib
- Handle missing data gracefully
- Output well-formatted tables
- At least 3 analytic functions

### Extension Ideas

- Moving average calculation
- Compare two years
- Humidity correlation analysis

# NYC Taxi Data Pipeline and Analytics (H2 2025)

## Project Overview
This project is a hands-on implementation of a data pipeline processing real-world NYC Taxi (Yellow Cabs) data from the second half of 2025 (July to December). The pipeline is built using PySpark and structured according to the three-tier Delta Lake (Medallion Architecture). 

The entire project was developed and verified within the free Databricks Community Edition platform using Unity Catalog (`nyctaxi`) for data isolation and schema management.

## Technology Stack
* **Platform:** Databricks Community Edition
* **Data Governance:** Unity Catalog (Catalog: `nyctaxi`)
* **Language & Engine:** Python, PySpark (SQL and DataFrames)
* **Storage Format:** Delta Lake / Parquet

---

## Repository Structure
```text
├── one_off/
│   └── backfill_historical_yellow_trips.ipynb  # Initial backfill notebook
├── quick_analysis/
│   └── yellow_taxi_eda.ipynb                    # Exploratory Data Analysis (EDA)
└── transformations/                             # Core ETL Pipeline
    ├── 01_bronze/
    │   └── yellow_trips_raw.ipynb               # Raw ingestion with processed_timestamp
    ├── 02_silver/
    │   ├── taxi_zone_lookup.ipynb               # Lookup standardization (SCD effective/end_date)
    │   ├── yellow_trips_cleansed.ipynb          # Schema cleaning & snake_case renaming
    │   └── yellow_trips_enriched.ipynb          # JOIN of trips and zones + duration calculation
    └── 03_gold/
        └── daily_trip_summary.ipynb             # Final BI-ready report aggregation

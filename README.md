# NYC Taxi Data Pipeline and Analytics (H2 2025)

## Project Overview
This project implements a robust, scalable, end-to-end data pipeline processing real-world NYC Taxi (Yellow Cabs) data covering the second half of 2025 (July to December). The solution is designed following production standards for Azure Databricks and implemented using PySpark and the modern three-tier Delta Lake (Medallion Architecture). Due to environment availability, the pipeline was deployed and verified within the Databricks Community Edition platform.

Data governance and schema isolation are managed via Unity Catalog (`nyctaxi`), ensuring a transparent data lineage from raw backend files to production-ready business aggregations.

## Technology Stack
* **Environment and Orchestration:** Databricks Community Edition (with architecture ready for Azure Databricks production deployment)
* **Data Governance:** Unity Catalog (Catalog: `nyctaxi`)
* **Language and Engine:** Python, PySpark (SQL and DataFrames)
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

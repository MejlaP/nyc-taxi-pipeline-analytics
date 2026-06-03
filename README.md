# NYC Taxi Data Pipeline and Analytics (H2 2025)

## Project Overview
This project is a hands-on implementation of a data pipeline processing real-world NYC Taxi (Yellow Cabs) data from the second half of 2025 (July to December). The pipeline is built using Apache Spark and structured according to the three-tier Delta Lake (Medallion Architecture). 

The entire project was developed and verified within the free Databricks Community Edition platform using Unity Catalog (`nyctaxi`) for data isolation and schema management.

## Technology Stack
* **Platform:** Databricks Community Edition
* **Data Governance:** Unity Catalog (Catalog: `nyctaxi`)
* **Languages:** Python, SQL
* **Processing Engine:** Apache Spark (PySpark and Spark SQL)
* **Storage Format:** Delta Lake / Parquet

---

## Repository Structure
```text
├── one_off/                                     # 1. Environment Setup & Backfill (Run first)
│   ├── creating_catalogs_schemas_volume.ipynb   # Step 1: Create catalog, schemas, and Unity Catalog Volume
│   ├── create_folder_for_taxi_zone_lookup.ipynb # Step 2: Prepare directory structure for lookup reference
│   └── backfill_historical_yellow_trips.ipynb   # Step 3: Run initial historical data load
├── transformations/                             # 2. Core ETL Pipeline (Chronological flow)
│   ├── 01_bronze/
│   │   └── yellow_trips_raw.ipynb               # Raw ingestion with processed_timestamp
│   ├── 02_silver/
│   │   ├── taxi_zone_lookup.ipynb               # Lookup standardization (SCD effective/end_date)
│   │   ├── yellow_trips_cleansed.ipynb          # Schema cleaning & snake_case renaming
│   │   └── yellow_trips_enriched.ipynb          # JOIN of trips and zones + duration calculation
│   └── 03_gold/
│       └── daily_trip_summary.ipynb             # Final BI-ready report aggregation
├── quick_analysis/
│   └── yellow_taxi_eda.ipynb                    # 3. Exploratory Data Analysis (EDA on gold data)

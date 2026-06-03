# NYC Taxi Data Pipeline & Analytics (H2 2025)

## 📌 Project Overview
This project is a hands-on data engineering pipeline that processes real-world NYC Yellow Taxi data from the second half of 2025 (July to December). Using **Apache Spark** and the **Medallion Architecture**, the pipeline takes raw, messy data and transforms it step-by-step into clean, business-ready tables.

The entire pipeline was built, debugged, and run within the free **Databricks Community Edition**, using **Unity Catalog** (`nyctaxi`) for data cataloging and schema isolation.

---

## 🛠️ Technology Stack
* **Platform:** Databricks Community Edition
* **Data Governance:** Unity Catalog (Catalog: `nyctaxi`)
* **Processing Engine:** Apache Spark (PySpark & Spark SQL)
* **Storage & Table Format:** Delta Lake & Parquet
* **Languages:** Python, SQL

---

## 📂 Repository Structure

```text
├── one_off/                                     # Setup & Environment Initialization
│   ├── creating_catalogs_schemas_volume.ipynb   # Creates Unity Catalog, schemas, and Volumes
│   ├── backfill_historical_yellow_trips.ipynb   # Creates monthly folder structures in Volume
│   └── create_folder_for_taxi_zone_lookup.ipynb # Creates storage folder for lookup data
├── transformations/                             # Core ETL Pipeline (Landing ➔ Gold)
│   ├── 01_bronze/
│   │   └── yellow_trips_raw.ipynb               # First ingestion layer + audit timestamps
│   ├── 02_silver/
│   │   ├── taxi_zone_lookup.ipynb               # Prepares location lookup data (SCD history tracking)
│   │   ├── yellow_trips_cleansed.ipynb          # Renames columns to snake_case & decodes numeric IDs
│   │   └── yellow_trips_enriched.ipynb          # Joins trips with zones + calculates trip duration
│   └── 03_gold/
│       └── daily_trip_summary.ipynb             # Aggregates daily stats for BI tools
├── quick_analysis/
│   └── yellow_taxi_eda.ipynb                    # Data insights & visualization

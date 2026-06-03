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
├── one_off/                                     # Setup and Initialization
│   ├── creating_catalogs_schemas_volume.ipynb   # Catalog, schemas, and Volume creation
│   ├── backfill_historical_yellow_trips.ipynb   # Creating directory structure for each month in Volume
│   └── create_folder_for_taxi_zone_lookup.ipynb # Creating directory for lookup Volume
├── transformations/                             # Core ETL Pipeline (Landing Parquet ➔ Delta Lake)
│   ├── 01_bronze/
│   │   └── yellow_trips_raw.ipynb               # Raw ingestion with processed_timestamp
│   ├── 02_silver/
│   │   ├── taxi_zone_lookup.ipynb               # Lookup standardization (SCD effective/end_date)
│   │   ├── yellow_trips_cleansed.ipynb          # Schema cleaning, snake_case renaming and decoding numeric IDs
│   │   └── yellow_trips_enriched.ipynb          # JOIN of trips and zones + duration calculation
│   └── 03_gold/
│       └── daily_trip_summary.ipynb             # Final BI-ready report aggregation
├── quick_analysis/
│   └── yellow_taxi_eda.ipynb                    # Exploratory Data Analysis (EDA on gold data)
```
## Pipeline & Transformations

### 1. landing Schema (Raw Storage)
* **nyctaxi_yellow:** Raw monthly partitioned Parquet files containing native taxi backend columns.
* **taxi_zone_lookup:** Static reference file mapping zone IDs to NYC Boroughs.

### 2. bronze Schema (Ingestion)
* **yellow_trips_raw:** Delta table preserving 100% original structural integrity (overwritten per batch/run), enriched with an administrative `processed_timestamp` audit column.
  
### 3. silver Schema (Cleaning & Enrichment)
* **yellow_trips_cleansed:** Standardized schema using `snake_case` notation. Applied data cleansing by mapping raw IDs to meaningful categories.
* **taxi_zone_lookup:** Enriches the static mapping table with `effective_date` and `end_date` for Slowly Changing Dimension (SCD) requirements.
* **yellow_trips_enriched:** Wide production table combining cleansed trips and lookup zones. Features new calculated column `trip_duration_mins`.

### 4. gold Schema (Business Aggregations)
* **daily_trip_summary:** Business-ready Delta table aggregated at the daily level (`pickup_date`) serving as a direct source for Power BI/Tableau reports (`total_trips`, `avg_distance_per_trip`, `total_revenue`, etc.).

---

## Exploratory Data Analysis (EDA) Highlights
The `yellow_taxi_eda.ipynb` notebook delivers actionable insights regarding:
* **Vendor Performance:** Revenue analysis across taxi operators.
* **Borough Popularity:** Top pickup and destination locations based on trip counts.
* **Trend Analysis:** Time Series analysis correlating daily trip volumes with total revenue to identify weekly seasonality.

---

## Attribution and Course Inspiration
This project is based on the data engineering curriculum and architecture designed by Malvik Vaghadia in the course "Azure Databricks and Spark SQL (Python)". While the core architectural framework (Medallion layers), database schemas, analytical assignment questions, and code logic were provided by the instructor, the hands-on setup, debugging, and execution within this repository were performed independently.

**My independent contributions and development workflow:**
1. **Hands-on Implementation:** Independently wrote the logic for data transformations and the Exploratory Data Analysis (EDA) based on the instructor's business questions, followed by self-correction and code optimization against the course reference solutions.
2. **New Dataset & Timeline:** Applied the entire methodology to a completely different and newer time frame (H2 2025), requiring separate data validation of late-2025 taxi records.
3. **Environment Adaptation:** Configured and optimized the execution of all notebooks to run properly within the strict resource and compute constraints of the free Databricks Community Edition utilizing Unity Catalog.

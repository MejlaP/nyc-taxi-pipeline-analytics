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
```
## ⚙️ Data Pipeline & Transformations

### 1. Landing Zone (Raw Storage)
* **nyctaxi_yellow:** Raw, untouched Parquet files split into monthly folders, exactly as they come from the backend database.
* **taxi_zone_lookup:** A static CSV file used to map numeric Zone IDs to real NYC Boroughs.

### 2. Bronze Layer (Ingestion)
* **yellow_trips_raw:** A Delta table that acts as a safety copy. It keeps 100% of the original data structure (overwritten on each run) and adds a `processed_timestamp` so we know exactly when the data entered our system.

### 3. Silver Layer (Cleaning & Enrichment)
* **yellow_trips_cleansed:** Data is cleaned up here. Columns are renamed to standard `snake_case`, invalid records are dropped, and raw numeric codes (like payment types) are decoded into human-readable text.
* **taxi_zone_lookup:** Enhances the static zone table by adding `effective_date` and `end_date` to handle any future changes in location data (SCD logic).
* **yellow_trips_enriched:** The main production table. It joins the cleansed taxi trips with the location lookup table and calculates a new column: `trip_duration_mins`.

### 4. Gold Layer (Business Reports)
* **daily_trip_summary:** A clean, aggregated Delta table optimized for BI tools like Power BI or Tableau. It groups data by `pickup_date` and provides clear business metrics like `total_trips`, `avg_distance_per_trip`, `total_revenue`, etc.

---

## 📊 Analytics & Insights (EDA Highlights)
The `yellow_taxi_eda.ipynb` notebook analyzes the final Gold data to answer core business questions:
* **Vendor Performance:** Which taxi operators generate the most revenue?
* **Borough Popularity:** Where do most pickups and drop-offs happen?
* **Trend Analysis:** A time-series look at daily trip counts and revenue to uncover weekly patterns and seasonality.

---

## 🤝 Course Inspiration & Credit
This project is based on the data engineering curriculum and architecture designed by **Malvik Vaghadia** in the course **"Azure Databricks and Spark SQL (Python)"**. 

While the general Medallion framework, database schemas, business questions, and core code logic come from the course curriculum, the hands-on setup, implementation, and execution were done independently.

**My development workflow and adaptations:**
1. **Active Learning & Implementation:** I wrote the transformation and analysis code myself based on the instructor's assignment goals, then self-corrected and optimized it using the course solutions.
2. **Fresh Dataset:** I applied the methodology to a completely different and newer time frame (**H2 2025**), handling data validation for this specific period.
3. **Environment Optimization:** I adjusted and configured the pipeline to run successfully within the strict memory and compute limits of the free Databricks Community Edition with Unity Catalog.

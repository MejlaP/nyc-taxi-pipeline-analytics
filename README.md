# NYC Taxi Data Pipeline & Analytics (H2 2025)

## 📌 Project Overview
This project is a hands-on data engineering pipeline that processes real-world NYC Yellow Taxi data from the second half of 2025 (July to December). Using Apache Spark and the Medallion Architecture, the pipeline takes raw, messy data and transforms it step-by-step into clean, business-ready tables.

The entire pipeline was built, debugged, and run within the free **Databricks Community Edition**, using **Unity Catalog** (`nyctaxi`) for data cataloging and schema isolation.

---
## Medallion Architecture Workflow
<img width="1645" height="1042" alt="diagram_final" src="https://github.com/user-attachments/assets/0823ab3d-7c83-4ec8-ad97-a87b535369ec" />

---

## ⚙️ Engineering Highlights
* **Incremental Processing & Orchestration:** Built a robust ETL pipeline designed for incremental batch processing. The workflow is orchestrated using Databricks Workflows (Jobs), ensuring consistent and automated updates to the Gold layer.
* **Historical Data Management (SCD Type 2):** Implemented SCD Type 2 logic for the taxi_zone_lookup table (Silver layer) to track historical changes in location names, maintaining a full audit trail.
* **Temporal Joins:** Fact-to-dimension joins are configured to respect the validity periods of location data, ensuring accurate record assignment even as business attributes change over time.
* **Environment Optimization:** Pipeline configured to run within the strict memory and compute limits of the Databricks Community Edition.

---

## 🛠️ Technology Stack
* **Platform:** Databricks Community Edition
* **Data Governance:** Unity Catalog (Catalog: `nyctaxi`)
* **Processing Engine:** Apache Spark (via PySpark API)
* **Storage & Table Format:** Delta Lake & Parquet
* **Languages:** Python

---

## 📂 Repository Structure
* **`one_off/`:** Notebooks for initial data ingestion and cleaning (backfill). These are used once for initial table initialization.
* **`transformations/`:** The core of the project, containing the incremental pipeline (Bronze → Silver → Gold). It implements SCD Type 2 logic and Temporal Joins to ensure data integrity and track historical changes.
* **`quick_analysis/`:** Notebooks designed for ad-hoc analysis, data quality checks, and generating initial insights (Data Exploration).

---

## ⚙️ Data Pipeline & Orchestration

> **Data Source (Landing Zone):** Raw Parquet files and static CSV lookups are stored within Databricks Volume storage.

### 1. Bronze Layer (Ingestion)
* **yellow_trips_raw (`01_bronze/`):** loads raw data into a Delta table, adding a `processed_timestamp` for auditability.

### 2. Silver Layer (Cleaning & Enrichment)
* **yellow_trips_cleansed (`02_silver/`):** Data is cleaned up here. Columns are renamed to standard `snake_case`, invalid records are dropped, and raw numeric codes (like payment types) are decoded into human-readable text.
* **taxi_zone_lookup (`02_silver/`):** Manages historical changes via SCD Type 2 (effective/end dates).
* **yellow_trips_enriched (`02_silver/`):** Executes Temporal Joins to merge trip facts with valid location dimensions.

### 3. Gold Layer (Business Reports)
* **daily_trip_summary (`03_gold/`):** provides aggregated business metrics optimized for BI tools.

### Orchestration
* **Production Pipeline:** Logic within `transformations/` is automated via Databricks Workflows, ensuring incremental updates.
* **Initialization:** Notebooks in `one_off/` are strictly separated for backfilling and are not part of the recurring production schedule.

---

## 📊 Analytics & Insights (EDA Highlights)
The `yellow_taxi_eda.ipynb` notebook analyzes the final Gold data to answer core business questions:
* **Vendor Performance:** Comparing revenue generation across different taxi operators to identify the highest and lowest performers.
* **Borough Popularity:** Where do most pickups and drop-offs happen?

---

## 🤝 Course Inspiration & Credit
This project is based on the data engineering curriculum and architecture designed by **Malvik Vaghadia** in the course **"Azure Databricks and Spark SQL (Python)"**. 

While the framework and core logic were inspired by the course, the implementation, setup, H2 2025 dataset adaptation, and incremental orchestration logic were developed independently to demonstrate modern data engineering practices.

**My development workflow and adaptations:**
1. **Active Learning & Implementation:** I wrote the transformation and analysis code myself based on the instructor's assignment goals, then self-corrected and optimized it using the course solutions.
2. **Fresh Dataset:** I applied the methodology to a completely different and newer time frame (**H2 2025**), handling data validation for this specific period.
3. **Environment Optimization:** I adjusted and configured the pipeline to run successfully within the strict memory and compute limits of the free Databricks Community Edition with Unity Catalog.

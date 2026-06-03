# NYC Taxi Data Pipeline & Analytics (H2 2025)

## Project Overview
This project implements a robust, scalable, end-to-end data pipeline processing real-world NYC Taxi (Yellow Cabs) data covering the second half of 2025 (July to December). The entire solution is engineered within Azure Databricks leveraging PySpark and the modern three-tier Delta Lake (Medallion Architecture).

Data governance and schema isolation are fully managed via Unity Catalog (Catalog: `nyctaxi`), ensuring a transparent data lineage from raw backend files to production-ready business aggregations.

## Technology Stack
* **Environment & Orchestration:** Azure Databricks (Community Edition)
* **Data Governance:** Unity Catalog (Catalog: `nyctaxi`)
* **Language & Engine:** Python, PySpark (Spark SQL & DataFrames)
* **Storage Format:** Delta Lake / Parquet
* **Architecture Visualization:** Mermaid.js

---

## Data Architecture & Schema Lineage (Medallion)

The pipeline processes data sequentially across four dedicated schemas within the `nyctaxi` catalog. The schema below outlines the exact table structures, key column transformations, and relationships:

```mermaid
graph TD
    subgraph Unity Catalog: nyctaxi
        subgraph Schema: landing
            A["nyctaxi_yellow (Parquet)<br>Raw Backend Columns:<br>• VendorID, tpep_pickup_datetime, tpep_dropoff_datetime<br>• passenger_count, trip_distance, RatecodeID<br>• store_and_fwd_flag, PULocationID, DOLocationID<br>• payment_type, fare_amount, extra, mta_tax, tip_amount<br>• tolls_amount, improvement_surcharge, total_amount<br>• congestion_surcharge, airport_fee, cbd_congestion_fee"]
            B["lookup / taxi_zone_lookup (Parquet)<br>Source Columns:<br>• LocationID, Borough, Zone, service_zone"]
        end

        subgraph Schema: bronze
            C["yellow_trips_raw (Delta)<br>Append-Only Ingestion:<br>• Retains all 20 raw columns<br>• processed_timestamp (Audit Column)"]
        end

        subgraph Schema: silver
            D["yellow_trips_cleansed (Delta)<br>Data Cleaning & Standardization:<br>• VendorID --> vendor<br>• RatecodeID --> rate_type<br>• PULocationID --> pu_location_id<br>• DOLocationID --> do_location_id<br>• payment_type --> payment_type<br>• Filtered out negative fares & invalid distances"]
            E["taxi_zone_lookup (Delta)<br>Dimensional Extension (SCD):<br>• LocationID, Borough, Zone, service_zone<br>• effective_date<br>• end_date"]
            F["yellow_trips_enriched (Delta)<br>Denormalized Production Table:<br>• vendor, timestamps, passenger_count, trip_distance, rate_type<br>• trip_duration_mins (datediff from pickup/dropoff)<br>• pu_borough, do_borough (JOIN via LocationID)<br>• pu_zone, do_zone (JOIN via LocationID)<br>• All standardized financial components & processed_timestamp"]
        end

        subgraph Schema: gold
            G["daily_trip_summary (Delta)<br>Aggregated Business KPIs:<br>• pickup_date (Granularity Key)<br>• total_trips<br>• avg_passengers_per_trip<br>• avg_distance_per_trip<br>• avg_fare_per_trip<br>• max_fare, min_fare<br>• total_revenue"]
        end
    end

    subgraph Analytics Layer
        H["yellow_taxi_eda.ipynb<br>Exploratory Data Analysis:<br>• Vendor Revenue Performance<br>• Top Pickup Boroughs & Journeys<br>• Revenue vs. Trip Count Time Series"]
    end

    A -->|Raw Ingestion| C
    C -->|Schema Enforcement & Rename| D
    B -->

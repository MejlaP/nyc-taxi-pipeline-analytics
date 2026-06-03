# NYC Taxi Data Pipeline and Analytics (H2 2025)

## Project Overview
This project implements a robust, scalable, end-to-end data pipeline processing real-world NYC Taxi (Yellow Cabs) data covering the second half of 2025 (July to December). The entire solution is engineered within Azure Databricks leveraging PySpark and the modern three-tier Delta Lake (Medallion Architecture).

Data governance and schema isolation are fully managed via Unity Catalog (Catalog: `nyctaxi`), ensuring a transparent data lineage from raw backend files to production-ready business aggregations.

## Technology Stack
* **Environment and Orchestration:** Azure Databricks (Community Edition)
* **Data Governance:** Unity Catalog (Catalog: `nyctaxi`)
* **Language and Engine:** Python, PySpark (Spark SQL and DataFrames)
* **Storage Format:** Delta Lake / Parquet
* **Architecture Visualization:** Mermaid.js

---

## Data Architecture and Schema Lineage (Medallion)

The pipeline processes data sequentially across four dedicated schemas within the `nyctaxi` catalog. The schema below outlines the exact table structures, key column transformations, and relationships:

```mermaid
graph TD
    subgraph Unity Catalog: nyctaxi
        subgraph Schema: landing
            A["nyctaxi_yellow (Parquet)<br>Raw Backend Columns:<br>VendorID, tpep_pickup_datetime, tpep_dropoff_datetime,<br>passenger_count, trip_distance, RatecodeID,<br>store_and_fwd_flag, PULocationID, DOLocationID,<br>payment_type, fare_amount, extra, mta_tax,<br>tip_amount, tolls_amount, improvement_surcharge,<br>total_amount, congestion_surcharge,<br>airport_fee, cbd_congestion_fee"]
            B["lookup / taxi_zone_lookup (Parquet)<br>Source Columns:<br>LocationID, Borough, Zone, service_zone"]
        end

        subgraph Schema: bronze
            C["yellow_trips_raw (Delta)<br>Append-Only Ingestion:<br>All 20 raw columns from landing schema,<br>processed_timestamp"]
        end

        subgraph Schema: silver
            D["yellow_trips_cleansed (Delta)<br>Data Cleaning and Standardization:<br>vendor, tpep_pickup_datetime, tpep_dropoff_datetime,<br>passenger_count, trip_distance, rate_type,<br>store_and_fwd_flag, pu_location_id, do_location_id,<br>payment_type, fare_amount, extra, mta_tax,<br>tip_amount, tolls_amount, improvement_surcharge,<br>total_amount, congestion_surcharge,<br>airport_fee, cbd_congestion_fee, processed_timestamp"]
            E["taxi_zone_lookup (Delta)<br>Dimensional Extension (SCD):<br>LocationID, Borough, Zone, service_zone,<br>effective_date, end_date"]
            F["yellow_trips_enriched (Delta)<br>Denormalized Production Table:<br>vendor, tpep_pickup_datetime, tpep_dropoff_datetime,<br>trip_duration_mins, passenger_count, trip_distance,<br>rate_type, store_and_fwd_flag, pu_borough,<br>do_borough, pu_zone, do_zone, payment_type,<br>fare_amount, extra, mta_tax, tip_amount,<br>tolls_amount, improvement_surcharge, total_amount,<br>congestion_surcharge, airport_fee,<br>cbd_congestion_fee, processed_timestamp"]
        end

        subgraph Schema: gold
            G["daily_trip_summary (Delta)<br>Aggregated Business KPIs:<br>pickup_date, total_trips, avg_passengers_per_trip,<br>avg_distance_per_trip, avg_fare_per_trip,<br>max_fare, min_fare, total_revenue"]
        end
    end

    subgraph Analytics Layer
        H["yellow_taxi_eda.ipynb<br>Exploratory Data Analysis:<br>Vendor Revenue Performance,<br>Top Pickup Boroughs and Journeys,<br>Revenue vs. Trip Count Time Series"]
    end

    A -->|Raw Ingestion| C
    C -->|Schema Enforcement and Rename| D
    B -->|SCD Tracking Setup| E
    D -->|JOIN via pu or do location id| F
    E -->|JOIN via LocationID| F
    F -->|Business Aggregations| G
    F -.->|Ad-hoc Source Data| H

    style A fill:#eceff1,stroke:#333,stroke-width:1px
    style B fill:#eceff1,stroke:#333,stroke-width:1px
    style C fill:#bbf,stroke:#333,stroke-width:2px
    style D fill:#bfb,stroke:#333,stroke-width:2px
    style E fill:#bfb,stroke:#333,stroke-width:2px
    style F fill:#bfb,stroke:#333,stroke-width:2px
    style G fill:#fbf,stroke:#333,stroke-width:2px
    style H fill:#ffe0b2,stroke:#333,stroke-width:1px

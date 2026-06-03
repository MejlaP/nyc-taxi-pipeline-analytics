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

The pipeline processes data sequentially across four dedicated schemas within the `nyctaxi` catalog. The diagram below outlines the clean flow of data across the Medallion layers:

```mermaid
graph TD
    subgraph Unity Catalog: nyctaxi
        subgraph Schema: landing
            A[nyctaxi_yellow]
            B[taxi_zone_lookup]
        end

        subgraph Schema: bronze
            C[yellow_trips_raw]
        end

        subgraph Schema: silver
            D[yellow_trips_cleansed]
            E[taxi_zone_lookup_scd]
            F[yellow_trips_enriched]
        end

        subgraph Schema: gold
            G[daily_trip_summary]
        end
    end

    subgraph Analytics Layer
        H[yellow_taxi_eda.ipynb]
    end

    A --> C
    C --> D
    B --> E
    D --> F
    E --> F
    F --> G
    F -.-> H

    style A fill:#eceff1,stroke:#333,stroke-width:1px
    style B fill:#eceff1,stroke:#333,stroke-width:1px
    style C fill:#bbf,stroke:#333,stroke-width:2px
    style D fill:#bfb,stroke:#333,stroke-width:2px
    style E fill:#bfb,stroke:#333,stroke-width:2px
    style F fill:#bfb,stroke:#333,stroke-width:2px
    style G fill:#fbf,stroke:#333,stroke-width:2px
    style H fill:#ffe0b2,stroke:#333,stroke-width:1px

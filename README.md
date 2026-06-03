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

# NYC Taxi Data Pipeline & Analytics (H2 2025)

## 📌 O projektu
Tento projekt implementuje robustní a škálovatelnou end-to-end datovou pipeline nad reálným datasetem **NYC Taxi (Yellow Cabs)** za uzavřené období druhého půlroku 2025 (červenec–prosinec). Celé řešení je postaveno v prostředí **Azure Databricks** s využitím frameworku **PySpark** a moderní třívrstvé architektury **Delta Lake (Medallion Architecture)**.

Projekt je kompletně řízen přes **Unity Catalog** (`nyctaxi`), což zajišťuje jasnou správu dat, oddělení schémat a transparentní datovou lineage od surových souborů až po finální agregace.

## 🛠️ Technologický stack
* **Prostředí & Orchestrace:** Azure Databricks (Community Edition)
* **Správa dat (Governance):** Unity Catalog (Katalog: `nyctaxi`)
* **Jazyk & Engine:** Python, PySpark (Spark SQL & DataFrames)
* **Formát úložiště:** Delta Lake / Parquet
* **Vizualizace architektury:** Mermaid.js

---

## 📐 Datová architektura & Schémata (Medallion)

Pipeline zpracovává data sekvenčně skrz čtyři dedikovaná schémata v katalogu `nyctaxi`. Propojení a transformace dat ilustruje následující diagram:

```mermaid
graph TD
    subgraph Unity Catalog: nyctaxi
        subgraph Schema: landing
            A[nyctaxi_yellow<br>Měsíční Parquet soubory<br>H2 2025]
            B[lookup / taxi_zone_lookup<br>Parquet]
        end

        subgraph Schema: bronze
            C[(yellow_trips_raw)]
        end

        subgraph Schema: silver
            D[(yellow_trips_cleansed)]
            E[(taxi_zone_lookup)]
            F[(yellow_trips_enriched)]
        end

        subgraph Schema: gold
            G[(daily_trip_summary)]
        end
    end

    subgraph Analytická vrstva
        H[yellow_taxi_eda.ipynb<br>Exploratory Analysis]
    end

    A -->|Iniciální load + processed_timestamp| C
    C -->|Přejmenování sloupců & Typování| D
    B -->|Doplnění efektivního rozsahu dat| E
    D -->|JOIN přes Location ID| F
    E -->|JOIN přes Location ID| F
    F -->|Agregace a byznys metriky| G
    F -.->|Zdroj pro rychlou analýzu| H

    style A fill:#eceff1,stroke:#333,stroke-width:1px
    style B fill:#eceff1,stroke:#333,stroke-width:1px
    style C fill:#bbf,stroke:#333,stroke-width:2px
    style D fill:#bfb,stroke:#333,stroke-width:2px
    style E fill:#bfb,stroke:#333,stroke-width:2px
    style F fill:#bfb,stroke:#333,stroke-width:2px
    style G fill:#fbf,stroke:#333,stroke-width:2px
    style H fill:#ffe0b2,stroke:#333,stroke-width:1px

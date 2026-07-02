# Databricks notebook source
# Creating catalog
spark.sql("create catalog if not exists nyctaxi")

# COMMAND ----------

# Creating schemas
spark.sql("create schema if not exists nyctaxi.00_landing")
spark.sql("create schema if not exists nyctaxi.01_bronze")
spark.sql("create schema if not exists nyctaxi.02_silver")
spark.sql("create schema if not exists nyctaxi.03_gold")

# COMMAND ----------

# Creating volumes
spark.sql("create volume if not exists nyctaxi.00_landing.data_sources")
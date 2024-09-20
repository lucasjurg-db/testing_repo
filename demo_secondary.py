# Databricks notebook source
from lucas_library import search_for_lucas

search_for_lucas("titanic_data.csv")

# COMMAND ----------

with open("demo.py", "r") as f:
  for line in f:
    if "pandas" in line:
      print("found pandas in demo.py")
      print(line)

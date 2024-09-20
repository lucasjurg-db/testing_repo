# Databricks notebook source
from finding_library import search_for_word

search_for_word("titanic_data.csv", "Johnson") # Williams

# COMMAND ----------

with open("demo.py", "r") as f:
  for line in f:
    if "pandas" in line:
      print(f"found pandas in demo.py - {line}")


# COMMAND ----------

with open("demo_copy.py", "w") as out:
  with open("demo.py", "r") as infile:
    for line in infile:
      out.write(line)

# COMMAND ----------

import os
os.remove("demo_copy.py")

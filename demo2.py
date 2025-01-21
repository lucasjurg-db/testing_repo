# Databricks notebook source
from finding_library import search_for_word

search_for_word("titanic_data.csv", "Johnson") # Williams Mark

# COMMAND ----------

with open("demo_copy.py", "w") as out:
  with open("demo.py", "r") as infile:
    for line in infile:
      out.write(line)

# COMMAND ----------

# MAGIC %sh
# MAGIC echo "
# MAGIC # COMMAND ----------
# MAGIC
# MAGIC import os
# MAGIC os.remove(\"demo_copy.py\")
# MAGIC " >> demo.py
# MAGIC
# MAGIC # With changes 2

# COMMAND ----------

print("new command")

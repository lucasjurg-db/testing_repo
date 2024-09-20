# Databricks notebook source
import pandas as pd
import os

titanic_data_url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

titanic_df = pd.read_csv(titanic_data_url)

titanic_df.to_csv("titanic_data.csv")

# COMMAND ----------

def search_for_lucas(file_name):
  with open(file_name, "r") as f:
    for line in f:
      if "Lucas" in line:
        print("Found Lucas in " + file_name)

search_for_lucas("titanic_data.csv")

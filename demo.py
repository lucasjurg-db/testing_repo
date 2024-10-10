# Databricks notebook source
import pandas as pd
import os

titanic_data_url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(titanic_data_url)
titanic_df.to_csv("titanic_data.csv")

# COMMAND ----------

def search_for_word(file_name, word):
  with open(file_name, "r") as f:
    for line_num, line in enumerate(f):
      if word in line:
        print(f"Found '{word}' on line: {line_num+1} of file: '{file_name}'")

search_for_word("titanic_data.csv", "Johnson")


# With some new code

# Databricks notebook source
# MAGIC %md
# MAGIC Testing

# COMMAND ----------

# DBTITLE 1,Exploring Databricks Log Files with Bash
# MAGIC %sh
# MAGIC ls
# MAGIC # # cat /databricks/data/logs/wsfs.log
# MAGIC # echo "Hello" > jurgensen_test_file_new
# MAGIC # with some new stuff again
# MAGIC # and again some new stuff
# MAGIC

# COMMAND ----------

# MAGIC %sh
# MAGIC echo "#Databricks notebook source" > notebook.ipynb

# COMMAND ----------

# MAGIC %sh
# MAGIC echo "" > /databricks/data/logs/wsfs.log

# COMMAND ----------

# MAGIC %sh
# MAGIC cat /databricks/runtime/info.json
# MAGIC cat /databricks/data/logs/wsfs.log

# COMMAND ----------

# MAGIC %sh
# MAGIC cat /databricks/common/conf/deploy.conf
# MAGIC

# COMMAND ----------

import os

print(os.getcwd())

results = []
file_path = 'test1'
for _ in range(10):
  os.mkdir("test1")
  os.rmdir("test1")


# COMMAND ----------

# with open("filex00.py", "w") as f:
#   f.write("print('Hello World Again')")

# Another comment again
import os

# file_path = '/Workspace/lucas'
# file_status = os.stat(file_path)
# print(file_status)

# COMMAND ----------

# MAGIC %sh
# MAGIC
# MAGIC strace echo "" > tests_file_3
# MAGIC

# COMMAND ----------

# MAGIC %sh
# MAGIC strace touch test_file_3

# COMMAND ----------

# MAGIC %sh
# MAGIC touch /tmp/file.txt
# MAGIC echo "PWD"
# MAGIC pwd
# MAGIC ls -lah tmp 
# MAGIC cd /tmp
# MAGIC

# COMMAND ----------

# DBTITLE 1,Current Directory Command
# MAGIC %sh
# MAGIC
# MAGIC pwd
# MAGIC
# MAGIC cd /Workspace/Users/lucas.jurgensen@databricks.com/guff
# MAGIC pwd
# MAGIC ls -lah
# MAGIC
# MAGIC # cat basic_notebook
# MAGIC
# MAGIC echo "WSFS_NOTEBOOK_READS_ENABLED = $WSFS_NOTEBOOK_READS_ENABLED"
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# DBTITLE 1,Precision Pi Substring Display
import demo_library
y = demo_library.demo(2)
y.print_x()

# COMMAND ----------

# MAGIC %md
# MAGIC HEre's some text

# COMMAND ----------

# DBTITLE 1,Python Demo Printer Function
class demo():
  def printer(self):
    print("Hello World")

x = demo()

x.printer()

# COMMAND ----------

# DBTITLE 1,Python Printer Invocation
x.printer()

# COMMAND ----------

# DBTITLE 1,Databricks Model Scoring Utility
import os
import requests
import numpy as np
import pandas as pd
import json

DATABRICKS_TOKEN = 'dapid920ff90c33c692e98e93a1338b0a75a'

def create_tf_serving_json(data):
    if isinstance(data, pd.DataFrame):
        # Convert DataFrame to split dictionary format while preserving the index
        return {'inputs': data.to_dict(orient='split')}
    elif isinstance(data, dict):
        # Assuming the dictionary is structured with column names as keys and lists of values as values
        df = pd.DataFrame.from_dict(data)
        return {'inputs': df.to_dict(orient='split')}
    else:
        # Handle other data formats as needed
        return {'inputs': data}


def score_model(dataset):
    if not isinstance(dataset, pd.DataFrame):
        raise Exception("Dataset should be a DataFrame")

    url = 'https://e2-dogfood.staging.cloud.databricks.com/serving-endpoints/jurgensen_EV_v10/invocations'
    headers = {'Authorization': f'Bearer {DATABRICKS_TOKEN}', 'Content-Type': 'application/json'}

    # Convert DataFrame to the expected JSON format
    data_json = json.dumps({'inputs': dataset.to_dict(orient='split')}, allow_nan=True)

    response = requests.post(url, headers=headers, data=data_json)
    if response.status_code != 200:
        raise Exception(f'Request failed with status {response.status_code}, {response.text}')

    return response.json()

# Define your data and column names
data = [
    "5YJYGDEE1L", "King", "Seattle", "WA", "98122", 2020, "TESLA", "MODEL Y", "Clean Alternative Fuel Vehicle Eligible", 291, 0, 37, 125701579, "POINT (-122.30839 47.610365)", "CITY OF SEATTLE - (WA)|CITY OF TACOMA - (WA)", "53033007800"
]
columns = ["VIN (1-10)", "County", "City", "State", "Postal Code", "Model Year", "Make", "Model", "Clean Alternative Fuel Vehicle (CAFV) Eligibility", "Electric Range", "Base MSRP", "Legislative District", "DOL Vehicle ID", "Vehicle Location", "Electric Utility", "2020 Census Tract"]

# Create a DataFrame
df = pd.DataFrame(data, columns=columns)

# Score the model using the DataFrame directly
score_result = score_model(df)

# COMMAND ----------

# MAGIC %sh
# MAGIC grep "sparkVersion" /databricks/common/conf/deploy.conf
# MAGIC grep "sparkImageLabel" /databricks/common/conf/deploy.conf
# MAGIC

# COMMAND ----------

# MAGIC %sh
# MAGIC cat nb
# MAGIC

# COMMAND ----------

# MAGIC %sh
# MAGIC cat /Workspace/.proc/self/token

# COMMAND ----------

# MAGIC %sh
# MAGIC cat notebook.py

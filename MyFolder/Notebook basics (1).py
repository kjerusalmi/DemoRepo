# Databricks notebook source
print("hello wolrd")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "Hello_wolrd FROM SQL"

# COMMAND ----------

# MAGIC %md
# MAGIC Hello world
# MAGIC # title

# COMMAND ----------

# MAGIC %run Setup

# COMMAND ----------

full_name

# COMMAND ----------

# MAGIC %fs ls databricks-datasets

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('databricks-datasets')
files

# COMMAND ----------

display(files)

# COMMAND ----------



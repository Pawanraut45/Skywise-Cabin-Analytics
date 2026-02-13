from pyspark.sql import SparkSession
from pyspark.sql.functions import col


spark = SparkSession.builder.appName("CabinAnalytics").getOrCreate()


df = spark.read.csv("data/raw/cabin_maintenance_raw.csv", header=True, inferSchema=True)


clean_df = df.filter(col("aircraft_id").isNotNull())


clean_df.write.mode("overwrite").parquet("data/processed/cabin_maintenance_clean.parquet")
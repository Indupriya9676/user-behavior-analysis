from pyspark.sql import SparkSession
from pyspark.sql.functions import split, col

spark = SparkSession.builder.appName("WebLogETL").getOrCreate()

# Read web logs
logs = spark.read.text("data/weblogs.csv")

# Parse logs: assume CSV format with timestamp, user_id, page
logs_df = logs.selectExpr("split(value, ',') as fields")               .select(
                  col("fields")[0].alias("timestamp"),
                  col("fields")[1].alias("user_id"),
                  col("fields")[2].alias("page")
              )

logs_df.write.mode("overwrite").csv("data/cleaned_logs")

spark.stop()

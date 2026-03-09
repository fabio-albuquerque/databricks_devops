from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

print('test1')
df = spark.sql("select 1")
print(df.toPandas())
print('test2')


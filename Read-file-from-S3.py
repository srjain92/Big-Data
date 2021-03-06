from pyspark.sql import SparkSession
from pyspark.sql import Row
import os

os.environ['PYSPARK_SUBMIT_ARGS'] = "--packages=org.apache.hadoop:hadoop-aws:2.7.3 pyspark-shell"

# Create a SparkSession (Note, the config section is only for Windows!)
spark = SparkSession.builder.config("spark.sql.warehouse.dir", "file:///C:/temp").appName("SparkSQL").getOrCreate()

spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.access.key", "Insert Access Key")
spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.secret.key", "Insert Secret Key")
spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "s3.amazonaws.com")

df = spark.read.csv("s3a://sj-databricks/Amazon.csv")
df.show()
print("Done")

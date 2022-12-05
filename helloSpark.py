from lib.logger import Log4j
from pyspark.sql import *
from lib.logger import Log4j


if __name__ == '__main__':
    spark = SparkSession.builder \
            .appName("HelloSpark") \
            .master("local[4]") \
            .getOrCreate()

    logger = Log4j(spark)
    
    logger.info("Started the Spark Session From Here")

    logger.info("===="*20)
    print("HELLO WORLD")
    logger.info("===="*20)
    logger.info("Finished greetings......")

    spark.stop()
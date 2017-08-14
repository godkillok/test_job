import os
import sys

os.environ['SPARK_HOME'] = "/usr/lib/spark/spark-2.1.1-bin-hadoop2.7"
sys.path.append("/usr/lib/spark/spark-2.1.1-bin-hadoop2.7/python")

try:

    from pyspark import SparkContext, SparkConf
    from pyspark.sql import SQLContext

    sc = SparkContext("local", "Simple App")

    sqlContext = SQLContext(sc)

    # A JSON dataset is pointed to by path.
    # The path can be either a single text file or a directory storing text files.
    people = sqlContext.read.json("/usr/lib/spark/spark-2.1.1-bin-hadoop2.7/examples/src/main/resources/people.json")

    # The inferred schema can be visualized using the printSchema() method.
    people.printSchema()

    people.registerTempTable("people")

    # SQL statements can be run by using the sql methods provided by `sqlContext`.
    teenagers = sqlContext.sql("SELECT name FROM people")
    teenagers.show()
    ad=teenagers.collect()
    print(ad)



    anotherPeopleRDD = sc.parallelize([
        '{"name":"Yin","address":{"city":"Columbus","state":"Ohio"}}'])
    anotherPeople = sqlContext.jsonRDD(anotherPeopleRDD)

    from pyspark.sql import SQLContext

    # create_engine('postgresql://postgres:123456@localhost/pipeline')
    df = sqlContext.load(source="jdbc", url="jdbc:postgresql://localhost/postgres", dbtable="[public.user_tbl]")



    print("Successfully imported Spark Modules")
except ImportError as e:
    print("Can not import Spark Modules", e)
    sys.exit(1)


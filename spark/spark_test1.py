from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
import os

os.environ["SPARK_HOME"] = "/home/tom/spark/"
os.environ["PYSPARK_PYTHON"] = "/usr/bin/python3.5"
conf = SparkConf().setAppName('app_test').setMaster('local')
sc = SparkContext(conf=conf)
ss=SparkSession(sc)


class ml_100k():
    @classmethod
    def read(self):
        textFile = sc.textFile("/home/tom/github_folder/test_job/ml-100k/u.user")
        textFile2=textFile.collect()
        textFiles=textFile.map(lambda line: line.split('|')).map(lambda x:(int(x[0]),int(x[1]),x[2],x[3],int(x[4] if x[4].isdigit() else 0)))
        #rdd to DataFrame
        df=ss.createDataFrame(textFiles).toDF('user_id', 'age','gender','occupation','zip_code')
        df.createOrReplaceTempView("people")
        df.show()
        df.select(df['user_id'], df['age'] + 1).show()
        textFiles.first()
        sqlDF = ss.sql("SELECT count(user_id),occupation FROM people GROUP by occupation")
        sqlDF.show()
        # sc.createDataFrame(textFiles, ["id", "score"])
        age=textFiles.map(lambda x:(x[1],1))
        age.first()
        ge=age.reduceByKey(lambda x,y:x+y).collect()
        userid=[int(v[0]) for v in textFiles.take(10)]
        gge=textFiles.collect()
        print(textFile.first())
        rdd = sc.parallelize([1, 1, 2, 3, 5, 8])
        result = rdd.groupBy(lambda x: x % 2).collect()

    @classmethod
    def ml(self):
        from pyspark.ml.linalg import Vectors
        from pyspark.ml.stat import Correlation

        data = [(Vectors.sparse(4, [(0, 1.0), (3, -2.0)]),),
                (Vectors.dense([4.0, 5.0, 0.0, 3.0]),),
                (Vectors.dense([6.0, 7.0, 0.0, 8.0]),),
                (Vectors.sparse(4, [(0, 9.0), (3, 1.0)]),)]
        df = ss.createDataFrame(data, ["features"])
        df.show()

        r1 = Correlation.corr(df, "features").head()
        print("Pearson correlation matrix:\n" + str(r1[0]))

        r2 = Correlation.corr(df, "features", "spearman").head()
        print("Spearman correlation matrix:\n" + str(r2[0]))

if __name__ == '__main__':
    # ml_100k.read()
    ml_100k.ml()



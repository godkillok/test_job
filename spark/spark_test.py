from pyspark import SparkContext
from pyspark import SparkContext, SparkConf
import os

os.environ["SPARK_HOME"] = "/home/tom/spark/"
os.environ["PYSPARK_PYTHON"]="/usr/bin/python3.5"


conf = SparkConf().setAppName('app_test').setMaster('local')
sc = SparkContext(conf=conf)

textFile = sc.textFile("/home/tom/github_folder/test_job/spark/README.md")
a=textFile.count()
textFile.first()
len2=textFile.filter(lambda x:"spark" in x)
b=len2.take(10)
oo=len2.collect()
len45=textFile.map(lambda x:len(x)).reduce(lambda a,b:a if a>b else b)
# gg=len44.count()
# gg=len44.collect()
print(len45)

# 2.更多的RDD操作
print(textFile.map(lambda line: len(line.split())).reduce(lambda a, b: a if (a > b) else b))  # 我们希望找到含有最后单词的一句话：
''' 这个语句中，map函数将len(line.split())这一语句在所有line上执行，
返回每个line所含有的单词个数，也就是将line都map到一个整数值，
 然后创建一个新的RDD。然后调用reduce，找到最大值。
 map和reduce函数里的参数是python中的匿名函数（lambda）
 ，事实上，我们这里也可以传递python中 更顶层的函数
 。比如，我们先定义一个比较大小的函数，这样我们的代码会更容易理解： '''


def max(a, b):
    if a > b:
        return a
    else:
        return b


print(textFile.map(lambda line: len(line.split())).reduce(max))
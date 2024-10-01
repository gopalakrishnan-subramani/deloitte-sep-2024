from pyspark import SparkContext
sc = SparkContext("local", "SparkBasic")

rdd = sc.parallelize([0,1,2,3,4,5,6,7,8,9])

oddRdd = rdd.filter (lambda n: n % 2 == 1)

results = oddRdd.collect()
print(results)

sc.version

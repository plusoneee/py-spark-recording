from pyspark import SparkContext

logFile = "./README.md"
sc = SparkContext("local", "world-count-App")
logData = sc.textFile(logFile).cache()

flat_str = logData.flatMap(lambda line: line.split(" "))

print("------flat------")
print(flat_str.collect())
map_str = flat_str.map(lambda w: (w,1))
print("------map-------")
print(map_str.collect())
counts = map_str.reduceByKey(lambda x,y: x+y )
print("------reduce------")
print(counts.collect())



### 上傳檔案到 HDFS
Spark API Example 採用以下測試資料來完成操作，可以透過 vim 或 nano 新增：
```txt
$ vim test.txt
# test data
a,123,456,789,11344,2142,123
b,1234,124,1234,123,123
c,123,4123,5435,1231,5345
d,123,456,789,113,2142,143
e,123,446,789,14,2142,113
f,123,446,789,14,2142,1113,323
```
新增完成後，上傳至 HDFS 或者 OpenStack Swift 上，以下為 HDFS 範例：
```sh
$ hadoop fs -mkdir -p /spark/hw
$ hadoop fs -put test.txt /spark/hw
```


### Map 練習：
* spark-hw01-map.py
找出測試資料所有的英文字母，結果如下：
```
a
b
c
d
e
f
```

### FlatMap 練習：
* spark-hw02-flatmap.py
找出測試資料所有以","切割的資料
結果如下：
```
a
123
456
789
11344
2142
123
…
```

### filter 練習:
* spark-hw03-filter.py
找出測試資料所有以123與456的資料，結果如下：
```
123
456
123
1234
1234
…
```

### reduce練習:
* spark-hw04-reduce.py
找出測試資料所有英文字母,並用reduce將之append成一個字串，結果如下：
```
abcdef
```

### reduceByKey練習:
* spark-hw05-reduceByKey.py
找出測試資料所有英文字母,並用reduce將之append成一個字串，結果如下：
```
(d,1)
(1113,1)
(1231,1)
(e,1)
(14,2)
(113,2)
…
```

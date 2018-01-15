# [Day17]Numpy的數學&統計方法！

嗨，今天才第17天，
下禮拜期末考了所以非常煎熬（冒煙），突然覺得走了1/2之後開始有點累了（汗）
那今天來說說numpy中統計函數的方法。

其他天Numpy的文章：
* [[Day14]Numpy的ndarray！](https://ithelp.ithome.com.tw/articles/10195434)
* [[Day 15]Numpy操作索引＆局部資料！](https://ithelp.ithome.com.tw/articles/10195645)
* [[Day16]Numpy的廣播&方法！](https://ithelp.ithome.com.tw/articles/10195830)
* [[Day18]Numpy檔案輸入與輸出！](https://ithelp.ithome.com.tw/articles/10196167)

首先先import numpy
```python
import numpy as np
```
# Random Data
## random.randn()
`random.randn()`用來隨機建立資料：
```python
np.random.randn()
```

上面這個可以隨機得到一個數字，可能是負的或正的，可能大於一或小於一，總之就是`隨機`。
![Imgur](https://i.imgur.com/FIvxuED.png)

還可以怎麼用呢？
```python
np.random.randn(2, 4) + 1.920929
```
上面這裡建立一了一個`2 X 4`的矩陣，並且隨機給它數值，最後將它加上1.920929這個數子：
![Imgur](https://i.imgur.com/LXTAtUO.png)

OK！這就是`random.randn()`

## .random.randint()
接下來要說明的跟上一個有一點點不同，是`.randint()`
> (low, high=None, size=None, dtype='l')

直接來試試看就知道啦：
```python
np.random.randint(4, size=10)
```
產生`>4的整數`，大小為10，如圖：
![Imgur](https://i.imgur.com/BQwBEbV.png)

當然它有參數(low, high,size)可以自己設定範圍：
```python
np.random.randint(low=4,high=10,size=10)
```
像上面這樣就會產生大小為10，從4到小於10（9）的整數
![Imgur](https://i.imgur.com/7y89yQB.png)

# Methods
可以隨機產生資料之後，就拿產生的資料來做數學運算吧！
其實在pandas裡面也就有數學方法可以使用了哦，不過還是來看看Numpy的部分吧！

## .mean()
建立一個`5 X 4`的隨機資料，並取`平均值`：
```python
x = np.random.randn(5, 4)
x.mean()
```
分開做會比較清楚：
![Imgur](https://i.imgur.com/AnEIgbp.png)

## .sum()
建立一個`5 X 4`的隨機資料，並取`總和`：
```python
x = np.random.randn(5, 4)
x.sum()
```
![Imgur](https://i.imgur.com/XLDUAKC.png)

## .min()&.max()
建立一個`5 X 4`的隨機資料，並取`最大`跟`最小`值。
```python
xmin = np.random.randn(5, 4)
xmin.min()
```

```python
xmax = np.random.randn(5, 4)
xmax.min()
```
![Imgur](https://i.imgur.com/jN4H90I.png)

## .cumsum()
這個比較特別，會回傳累積的數值：
```python
x = np.array([[2,3,4], [5,6,7]])
np.cumsum(x)
```
會輸出：
```python
array([ 2,  5,  9, 14, 20, 27])
```
第一個index為2 = 2
第二個index為2+3 = 5
第三個index為2+3+4 = 9
第四個index為2+3+4+5 = 14
以此類推 。

## .std()
接下來這個是`標準差`，統計領域的一定非常熟悉！

> std = sqrt(mean(abs(x - x.mean())\**2))

上面為標準差公式，但用`std()`就可以快速的算出來啦：
```python
x = np.array([[1, 2], [3, 4]])
np.std(x)
```
![Imgur](https://i.imgur.com/g7z2zmT.png)


參考資料：
[numpy.random.randn](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.random.randn.html)
[numpy.cumsum](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.cumsum.html)



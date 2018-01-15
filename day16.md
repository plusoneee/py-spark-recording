
# [Day16]Numpy的廣播&方法！

嗨，今天來到鐵人的16天了，今天要說明一下在Numpy中很好用的廣播功能與會用到的函數。

若是想看其他Numpy的介紹：
* [[Day14]Numpy的ndarray！](https://ithelp.ithome.com.tw/articles/10195434)
* [[Day 15]Numpy操作索引＆局部資料！](https://ithelp.ithome.com.tw/articles/10195645)
* [[Day17]Numpy的數學&統計方法！](https://ithelp.ithome.com.tw/articles/10195984)
* [[Day18]Numpy檔案輸入與輸出！](https://ithelp.ithome.com.tw/articles/10196167)

# Broadcasting
首先！一定要先 `import numpy` ！
```python
import numpy as np
```

我們在之前提過如何產生（宣告）ndarray：
```python
a = np.array([1,2,3])
b = np.array([2,2,2])
```

現在我們要將`a`和`b`相乘：
```python
a * b
```
會得到：
```python
array([2, 4, 6])
```
這是沒有問題的。

### 那什麼叫做廣播呢？

> NumPy is smart enough to use the original scalar value without actually making copies, so that broadcasting operations are as memory and computationally efficient as possible

廣播的使用原來的向量而不需要實際的複製，所以它可以有效的運用記憶體和運算，不懂的話直接來試試看下面的範例：
```python
c = np.array([1.0, 2.0, 3.0])
d = 2
c * d
```
上面這個一樣會得到 `array([ 2.,  4.,  6.])`，這就是所謂的廣播！
相當於`d`也是一個array，可以想像是Numpy會把`d`給放大變成和`c`一樣的大小（shape），而不需要自己去複製和`c`一樣多個2。
這樣對廣播有概念了吧！

再來進階一點，這邊可能需要一點`線性代數`的概念：

```python
x = np.arange(4)
```
上面這邊建立一個了一個 `x = [0,1,2,3]`
```python
x2 = x.reshape(4,1)
```
我們用`.reshape()`將`x`的矩陣形狀改成`4 X 1`
```python
y = np.ones(5)
```
接著建立一個`y = [1,2,3,4,5]`

接著將`xx`和`y`相加：
```python
xx + y
```
![Imgur](https://i.imgur.com/YzCFkfl.png)

我們可以想像`xx + y`的時候`xx`會延伸成：
```
0 0 0 0 0
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
```
而`y`:
```
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
```
所以兩個相加會變成
```
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
```
那這就是所謂的廣播！

## reshape()
接下來說明一下會用到的方法函數，先來看看`reshape()`吧：
> Gives a new shape to an array without changing its data.

簡單來說`reshape()`就是用來改變array的shape，但並不會改變它的數值。

```python
s = np.arange(6)
```
建立一個`s = [0,1,2,3,4,5]`，接著將`s`做`reshape()`
```python
s = s.reshape((3, 2))
```
`s`就會變成`3 X 2`了，如圖：
![Imgur](https://i.imgur.com/48WEpcJ.png)

## ndarray.T
```python
x = np.zeros((10, 2))
```
上面這個是建立一個都是`0`的矩陣，矩陣形狀為 `10 X 2`
![Imgur](https://i.imgur.com/ThJ2RnS.png)

```python
y = x.T
```
`T`這個是將`x`整個選轉變成`2 X 10`，如圖：
![Imgur](https://i.imgur.com/59PIHTb.png)

再看一個例子：
```python
x = np.array([[3,4],[5,6]])
```
將`x`做transpose：
```python
x.T
```
![Imgur](https://i.imgur.com/Vh3QETC.png)
看出差別了吧！

## ndarray.base

> Base object if memory is from some other object.

我們直接來看一下範例就知道這是什麼了！
```python
y = np.array([1,2,3,4])
y.base is None
```
會得到 True，是因為它的基底不是從其他的數值來的，來看看我們最前面的範例：
```python
x = np.arange(4)
xx = x.reshape(4,1)
y = np.ones(5)
(xx + y)

xx.base is x
```
在上面第二行，將`x.reshape(4,1)`得到的結果給了`xx`，這表示`xx`是從`x`來的，所以`True`
來看看`y`呢？
```python
x = np.arange(4)
xx = x.reshape(4,1)
y = np.ones(5)
(xx + y)

xx.base is y
```
會得到`False`，如圖：
![Imgur](https://i.imgur.com/Q1CnqPX.png)
這樣可以看出差別了嗎？

## 總結
今天說明了廣播的特性，以及其他會用到的方法`reshape`、`T`以及`base`。

參考資料：
[numpy.reshape](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.reshape.html)
[numpy.ndarray.T](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.ndarray.T.html)
[numpy.ndarray.base](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.ndarray.base.html)

# [Day14]Numpy的ndarray！

在之前我們已經將pandas的概念以及使用說明完了，現在要進入Numpy這個主題了，其實在之前幾篇文章中已經有稍微使用到Numpy，只是都沒有深入的說明，接下來幾天我將會深入的說明它是如何使用的，敬請期待！


若是想看更多Numpy的介紹：
* [[Day 15]Numpy操作索引＆局部資料！](https://ithelp.ithome.com.tw/articles/10195645)
* [[Day16]Numpy的廣播&方法！](https://ithelp.ithome.com.tw/articles/10195830)
* [[Day17]Numpy的數學&統計方法！](https://ithelp.ithome.com.tw/articles/10195984)
* [[Day18]Numpy檔案輸入與輸出！](https://ithelp.ithome.com.tw/articles/10196167)


# ndarray
今天，來聊聊ndarray是什麼吧。

> ndarray, a fast and space-efficient multidimensional array providing vectorized arithmetic operations and sophisticated broadcasting capabilities

簡單來說ndarray是一個快速的且可以節省空間的多維度陣列，提供向量運算以及複雜的廣播光能，所謂的廣播功能是什麼，不用擔心，下面會繼續說明的！

# np.array()

首先，我們先引入`Numpy`這個套件：
```python
import numpy as np
```
建立資料data：
```python
data = np.array([[ 0.226, -0.23 , -0.86],
[ 0.5639, 0.2379, 0.904]])
```
我們使用`np.array()`這個方法，可以看到上面建立一個矩陣的資料。
輸出data可以看到：
```
array([[ 0.226 , -0.23  , -0.86  ],
       [ 0.5639,  0.2379,  0.904 ]])
```

# Type provide
我們可以提供我們要的資料類型給它，只需要在括號內加上`dtype=資料類型`
```python
np.array([1, 2, 3], dtype=complex)
```
可以看到輸出：
```
array([ 1.+0.j,  2.+0.j,  3.+0.j])
```

# Creating ndarrays
創建資料的方法，也可以先建立一個list：
```python
data1 = [6, 7.5, 8, 0, 1]
```
使用`np.array()`
```python
arr1 = np.array(data1)
```
輸出`arr1`就可以看到輸出結果：
```python
array([ 6. , 7.5, 8. , 0. , 1. ])
```
當然，資料不一定一定要一維的：
```python
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
```
上面這裡我們是給一個二維的陣列，一樣可以轉成ndarrays：
```python
arr2 = np.array(data2)
```

# .ndim
要如何看資料(ndarray)有多少維？
```python
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
arr2.ndim
```
使用`ndim`，上面的程式碼可以得到`2`。
**記得要是ndarray的型態才可以用哦**

如果資料是list忘記轉成ndarray會得到以下錯誤：
```python
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-27-78cb2f6fe29a> in <module>()
----> 1 data1.ndim
AttributeError: 'list' object has no attribute 'ndim'
```

# .shape
若是想看是幾乘幾的矩陣可以使用`shape`這個方法：
```python
arr2.shape
```
就可以得到 (2,4)

# .dtype
它和pandas相同也可以看資料類型：
```python
data.dtype
```

## 總結：
今天簡單說明了什麼是ndarray，講解了如何建立ndarray這樣的資料類型，還有查看資料的資訊，接下來會繼續說明如何操作ndarray的資料。

更多資訊：
[numpy.array](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.array.html)

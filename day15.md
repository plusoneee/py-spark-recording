# [Day 15]Numpy操作索引＆局部資料！

嗨！終於來到了1/2路程了，今天會繼續來說明Numpy的索引以及資料切割。


若是想看其他Numpy的介紹：
* [[Day14]Numpy的ndarray！](https://ithelp.ithome.com.tw/articles/10195434)
* [[Day16]Numpy的廣播&方法！](https://ithelp.ithome.com.tw/articles/10195830)
* [[Day17]Numpy的數學&統計方法！](https://ithelp.ithome.com.tw/articles/10195984)
* [[Day18]Numpy檔案輸入與輸出！](https://ithelp.ithome.com.tw/articles/10196167)

首先先匯入Numpy：
```python
import numpy as np
```
## Creat data
新增資料：
```python
arr = np.arange(10)
```
這跟python內的方法一樣，可以使用`arange()`建立一個範圍的資料：
```python
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

# Indexing
我們的資料是 ： array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#### 索引要如何使用？
和list一樣用[]就可以了：
```python
arr[5]
```
可以得到 5
```python
arr[5:8]
```
可以得到 5,6,7

#### 改變索引內的資料
我們改變索引第5到8的資料為7
```python
narr[5:9] = 7
```
可以看到結果：
```python
array([ 0, 1, 2, 3, 4, 7, 7, 7, 8, 9])
```

# Slicing
在這我們可以只改變局部的資料，這就是所謂的Slicing：
```python
myarr = np.arange(10)
slice = myarr[5:8]
myarr[5:8] = 7
slice[1] = 87
myarr
```
對得到結果：
```python
array([   0,    1,    2,    3,    4,   7,   87,   7,    8,    9])
```
第一行：建立的一個範圍0-9的資料
第二行：將5、6、7改為數字7
第三行：建立一個變數slice，內容為myarr[5:8]，也就是[7,7,7]
第四行：改變slice第1個索引為87
第五行：輸出myarr

可以看到我們局部修改了myarr的資料！

## 總結：
如果你剛接觸Numpy應該會覺得很神奇吧！因為numpy它常用來處理很大型的資料，所以這樣局部修改的功能是非常方便的，可以不需要另外複製一份！

下一次將會介紹更多的numpy資料操作，講解Numpy的廣播功能，明天見。


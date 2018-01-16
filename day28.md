

今天要來聊聊機器學習中的`特徵標準化(normalization)`，包含：
* 什麼是特徵標準化？
* 為什麼要標準化？
* 特徵標準化怎麼做？

# 什麼是標準化？
特徵標準化(normalization)是將特徵資料按比例縮放，讓資料落在某一特定的區間。

### 圖片說明
來看下方圖示，藍色圈圈代表的是特徵的等高線，左圖的特徵`X1`,`X2`區間相差非常大，所以對應的等高線非常尖，會導致在使用梯度下降法尋求最佳解時，需要很迭代多次才可以收斂。
![Imgur](https://i.imgur.com/4pW0eRh.jpg)


# 為什麼要標準化？
當特徵做標準化當然有它的優點，除了上述說明了可以優化梯度下降法外，還可以`提高精準度`。
怎麼說呢？有的分類器需要計算樣本間的距離，例如之前所提到的KNN，一個特徵值的範圍非常大，那麼距離計算通常就會取決於這個特徵，若情況是範圍小的特徵比較重要的話，就會與我們所要的結果是相反的。

* 補充：
若想知道關於KNN演算法怎麼做的可以看看之前的文章：[[Day26]機器學習：KNN分類演算法！](https://ithelp.ithome.com.tw/articles/10197110)

# 特徵標準化怎麼做？
在用程式碼說明之前，先來瞭解有哪些標準化的方式：

### 標準化方式：
通常有兩種標準化的方法：
* min max normalization：
    會將特徵數據按比例縮放到0到1的區間，（或是-1到1）。
* standard deviation normalization：
    會將所有特徵數據縮放成平均為0、平方差為1。

## 程式碼撰寫
為了證明標準化真的能夠讓幫助機器學習的訓練，我們要用程式碼來測驗看看，在sklearn裡面，已經有函數可以幫我們將資料做`標準化`，並不需要自行寫數學的方法，那就來看看怎麼用吧：

標準化是使用了叫做`preprocessing`的函數，我們引入它。需要創建資料所以也引入`numpy`：
```python
from sklearn import preprocessing
import numpy as np
```

* 用`train_test_split`來把資料做切分（一邊為訓練一邊為測試資料）
* 用`make_classification`用來產生隨機的訓練資料
* 用`SVC`這個分類法當作例子
```python
from sklearn.cross_validation import train_test_split
from sklearn.datasets.samples_generator import make_classification
from sklearn.svm import SVC
```

最後因為需要繪圖所以：
```python
import matplotlib.pyplot as plt
```

建立隨機的特徵資料並且繪圖：
```python
X,y = make_classification(n_samples=300,n_features=2,n_redundant=0,n_informative=2,
                          random_state=3,scale=100,n_clusters_per_class=1)
plt.scatter(X[:,0],X[:,1],c=y)
plt.show()
```
會看到下圖，有兩部分的資料，因為我們設定了`n_features=2`：
![Imgur](https://i.imgur.com/5yNOOF1.png)

將資料切分，並且用SVC分類法進行訓練：
```python
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
clf = SVC()
clf.fit(X_train,y_train)
```
最後用`score()`來查看訓練的分數如何：
```python
clf.score(X_test,y_test)
```
結果為：`0.36666666666666664`，也就是`準確度`只有`36%`。

### 標準化：
為了證明標準化能夠讓幫助資料訓練，我們使用`preprocessing.scale()`標準化`X`：
```python
X = preprocessing.scale(X)
```
一樣區分資料，並且訓練：
```python
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
clf = SVC()
clf.fit(X_train,y_train)
```
來看看得分多少吧：
```python
clf.score(X_test,y_test)
```
結果為：`0.98333333333333328`，`準確度`直接提高到`98%`啊！！！！

而且可以看到圖中的座標，X軸與Y軸的範圍縮小了：
![Imgur](https://i.imgur.com/u8bF9Gn.png)

## 總結
今天是第28天，說明了何為標準化（正規化）並用程式碼證明了為何需要標準化，因為標準化可以幫助機器學習訓練的時候有更好的資料結構，進而提高資料的準確度。

更多參考資料來源：
[為什麼一些機器學習模型需要對數據進行歸一化？](https://read01.com/7BD3QR.html#.Wl2iLLb3Wpk)
[莫煩 正規化Normalization](https://morvanzhou.github.io/tutorials/machine-learning/sklearn/3-1-normalization/)



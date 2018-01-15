
# [Day26]機器學習：KNN分類演算法！

嗨！今天是第26天，之前介紹完了基本的機器學習概念了，這次要說明一個K-近鄰演算法（K Nearest Neighbor）！

### 什麼是K-近鄰演算法？

> k是一個用戶定義的常數。一個沒有類別標籤的向量（查詢或測試點）將被歸類為最接近該點的k個樣本點中最頻繁使用的一類。

簡單來說，我們要找出和新數據附近的K個鄰居（資料），這些鄰居是哪一類（標籤）的它就是哪一類的啦。

# sklearn
那我們就直接開始撰寫程式並說明吧！
```python
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
```

我們用鳶尾花的資料集做測試，所以`import datasets`，用sklearn的其中一個優點就是包含了豐富的函數，所以要用knn演算法只要直接引入(import KNeighborsClassifier)就可以了。

## load_iris
要匯入鳶尾花的資料只需要使用`datasets.load_iris()`函數就可以了：
```python
iris = datasets.load_iris()
```
可以到[安德森鳶尾花卉數據集](https://zh.wikipedia.org/wiki/安德森鸢尾花卉数据集)就可以看到裡面有一個表格(如圖)：
![Imgur](https://i.imgur.com/bO7ukyu.png)
上面包含了`特徵`資料（花萼長、寬等等）以及最右邊的`標籤`也就是屬種。

定義特徵資料：
```python
iris_data = iris.data
```
可以印出前三筆資料：
```python
iris_data[0:3]
```
會看到結果：
```python
array([[ 5.1,  3.5,  1.4,  0.2],
       [ 4.9,  3. ,  1.4,  0.2],
       [ 4.7,  3.2,  1.3,  0.2]])
```
跟上面鳶尾花資料表格內的資料是一樣的！

## train_test_split
一般來說，我們會將資料分成兩個部分：`訓練資料`與`測試資料`，訓練資料用在訓練模型的時候，測試則用來測試看看這個模型預測的準確度。
使用`train_test_split()`函數可以簡單的將資料分開成兩部分：
```python
train_data , test_data , train_label , test_label = train_test_split(iris_data,iris_label,test_size=0.2)
```
上面就是我們將資料分成兩份的程式碼：一部分是用來訓練電腦的(0.8)、一部份用來測試(0.2)。

## KNeighborsClassifier
要使用KNeighbors分類法，直接使用sklearn的`KNeighborsClassifier()`就可以了：
```python
knn = KNeighborsClassifier()
```
上面程式碼中我們不改變`KNeighborsClassifier()`中預設的參數，若你想要自行設定內部參數可以參考：[sklearn KNeighborsClassifier](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)

將資料做訓練：
```python
knn.fit(train_data,train_label)
```

## predict
預測我們剛剛切分出來的`test_data`資料
```python
print(knn.predict(test_data))
```
結果為：
[2 1 1 1 2 2 0 0 0 1 0 2 2 2 0 2 0 0 1 2 0 0 0 0 2 1 1 0 1 0]

看一下正確答案是否跟預測一樣：
```python
print(test_label)
```
結果為：
[1 1 1 1 2 2 0 0 0 1 0 2 2 2 0 2 0 0 1 2 0 0 0 0 2 1 1 0 1 0]

哦！發現第一個的結果預測錯誤！不過其他都是一樣的！這是正常的，就像人一樣可能會有出錯誤判的時候，電腦也會有。
![Imgur](https://i.imgur.com/7WogKXg.png)

## 總結
今天說明了knn演算法，是機器學習中較好理解的一個演算法，是透過找出附近鄰居的分類定義來自己的類別，並用sklearn輕易的完成這個機器學習的演算法。

更多參考資料：
[[Machine Learning] kNN分類演算法](http://enginebai.logdown.com/posts/241676/knn)
[最近鄰居法 維基百科](https://zh.wikipedia.org/wiki/最近鄰居法)
[sklearn KNeighborsClassifier](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)

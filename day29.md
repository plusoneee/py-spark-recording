

倒數第二天！

今天要來看機器學習中很重要的`交叉驗證(Cross validation)`：


# 交叉驗證

一般來說我們會將數據分為兩個部分，一部分用來訓練，一部分用來測試，交叉驗證是一種統計學上將樣本切割成多個小子集的做測試與訓練。

交叉驗證主要分為以下幾類：

* k-folder cross-vailation
* kk folder cross-vaildation
* least-one-out cross-validation
* 10-fold corss validation

如果想要知道更多關於上述交叉驗證法的優缺點可以到：[機器學習中的交叉驗證cross-validation](http://blog.csdn.net/lhx878619717/article/details/49079785)

## 為什麼需要交叉驗證

為了避免依賴某一特定的訓練和測試資料產生偏差。

> which is intended to avoid the possible bias introduced by relying on any one particular division into test and train components, is to partition the original set in several different ways and to compute an average score over the different partitions.

一個更好的方式是把原始資料按不同的方法分，計算不同部分的平均得分。

誇張點來說，我們都只有用一部分特定的測試資料去測試我們訓練的結果，假設剛好那一部分測試資料剛好百分之百一樣，而其他部分剛好都不準確，我們就以為這個訓練結果是百分之百的。

## 交叉驗證怎麼做？

> K-Fold Cross Validation is used to validate your model through generating different combinations of the data you already have. For example, if you have 100 samples, you can train your model on the first 90, and test on the last 10. Then you could train on samples 1-80 & 90-100, and test on samples 80-90. Then repeat. This way, you get different combinations of train/test data, essentially giving you ‘more’ data for validation from your original data. 

在k交叉驗證中，是使用不同的資料組合來驗證你訓練的模型，舉例來說，假設你有100個樣本，你可以第一次先使用前90個做訓練，另外10個做測試，然後再用第80到90個，不斷重複這個動作，這樣你可以得到不同的訓練/測試資料組合，提供更多數據去驗證。 

關於上述內容可以到：[K-Fold Cross Validation and GridSearchCV in Scikit-Learn](https://randomforests.wordpress.com/2014/02/02/basics-of-k-fold-cross-validation-and-gridsearchcv-in-scikit-learn/)看更詳細說明。


![Imgur](https://i.imgur.com/tLWEE80.png)

如上圖，我們將資料分成`10`等份，其中`第1`等分用來當作`驗證`的測試資料，其餘`9`份拿來訓練，下一輪我們繼續將`第2`等分拿來當作驗證的測試資料，其餘`9`份一樣拿來訓練，總共做10次。
藉著將`10次`的`準確性(Accuracy)`平均，而這個得到的平均值，我們可以自信的說這個數值就是我們的準確度沒有偏差。


## 程式碼
接下來要來看一下怎麼使用python做交叉驗證！

### 引入
首先，我們將會用到的函數庫引入：
```python
from sklearn.cross_validation import cross_val_score
```
`cross_val_score`這是驗證用來評分資料準確度的。

還有：
```python
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
```
上述的在之前都介紹過了，這邊就不多做說明了，接著導入資料：
```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
```

### KNeighborsClassifier
我們使用之前所說明過的KNN分類法，並且定義`n_neighbors=10`，這裡的`10`是會去找附近的`10`個鄰居。
```pthon
knn = KNeighborsClassifier(n_neighbors=10)
```

### cross_val_score
我們在前面圖片中，將資料分成10組，而這裡的`cv=5`是分成5組的意思。
`'accuracy'`則是一種方法，是顯示準確度高不高的方法（越高越好），接下來我們將得分取平均：
```python
scores = cross_val_score(knn,X,y,cv=5,scoring='accuracy')
print(scores)
print(scores.mean())
```
全部分數為`[ 0.96666667  1.      1.      0.93333333  1.      ]`
平均為：`0.98`

可以看到上面有`100%`正確的，也有`93%`的。所以假設我們只取一組當測試資料，剛好取到的是`100%`的部分，我們就會以為我們的結果準確度是百分之百的。

### 改變n_neighbors
我們剛剛將`n_neighbors=10`，可以得到`平均98%`的`準確度`，我們要用交叉驗證來測試到底用多少個neighbor可以得到較高的準確度：

```python
k_range = range(1,31)
k_scores = []
for k_number in k_range:
    knn = KNeighborsClassifier(n_neighbors=k_number)
    scores = cross_val_score(knn,X,y,cv=10,scoring='accuracy')
    k_scores.append(scores.mean())
```

### 繪圖
```python
plt.plot(k_range,k_scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Validated Accuracy')
plt.show()
```
![Imgur](https://i.imgur.com/s0d4JlT.png)

## 總結
我們可以從上圖看到不同的n_neighbors會有不同的準確度，中間取間的k數量是最好的，而到後面則有下降的趨勢，就是所謂的`Overfitting`，意思就是太過追求參數完美預測出訓練數據結果，反而會導致實際預測效果不佳。



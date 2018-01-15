
# [Day27]機器學習：建立線性迴歸資料與預測！

嗨，今天是鐵人賽的第27天啦！
今天要介紹的是一個簡單的預測法：`線性迴歸（linear regression)`！

### 什麼是線性迴歸？

> Finding the curve that best fits your data is called regression, and when that curve is a straight line, it's called linear regression.

找出符合資料規律的直線，就叫線性迴歸。

在線性回歸中，數據使用線性預測函數來建模，未知的模型參數也是通過數據來估計。這些模型被叫做線性模型。
最常用的線性回歸建模是給定X值的y的條件均值是X的仿射函數。
線性回歸模型可以是一個中位數或一些其他的給定X的條件下y的條件分布的分位數作為X的線性函數表示。

# sklearn
今天我們一樣會使用`sklearn`來做線性迴歸（linear regression)！

首先import LinearRegression，因為我們會繪圖所以會用到`matplotlib.pyplot`也引入:
```python
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
```

## 建立迴歸資料

在sklearn中很方便的是它內涵豐富的函數可以使用，所以要建立`隨機`資料只需要：
```python
X,y = datasets.make_regression(n_samples=200,n_features=1,n_targets=1,noise=10)
```
使用`make_regression()`方法，建立200個樣本(samples)，只有一種`特徵(features)`和一種標籤類別（label），我們將`noise`設為10，這樣資料會比較分散一點（上述參數都可以自行設定）。

可以到 [sklearn.datasets.make_regression](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html)看內部更多參數的使用。

## Scatter散點圖繪製
我們將剛剛建立的資料繪成散點圖：
```python
plt.scatter(X,y,linewidths=0.1)
plt.show()
```
會看到散點圖：
![Imgur](https://i.imgur.com/Ky8aIGS.png)
* 注意：因為資料建立為`隨機`的，所以看到的圖可能會稍微有所不同！

## LinearRegression
接下來要做線性迴歸預測了！
使用線性迴歸會用到sklearn中的LinearRegression函數

建立一個模型`model`為線性迴歸模型：
```python
model = LinearRegression()
```
這裡我們使用預設就好的不改變內部的參數，當然你可以到[sklearn LinearRegression](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)文檔內看更多關於sklearn LinearRegression如何使用。

將資料放進模型內訓練：
```python
model.fit(X,y)
```

因為要再繪出預測的資料圖，所以將預測資料放到predict變數內：
```python
predict = model.predict(X[:200,:])
```

繪圖：
```python
plt.plot(X,predict,c="red")
plt.scatter(X,y)
plt.show()
```
![Imgur](https://i.imgur.com/Jcyw9VT.png)

中間的紅色線就是我們用LinearRegression找出的線，這樣就完成線性迴歸預測了。

## 總結
今天說明了線性迴歸LinearRegression，用sklearn快速建立隨機的迴歸資料並且分析。

更多參考資料：
[線性迴歸 維基百科](https://zh.wikipedia.org/wiki/線性回歸)
[sklearn LinearRegression](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
[sklearn.datasets.make_regression](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html)



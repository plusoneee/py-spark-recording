# [Day21]Pandas就能輕易將資料視覺化！

今天是第21天了！
前兩天說明了matplotlib是如何將資料視覺化的，今天就要來看看如何用Pandas就可以將資料視覺化！

首先，先`import`
```python
import pandas as pd
```
不過這裡我會直接使用yahoo的資料所以再加上下面兩行：
```python
from pandas_datareader import data
import pandas_datareader.data as web
```
如果顯示沒有`pandas_datareader`的話：
```
conda install pandas_datareader
or 
pip install pandas_datareader
```

import datetime：
```python
import datetime
```

# Remote Data Access
開始定義資料吧：
```python
start = datetime.datetime(2016, 1, 1)
end = datetime.datetime(2017, 1, 1)
```
上面我們先定義start開始時間與end結束時間為我們要抓取的資料範圍。
接下來抓取yahoo上的資料：
```python
data = web.DataReader("F", 'yahoo', start, end)
```
上面這邊引入了`yahoo`上`"F"`也就是Finance的資料，並給予要抓取的開始時間start與結束時間end。
![Imgur](https://i.imgur.com/d4aQgtF.png)

# Plot()
OK，接下來就要來看今天最神奇的部分了！

有了資料後，直接使用`plot()`函數：
```python
data.plot()
```
然後！登冷！你就會看到：
![Imgur](https://i.imgur.com/6Hk7l5z.png)
竟然不需要自行定義資料或標籤！

那因為`Volume`的數值太大了，以至於其他的值變動在圖上會看不出來，現在要取單獨一個值來看！

假設我們要看`Close`:
```python
data.plot(y="Close")
```
我們只需要改變`plot()`內的`y`參數就可以了！

或是我們之前在說明pandas的時候是如何取出單項資料的還記得嗎！
只要：
```python
data["Close"]
```
![Imgur](https://i.imgur.com/Gxzq0X9.png)

所以繪圖也可以這樣做：
```python
data["Close"].plot()
```
![Imgur](https://i.imgur.com/PjH03vk.png)
兩個方式是一樣的哦！

#### 可以一次取兩個以上嗎？

既然可以用`data["Close"]`一次取單項了，要取兩項資料當然可以：
```python
data[["High","Low"]].plot()
```
只需要裡面放`list`格式就可以了！是不是跟超級方便呢！
![Imgur](https://i.imgur.com/g7xA3kw.png)


# with Numpy
用padas繪圖，若要用Numpy的資料呢？

```python
import numpy as np
df = pd.DataFrame(np.random.randn(100, 4), index=pd.date_range('12/31/2017', periods=100), columns=list('ABCD'))
```
上面建立一筆隨機的資料`np.random.randn(100, 4)`，x為日期，`columns設定為A,B,C,D`

將資料累加
```python
df = df.cumsum()
```

### plot()
```
df.plot()
```
![Imgur](https://i.imgur.com/VGk9uxv.png)

# 總結
今天說明了如何用pandas將資料視覺化，也介紹了`pandas-datareader`這個好用的東西！
如果想暸解更多使用pandas-datareader抓股票的話可以到： [pandas-datareader](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#)



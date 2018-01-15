# [Day20]Matplotlib資料視覺化進階！

上一篇介紹了`Matplotlib`是如何做到讓資料變成折線圖，今天要說明如何結合`pandas`或`numpy`製作出其他樣式的資料圖表！

**那我們就開始吧！（let's go!）**
先import matplotlib：
```python
import matplotlib.pyplot as plt
```
# pie Chart
今天來介紹圓餅圖吧！
加入label：
```python
labels = 'A','B','C','D','E','F'
```

設定每塊的大小：
```python
size = [33,52,12,17,62,48]
```

要圓餅圖使用`plt.pie()`
```python
plt.pie(size , labels = labels,autopct='%1.1f%%')
```
size與labels都是上面設定的資料，`autopct='%1.1f%%'`是用來顯示百分比。

為了要讓圓餅圖比例相等加上：
```python
plt.axis('equal')
```

最後顯示：
```python
plt.show()
```

![Imgur](https://i.imgur.com/1Hn7QDC.png)

## separated
在pie裡面還有一個參數`explode`可以使用，我們直接來使用吧：
上面的程式碼新增：
```python
separated = (.1,0,0,0,0,0)
```
上面幾個.1,0,0,0,0,0 分別為 'A','B','C','D','E','F'，這是設定分開的數值(距離)。
修改`plt.pie()`的內容新增一個`explode`參數，變成：
```python
plt.pie(size , labels = labels,autopct='%1.1f%%',explode=separated) 
```
接著show資料：
![Imgur](https://i.imgur.com/hZbtgKF.png)
就會看到`A`的部分分開了，也可以自行改變`separated`內的數字，看看改變了什麼！

## With pandas
現在要加上我們之前講的`pandas`，來把`pandas`的資料做視覺化！
```python
import matplotlib.pyplot as plt
import pandas as pd
```
先定義資料：
```python
data = {'names':['a','b','c','d','e'],
        'jan':[133,122,101,104,320],
        'feb':[122,132,144,98,62],
        'march':[64,99,32,12,65] }
```
接著將資料設定為DataFrame資料格式，放到變數`df`：
```python
df = pd.DataFrame(data,columns=['names','jan','feb','march'])
```
定義（總）大小：
```pyhton
df['total'] = df['jan']+ df['feb']+df['march']
```
資料內容就定義完了，現在就要變成圓餅圖了：

定義顏色：
```python
colors = [(1,.4,.4),(1,.6,1),(.5,.3,1),(.7,.7,.2),(.6,.2,.6)]
```
定義圓餅圖，上面定義的資料放進去：
```python
plt.pie( df['total'] ,
    labels = df['names'],
    colors = colors,
    autopct='%1.1f%%',
    ) 
```

等比例：
```python
plt.axis('equal') 
plt.show()
```
![Imgur](https://i.imgur.com/Khog5vZ.png)

# Bar Chart
接下來要來製作長直條圖表，一樣先import：
```python
import matplotlib.pyplot as plt
```
## With Numpy
這裡我們用Numpy來幫助我們建立資料：
```pyhton
import numpy as np
```

先建立資料：
```python
col_count = 3
A_scores = (553,536,548)
B_scores = (518,523,523)
C_scores = (613,570,588)
D_scores = (475,505,499)
```
上面我們定義了A,B,C,D三人的成績，建立index：
```python
index = np.arange(col_count)
```

建立圖表：
```python
k = plt.bar(index,k_scores, .5)
plt.grid(True)
plt.show()
```
就有基本的Bar圖表了：
![Imgur](https://i.imgur.com/4fMiHal.png)

接下來我們要建立下面這個圖表：
![Imgur](https://i.imgur.com/Kwrkmjv.png)

上方可以看到有A,B,C,D四個人，每個人有三個分數包含數學、閱讀、科學。

**來看看怎麼做吧！**

一樣，先定義資料：
```python
col_count = 3
bar_width = 0.2
index = np.arange(col_count)
A_scores = (553,536,548)
B_scores = (518,523,523)
C_scores = (613,570,588)
D_scores = (475,505,499)
```

定義bar的圖型：
```python
A = plt.bar(index,
           A_scores, 
           bar_width,
           alpha=.4,
           label="K") 
B = plt.bar(index+0.2,
            B_scores,
            bar_width,
            alpha=.4,
            label="C") 
C = plt.bar(index+0.4,
            C_scores,
            bar_width,
            alpha=.4,
            label="N") # x,y ,width
D = plt.bar(index+0.6,
            D_scores,
            bar_width,
            alpha=.4,
            label="F") # x,y ,width
```

每個長條圖上面都有顯示文字：
```python
def createLabels(data):
    for item in data:
        height = item.get_height()
        plt.text(
            item.get_x()+item.get_width()/2., 
            height*1.05, 
            '%d' % int(height),
            ha = "center",
            va = "bottom",
        )
createLabels(A)
createLabels(B)
createLabels(C)
createLabels(D)
```
上面這裡我們用到了`plt.text()`定義文字，參考：
[How to write text above the bars on a bar plot (Python)?](https://stackoverflow.com/questions/40489821/how-to-write-text-above-the-bars-on-a-bar-plot-python)

最後：
```python
plt.ylabel("Mean score")
plt.xlabel("Subject")
plt.title("Test Scores by Contry")
plt.xticks(index+.3 / 2 ,("Math","Reading","Science"))
plt.legend() 
plt.grid(True)
plt.show()
```

`plt.legend() `為右上角的圖。
`plt.xticks`為底下的文字（為了至中所以`+.3 / 2`）


ok 這就是今天顯示圖表的部分了！

更多參考資料：
[matplotlib.org/pie](https://matplotlib.org/devdocs/gallery/pie_and_polar_charts/pie_demo2.html#sphx-glr-gallery-pie-and-polar-charts-pie-demo2-py)
[matplotlib.org/barchart](https://matplotlib.org/examples/api/barchart_demo.html)

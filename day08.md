# [Day08]Pandas資料的取得與篩選！

嗨，今天第八天了，最喜歡8這個數字了！（題外）
上一篇說明了如何讀取檔案還有pandas內的函式，包含查看資料內容、資料選擇、新增、刪除、空白填充以及排序。panda當然不只有這些功能，接下來我們就要來繼續探討它如何用之前所學到的運算子將做資料過濾，取得我們真正需要的資料。

若想看一下pandas的精彩（？）回顧：
[[Day06]Pandas的兩種資料類型！](https://ithelp.ithome.com.tw/articles/10193394)
[[Day07]Pandas操作資料的函數！](https://ithelp.ithome.com.tw/articles/10193421)

那就開始吧！
# 資料取得
這裡先複習一下資料的取得，會用到之前python運算元的觀念，
如果還是有困惑的地方，趕快看前兩天的pandas精彩（？）回顧，
放心，我會等你的（眼神堅定）。

## Series
先來建立一個Series：
```python
seriesObj = pd.Series(range(10),index=['a', 'a', 'b', 'b', 'b','c','c','c','c','c'])
```
建立一個範圍從0到9的資料並設定index，記得要用pandas前要先`import pandas`:
```python
import pandas as pd
```
還記得上之前講過要如何取得要得數值吧？現在想看看下面這個程式碼會出現什麼結果？
```python
seriesObj['c'] 
```
答案是輸出：
```python
c    5
c    6
c    7
c    8
c    9
dtype: int64
```

## Dataframe
現在我們再來試試看dataframe吧，建立一個dataframe：
```python
df = pd.DataFrame(np.random.randn(4,2),index=['a', 'a', 'b', 'b'])
```
我們創建一個4✖️2的陣列，要引入一個叫做`numpy`的套件，這個我們之後會花時間解釋(敬請期待）：
```python
import numpy as np
```
只要知道它是用來建立矩陣的，接著我們隨機給予數值：
```python
import numpy as np
df = pd.DataFrame(np.random.randn(4,2),index=['a', 'a', 'b', 'b'])
df
```
會看到輸出：
![Imgur](https://i.imgur.com/WhOFwWJ.png)
現在若要取出row b的值，可以這樣做：
```python
df.ix['b']
```

事不宜遲！進入資料篩選的部分吧！
# 資料篩選
要進入今天主要的部分了，今天要說明如何過濾資料只取得我們所要的數值，這就會用到我們之前在說明運算子的觀念了，

所以不熟悉python運算子的話先回去複習：
[[Day03]Python的基本運算！（上）](https://ithelp.ithome.com.tw/articles/10192814)
[[Day04]Python的基本運算！（下）](https://ithelp.ithome.com.tw/articles/10193001)

而我依然會在這裡等你的（眼神依然堅定）。

沒問題的話就繼續看下去吧！（let's go!）
![Imgur](https://i.imgur.com/ijp4aAm.png)

### 運算子運用
假設我現在要找出Gender為Male的員工我們可以用 `==` 判斷：
```python
employees["Gender"] == "Male"
```
執行上面的程式碼可以看到若為Male則顯示True否則False，接著我們以這個當作過濾器：
```python
fliter = (employees["Gender"] == "Male")
employees[fliter]
```
執行就可以看到顯示出來的員工資料都是男性的。

除了==當然也可以用`!=`像是：
```python
mask = employees['Team'] != "Finance"
```

當然也可以用`<`,`>`像是：
```python
employees["Salary"] > 148941
employees[employees["Salary"] > 148941]
```
用比較運算子就可以過濾並取得我們所要的數值，上面可顯示出薪水>148941的資料。
當然要在過濾日期也可以做到：
```python
mask = employees["Start Date"] <= "1980-05-01"
employees[mask]
```
![Imgur](https://i.imgur.com/GozzqTT.png)

假設我們想要過濾不只一個條件呢？記得布林運算子嗎？這時候就可以用上了！讓我們來看看吧！
```python
mask1 = employees["Team"] != "Marketing"
mask2 = employees["Start Date"] < "1980-01-01"
```
上面這裡的程式中，我們設定mask1為team不為Marketing的資料，把mask2設定成開始日期小於1980-01-01的資料。

設定完遮罩之後我們就可以用布林運算子（and）：
```python
employees[(mask1 & mask2)] 
```
這樣就只會顯示mask1和mask2都成立的資料，當然也可以用或（or）：
```python
employees[(mask1 ｜ mask2)] 
```

### .isin()
除了運算子其實還有其他方法可以做到：
```python
mask = employees["Team"].isin(["Legal","Scales","Product"])
```
就是上面的`.isin()`方法。

### innull() & notnull()
上一篇我們提到如何將NaN的值刪除，我們來看`innull()`跟`notnull()`兩個方法吧！
`isnull()`如果值是空的就會顯示`True`
```python
mask = employees["Team"].isnull()
```

`notnull()`如果值不是空的就會顯示True
```python
mask = employees["Team"].notnull()
```

### between()
上面提到可以用兩個比較運算子取出範圍，但其實還有一個方法可以取中間值就是`.between()`：
```python
employees[employees["Start Date"].between("2009-11-10","2010-01-20")]
```
使用`.between("2009-11-10","2010-01-20")`可以得到2009-11-10到2010-01-20間的數值。
```python
employees[employees["Start Date"].between("2009-11-10","2010-01-20")]
```

![Imgur](https://i.imgur.com/YvTKQzO.png)

## 總結
今天複習了資料的取得，說明了如何運用python的運算子過濾資料，還有用pandas內的函數取得。
那今天就到這啦！第八天就這麼結束了，只有一次，第三十天或第七天其實也是（廢話），那就明天見啦！

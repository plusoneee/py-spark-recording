
# [Day11]Pandas使用多層索引！

我們在上一篇（Day10）提到了groupby，第9天說明了索引的操作，那今天要繼續index這個主題繼續延伸說明多層索引！

首先要開始之前先import再說：
```python
import pandas as pd
```
匯入我們的資料，顯示前10筆資料：
```python
bigmac = pd.read_csv("./csv/bigmac.csv",parse_dates=["Date"])
bigmac.head(10)
```
![Imgur](https://i.imgur.com/AKaNIbA.png)

## set_index()
使用`set_index`設定index，
```python
bigmac.set_index(keys = ["Date","Country"],inplace=True)
```
```python
bigmac.head()
```
設定`Date`、`Country`為`index`就會像下圖這樣index改變：
![Imgur](https://i.imgur.com/id3CBrT.png)

### 使用index.names
查看有哪些index：
```python
bigmac.index.names
```
輸出：
```
FrozenList(['Date', 'Country'])
```
### 使用type()
查看資料的類型：
```
type(bigmac.index)
```
可以看到類型為 `pandas.core.indexes.multi.MultiIndex`
是MultiIndex!

## The get_level_values() Method
接下來說明`.get_level_values()`首先我們先匯入檔案，並設定`index_col`：
```python
bigmac = pd.read_csv("./csv/bigmac.csv",parse_dates=["Date"],index_col=["Date","Country"])
```
### sort index
使用`sort_index()`排序資料，因為上面我們已經將`index`改變，所以排序也會依照日期以及城市：
```
bigmac.sort_index(inplace=True)
bigmac.head(10)
```
![Imgur](https://i.imgur.com/jjxMl5b.png)

### get_level_values(0)
來看看get_level_values(0)會得到什麼吧：
```python
bigmac.index.get_level_values(0)
```
輸出：
```python
DatetimeIndex(['2010-01-01', '2010-01-01', '2010-01-01', '2010-01-01',
               '2010-01-01', '2010-01-01', '2010-01-01', '2010-01-01',
               '2010-01-01', '2010-01-01',
               ...
               '2016-01-01', '2016-01-01', '2016-01-01', '2016-01-01',
               '2016-01-01', '2016-01-01', '2016-01-01', '2016-01-01',
               '2016-01-01', '2016-01-01'],
              dtype='datetime64[ns]', name='Date', length=652, freq=None)
```
可以得到第`0`index的資料，也就是`'Date'`。

### get_level_values("Date")
其實括弧內可以直接放入要的index：
```
bigmac.index.get_level_values("Date")
```
輸出：
```python
DatetimeIndex(['2010-01-01', '2010-01-01', '2010-01-01', '2010-01-01',
               '2010-01-01', '2010-01-01', '2010-01-01', '2010-01-01',
               '2010-01-01', '2010-01-01',
               ...
               '2016-01-01', '2016-01-01', '2016-01-01', '2016-01-01',
               '2016-01-01', '2016-01-01', '2016-01-01', '2016-01-01',
               '2016-01-01', '2016-01-01'],
              dtype='datetime64[ns]', name='Date', length=652, freq=None)
```
兩種得到的內容是一樣的哦！如圖：
![Imgur](https://i.imgur.com/t35bpEt.png)

所以下面兩種寫法得到的也是一樣的：
```python
bigmac.index.get_level_values(1) 
bigmac.index.get_level_values("Country")
````

## The set_names() Method On MultiIndex
接下來介紹一下` .set_names()`方法，先重新匯入csv檔案並排序：
```python
bigmac = pd.read_csv("./csv/bigmac.csv",parse_dates=["Date"],index_col=["Date","Country"]) 
bigmac.sort_index(inplace=True)
```
我們可以更改index的名稱：
```python
bigmac.index.set_names(["Day","Location"],inplace=True)
```
有沒有覺得很熟悉？在單index裡有，多層index當然也有！
![Imgur](https://i.imgur.com/1TINOfh.png)

## 總結

今天說明了多層MultiIndex的設定與應用，這邊只有列出MultiIndex基本必要的方法，當然不只有這些可以用，還有`stack()`、`unstack()`等函數可以使用，想知道更多的可以點下面的連結：

[10 Minutes to pandas #stack](https://pandas.pydata.org/pandas-docs/stable/10min.html#stack)



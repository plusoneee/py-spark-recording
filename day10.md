# [Day10]Pandas Groupby使用！

接下來就來聊聊Groupby是什麼吧！

> Splitting the data into groups based on some criteria
> Applying a function to each group independently
> Combining the results into a data structure

有使用SQL語法的話，對它應該不陌生，是根據要的某一項資料做分組方便查找，根據不同組別做資料處理的概念。
直接開始使用就知道啦！(let's go!)

>The SQL GROUP BY Statement
The GROUP BY statement is often used with aggregate functions (COUNT, MAX, MIN, SUM, AVG) to group the result-set by one or more columns.

```python
import pandas as pd
fortune = pd.read_csv("./csv/fortune1000.csv",index_col="Rank")
```
`import` pandas並且匯入資料，資料的index設定為`"Rank"`。（如圖）
![Imgur](https://i.imgur.com/Rpo0Rci.png)

## Groupby()
使用`groupby()`方法可以將資料依照自己要的column分組，我們用`Sector`的內容做分組的依據，並存到變數內：
```python
sector = fortune.groupby("Sector")
```

## Groupby type
將`fortune`資料做`groupby`之後，可以來看看它的資料類型：
```python
type(sector)
```
使用type可以看到資料類型：`pandas.core.groupby.DataFrameGroupBy`

## Group size
我們可以用`size()`看`sector`裡面每個組別內的大小：
```python
sector.size()
```
輸出：
```
Sector
Aerospace & Defense              20
Apparel                          15
Business Services                51
Chemicals                        30
Energy                          122
Engineering & Construction       26
Financials                      139
Food and Drug Stores             15
Food, Beverages & Tobacco        43
Health Care                      75
Hotels, Resturants & Leisure     25
Household Products               28
Industrials                      46
Materials                        43
Media                            25
Motor Vehicles & Parts           24
Retailing                        80
Technology                      102
Telecommunications               15
Transportation                   36
Wholesalers                      40
dtype: int64
```

## get_group()
知道如何建立group之後，就來看看怎麼依據取資料吧！
```python
fortune = pd.read_csv("./csv/fortune1000.csv",index_col="Rank")
sectors = fortune.groupby("Sector")
```
一樣，先匯入資料，接著用`get_group()`這個方法：
```python
sectors.get_group("Energy")
```
括弧內放入要取出的類別，這邊我們找`"Energy"`。(如圖)
![Imgur](https://i.imgur.com/0ynrDrk.png)

如果還不清楚的話，來寫一個簡單的例子吧！
我們先定義`col`和`data`內容：
```python
col = ['class','name','hbd']
data = [['class0', 'user0', '1993-10-01'],
        ['class0', 'user1', '1992-10-02'],
        ['class1', 'user2', '1990-10-01'],
        ['class2', 'user3', '1983-10-03'],
        ['class1', 'user4', '1991-10-02'],
        ['class0', 'user5', '2001-10-03']]
frame = pd.DataFrame(data,columns=col)
```
上面可以看到總共有class0到2三個類別，我們要依據這項資料做分組：
```python
frame_class = frame.groupby('class')
```
分組之後，可以用`groups`來看結果：
```python
frame_class.groups
```
可以看到輸出：
```
{'class0': Int64Index([0, 1, 5], dtype='int64'),
 'class1': Int64Index([2, 4], dtype='int64'),
 'class2': Int64Index([3], dtype='int64')}
```
表示資料被分成`class0`,`class1`,`class2`，且顯示每個組有什麼資料與資料類型。

接著來使用`get_group()`取出class1：
```python
frame_class.get_group("class1")
```

## Groupby運算
講了這些，到底為何要做分組呢？
假設我們想知道不同族群的收入該怎麼做呢？其實分組後依然可以使用數學計算的方法：
一樣可以用`sum()`:
定義一組資料集：
```python
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                      'foo', 'bar', 'foo', 'foo'],
                   'B' : ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                   'C' : np.random.randn(8),
                   'D' : np.random.randn(8)})
```
記得要匯入pandas&numpy
```python
import pandas as pd
import numpy as np
```
![Imgur](https://i.imgur.com/mVajYuo.png)
計算總和：
```python
df.groupby('A').sum()
```
計算兩群組總和
```python
df.groupby('A').sum()
```
![Imgur](https://i.imgur.com/HxN2pSt.png)

## 總結
今天說明了`groupby`的使用，上一篇我們說明了Index的使用，但是都只是單一索引（index），下一篇我將會介紹如何使用多層索引MultiIndex！敬請期待啦！

更多參考資料：
[10 Minutes to pandas](https://pandas.pydata.org/pandas-docs/stable/10min.html)

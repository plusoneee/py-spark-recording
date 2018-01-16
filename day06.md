# [Day06]Pandas的兩種資料類型！

上一篇開始介紹了數據分析會使用到的幾個package，包含：

* Pandas 
* Numpy
* Matplotlib
* SciPy

接下來會先從`Pandas`開始講起，想看介紹的看上一篇：
[[Day05]聊聊重要的三個package吧！](https://ithelp.ithome.com.tw/articles/10193295)

**Pandas**是一個基於**Numpy**的package，在處理數據方面非常的好用簡單，在學習pandas之前我們要先知道pandas的兩種特有的資料結構`DataFrame`與`Series`。

通常應該先介紹Numpy才對啦可是我比較喜歡Pandas有一種很多熊貓的感覺XD(?)

廢話不多說，我們開始吧！（let's go?)

## 匯入Pandas

首先我們先import pandas才可以使用它：
```python
import pandas as pd
```
查看pandas的版本：
```python
pd.__version__
```

## 資料類型 - Series
Series，是一個類似陣列的物件，裡面可包含陣列的資料（Numpy之後會繼續做解釋），
最簡單的Series格式就是一個一維陣列的資料：
```python
my_obj = pd.Series([4, 7, -5, 3])
```
在這裡我們宣告一個pandas的Series類型資料，非常簡單的使用`.Series()`並將數值放到一個變數中。

若要讀取Series的value我們可以使用`.values`：
```python
my_obj.values
```
若要讀取Series的`index`：
```python
my_obj.index
```
**Series**的**index**若沒有自己設定的話它會自動分配！
```python
my_obj.index
```
輸出：
```
RangeIndex(start=0, stop=4, step=1)
```
### 改變Index
`Index`可以不一定是要從`0`開始也可以是其他的內容，我們可以這樣宣告：
```python
my_obj2 = pd.Series([8,9,10,11], index=['a','b','c','d'])
```

則可以輸出：
```
idnex: Index(['a', 'b', 'c', 'd'], dtype='object')
values: [ 8  9 10 11]
```

所以如果我要取出8這個幸運數字該怎麼做呢？
```
my_obj2['a']
```
因為我們設定`'a'`為index，所以只需要`my_obj2['a']`就可以了，忘記的話趕快回去複習python的語法吧！pandas是基於python的程式庫，很多語法都是以python為基礎的。

複習一下：
[[Day03] Python的基本運算！（上）](https://ithelp.ithome.com.tw/articles/10192814)


### 查詢是否存在某個Index

如果想知道`a` index在不在my_obj2裡面我們可以:
```python
'a' in my_obj2
```
有的話，會回傳`True`否則`False`。

### Dictinary轉成Series
這就是前面所提到的最基本的一個Series格式，其實之前提到的dictionary也可以變成Series：
```python
dic_data = {'name':'apple','birthday':'1996-1-1','luckynumber':7 }
```
這裡我們先宣告一個dictinary，接著轉成Series：
```python
my_obj3 = pd.Series(dic_data)
```
輸出my_obj3：
```
birthday       1996-1-1
luckynumber           7
name              apple
dtype: object
```

### Series內部資料型態
再來我們來看看它內部的資料型態吧！宣告一組布林的陣列再把它變成Series
```python
registration = [True,False,True,True]
registration = pd.Series(registration)
registration
```
可以看到Out結果`dtype`為`bool`。

```python
dictionary = {'A':'an animal',
              'B':'a color',
              'C':'a fruit'}
dictionary = pd.Series(dictionary)
dictionary
```
可以看到Out的`dtype`為`object`：
```
0     True
1    False
2     True
3     True
dtype: bool
```

## 資料類型 - DataFrame
DataFrame就像是我們在使用的excel表格一樣，是一個二維的數據有`index`和`column`，可以透過index和column來找到我們要的某一筆資料。
我們先定義一個資料，裡面包含`name`、`year`、`month`、`day`，接著將它轉成dataframe的格式並顯示：
```python
data = {'name': ['Bob', 'Nancy','Amy','Elsa','Jack'],
        'year': [1996, 1997, 1997, 1996, 1997],
        'month': [8, 8, 7, 1, 12],
        'day':[11,23,8,3,11]}
myframe = pd.DataFrame(data)
myframe
```
上面我們定義了一組數據data，並用`.DataFrame()`將它轉成DataFrame。
DataFrame和Series一樣，若沒有特別定義index的話它會自動的分配。

name、year、month、day就是剛剛提到的columns，左邊的0到4就是index。

### 更改columns順序
假如我要讓day在month後面怎麼辦呢？
```python
myframe2 = pd.DataFrame(data,columns=['name','year', 'month', 'day'])
```
在函式內多一個columns的參數就可以了！

### 新增columns
現在我們來定義新的frame，並在最後column下多加一個column。
```python
myframe3 = pd.DataFrame(data,columns=['name','year', 'month', 'day','luckynumber'])
myframe3
```
就會看到`NaN`，因為我們並沒有給它資料。

現在我們來給它資料吧！先定一一組幸運數字的資料：
```python
luckynumber = ['3','2','1','7','8']
luckynumber = pd.Series(luckynumber)
```
接著把資料放到myframe3的luckynumber內：
```python
myframe3['luckynumber'] = luckynumber
```
就可以看到資料被填滿了！

以上就是兩種Pandas的資料結構，接下來幾篇會更深入的講解Pandas，敬請期待！


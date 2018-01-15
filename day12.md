# [Day12]Pandas處理字串資料！（上）

嗨，今天是比賽的第12天，也是2017的最後一天，跨年還要寫這個真的是難過。
那來說一下字串的資料是如何處理、可以如何處理吧！
這邊我會將處理字串分成上、下兩個部分說明。

上半部這篇，來說說一些在python內的處理字串方式，在pandas其實也可以使用哦！


**那就開始吧！** 

## Common String Method
來看看一般在python內的字串方法，包含`lower()`,`upper()`,`title()`和`len()`。

### lower() 
lower()讓字串全部變成小寫：
```python
"HELLO WORLD".lower() 
```
會得到 hello world

### upper() 
upper() 讓字串全部變成大寫：
```python
"hello world".upper() 
```
會得到 HELLO WORLD

### title() 
title() 讓字串第一個字為大寫：
```python
"hello world".title() 
```
會得到 Hello World

### len()
len() 得到字串長度
```python
len("hello world")
```
會得到 11

# Pandas Working Text Data

以上說明的這些都是python內的字串處理方法，相信大家應該不陌生，來看看Pandas是否也可以這樣用！
首先，先匯入資料：
```python
import pandas as pd
chicago = pd.read_csv("./csv/chicago.csv")
```
我們將使用`astype()`資料類型轉成`category`，這樣做為了減少記憶體使用的大小。
```python
chicago["Department"] = chicago["Department"].astype("category")
```
我們顯示前十筆資料：
![Imgur](https://i.imgur.com/YcSIPYR.png)

## title()
```python
chicago["Name"].title()
```
會發現得到錯誤：'Series' object has no attribute 'title'
![Imgur](https://i.imgur.com/WckSkMD.png)
因為Series裡面並沒有title這個方法，所以我們可以：
### .str
```python
chicago["Name"].str.title()
```
這樣就可以讓資料使用`title()`這個方法了。
![Imgur](https://i.imgur.com/9TD0Ztn.png)

可以來看一下它是什麼資料類型：
```python
type(chicago["Name"].str)
```
pandas.core.strings.StringMethods

接下來的方法也是一樣：
## lower()
```python
chicago["Name"].str.lower().head(3)
```

## upper()
```python
chicago["Name"].str.upper().head(3)
```

![Imgur](https://i.imgur.com/DD4aI4w.png)

## len()
```python
chicago["Department"].str.len().head()
```

## 更改資料
要更改資料很簡單：
```python
chicago["Position Title"] = chicago["Position Title"].str.title()
chicago.head()
```
可以看到資料從原本都為大寫變成只有單字開頭為大寫的title格式了：
![Imgur](https://i.imgur.com/gfgn1IH.png)

## replace()
今天的最後呢，來說說`replace()`這個方法！
這是python內就有的用法：
```python
"Hello world".replace("l","!")
```
會得到輸出 'He!!o wor!d'
這個方法呢是將（）括弧內前面"l"的取代為後面的"!"，現在來看看pandas怎麼做：

先匯入資料：
```python
chicago = pd.read_csv("csv/chicago.csv").dropna(how="all")
chicago["Department"] = chicago["Department"].astype("category")
chicago.head(3)
```
![Imgur](https://i.imgur.com/x9AOwxW.png)

來看看如何使用replace()：
```python
chicago["Department"] = chicago["Department"].str.replace("MGMNT","MANAGEMENT")
```
![Imgur](https://i.imgur.com/P8uznvc.png)

可以看到原本的 MGMNT 被取代成 MANAGEMENT 了！

## 總結
那上半部就到這邊結束了，今天說明了python的字串處理在pandas內不能直接使用，需要先`.str`轉資料類型
最後，祝大家新年快樂啊！希望明年可以繼續撐下去啊～～～～～～（吶喊）

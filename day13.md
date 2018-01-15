# [Day13]Pandas處理字串資料！（下）

上一篇說明了python的字串處理方式在pandas內是要如何使用的，今天我們要更深入一點講解其他操作字串資料的方法、函數。

之前的文章中我們有說明如何過濾資料，取出需要的資料，那在字串中又是如何處理的呢？
一樣，我們先import pandas，並且匯入csv檔案:
```python
chicago = pd.read_csv("csv/chicago.csv").dropna(how="all")
chicago["Department"] = chicago["Department"].astype("category")
chicago.tail(3)
```
`tail(3)`用來顯示最後三筆資料，會看到如下圖：
![Imgur](https://i.imgur.com/pYXCDQQ.png)

# .str.contains()
現在我們要在"Position Title"中取出有"water"這個字串該怎麼做呢？
我先會使用`str.lower()`將全部字串都先轉成小寫：
```python
chicago["Position Title"].str.lower()
```
接著用`.str.contains()`這個函數：
```python
.str.contains("water")
```
這個會產生一個布林的結果，顯示每個欄位是否包含"water"，如下圖：
![Imgur](https://i.imgur.com/yYB3Z6W.png)
包含的話會回傳True、否則False，接著就可以用之前講過的方式將資料取出了（mask）！

# .str.startswith()
接著來說明`startswith()`這個方法，它用來找出資料內是否開頭是括弧內的，
我們一樣會將它轉成小寫再使用：
```python
mask = chicago["Position Title"].str.lower().str.startswith("water")
chicago[mask].head() 
```
一樣，正確的話就會回傳True、否則False，我們把這個布林放入mask變數中來過濾資料，如圖：
![Imgur](https://i.imgur.com/e1gozBk.png)
可以看到所顯示的資料開頭都是"water"。

# .str.endswith()
有取出開頭的，當然也有找最後結尾的，那就是我們的`.endswith()`，它的用法和`.startswith()`一樣：
```python
mask = chicago["Position Title"].str.lower().str.endswith("ist")
chicago[mask].head()
```
如圖：
![Imgur](https://i.imgur.com/i6LhwvN.png)

# Split Strings by Characters
再來要說明重要的切割字元的重點部分了！
一樣，我們先匯入資料：
```python
chicago = pd.read_csv("csv/chicago.csv").dropna(how="all")
chicago["Department"] = chicago["Department"].astype("category")
chicago.tail(3)
```

先來看看在python內是怎麼切割字元的：
```python
"Hello my name is jiayi".split(" ")
```
會得到結果：
```
['Hello', 'my', 'name', 'is', 'jiayi']
```
在pandas中：
```python
chicago["Name"].str.split(",").head()
```
上面程式碼中我們依照","將資料分開，會看到結果：
```
0        [AARON,   ELVIA J]
1      [AARON,   JEFFERY M]
2         [AARON,   KARINA]
3    [AARON,   KIMBERLEI R]
4    [ABAD JR,   VICENTE M]
Name: Name, dtype: object
```
分開之後我們就可以像list一樣把內容分別取出來：
```python
chicago["Name"].str.split(",").str.get(0).str.title()
```
![Imgur](https://i.imgur.com/UYJaz57.png)

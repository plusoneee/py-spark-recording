# [Day09]Pandas索引的運用！

上一篇說明了運用不同的方式做資料的過濾，透過過濾不需要的資料進而取出我們所要的資料，
接下來要來嘗試索引（index）的更多使用的方法！

## 將column變成index
一樣，先引入pandas。
```python
import pandas as pd
```
一樣，使用`pd.read_csv()`引入csv檔，並顯示前五筆資料：
![Imgur](https://i.imgur.com/fNYqIt6.png)

這是一個電影的資料表，它的index為數字序列，現在我們要改變它的index內容：
```python
pd.read_csv("csv/jamesbond.csv",index_col="Film").head(2)
```
在`.read_csv()`中更改參數`index_col`可以將`column`設定成`index`，比較原本的和下面的看看哪裡不一樣吧！原本的數字不見了變成`"Film"`
![Imgur](https://i.imgur.com/lX3xrUp.png)

可以用`index`看看有哪些`index`
```python
bond.index
```
輸出：
```
Index(['Dr. No', 'From Russia with Love', 'Goldfinger', 'Thunderball',
       'Casino Royale', 'You Only Live Twice',
       'On Her Majesty's Secret Service', 'Diamonds Are Forever',
       'Live and Let Die', 'The Man with the Golden Gun',
       'The Spy Who Loved Me', 'Moonraker', 'For Your Eyes Only',
       'Never Say Never Again', 'Octopussy', 'A View to a Kill',
       'The Living Daylights', 'Licence to Kill', 'GoldenEye',
       'Tomorrow Never Dies', 'The World Is Not Enough', 'Die Another Day',
       'Casino Royale', 'Quantum of Solace', 'Skyfall', 'Spectre'],
      dtype='object', name='Film')
```

### set_index()
也可以使用`set_index()`
```python
boud.set_index("Film" , inplace=True)
```
我們將Film設定為我們的index，`inplace=True`要記得！

### reset_index()
`reset_index()`可以讓index重置成原本的樣子！(如圖)
```python
bond.reset_index(inplace=True)
```
![Imgur](https://i.imgur.com/6ZANKnW.png)

## loc[]
再來要介紹`loc[]`的方法，用index的標籤來取出資料。
```python
bond = pd.read_csv("csv/jamesbond.csv",index_col="Film")
```
先重新匯入資料，並將index設定為Film，若我們要取出Goldfinger這部的資料（第2 index)：
```python
bond.loc["Goldfinger"]
```
輸出：
```python
Year                         1964
Actor                Sean Connery
Director             Guy Hamilton
Box Office                  820.4
Budget                       18.6
Bond Actor Salary             3.2
Name: Goldfinger, dtype: object
```

當然，`loc[]`不止可以一次選取一個(row)：
```python
bond.loc[["Goldfinger","From Russia with Love"]]
```
將要的資料放到陣列內，就可以一次選取多個（row）資料了！

## iloc[]
再來介紹一個跟`loc[]`很像的方法：`iloc[]`，我們將資料重新匯入（避免被上面的干擾），
```python
bond = pd.read_csv("csv/jamesbond.csv")
bond.iloc[15]
```
`iloc[]`是用index位置來取我們要的資料。(如圖)
![Imgur](https://i.imgur.com/TTuGgOi.png)

若是我們要一次取多個（row）資料呢？
```python
bond.iloc[[0,4]]
bond.iloc[0:4]
```
看得出來上面兩個的差別嗎？一個是取0,4 index的資料，一個是取0到3。

當然，資料不一定index要是數字才可以用`iloc[]`！
我們將index設定為Film，再來用`iloc[]`：
```python
bond.iloc[0:4]
```
可以看到其實它也是照index位置去取出資料的，並**不是因為index是數字**!

### loc[]與iloc[]
接下來再來更深入的說明`loc[]`和`iloc[]`怎麼使用吧！
```python
bond.loc["From Russia with Love"]
```
上面這是取出`From Russia with Love`這部電影的資訊，若要知道他的`Actor`我們可以：
```python
bond.loc["From Russia with Love","Actor"]
```

和剛剛一次取兩個（row）的差別在：
```python
bond.loc[["Goldfinger","From Russia with Love"]]
```
#### 上面這是`[]`裡面再放一個list！

## rename()
再來我們來看一下要怎麼將`index`或是`columns`的名稱改變吧：
### rename(columns)
```python
bond = pd.read_csv("csv/jamesbond.csv",index_col="Film")
```
```python
bond.rename(columns={"Year":"Release Date","Box Office":"Revenue"},inplace=True)
```
用`rename()`這個方法，上述我們改變"Year"為"Release Date"，"Box Office"為"Revenue"
![Imgur](https://i.imgur.com/SXJPLIi.png)
### rename(index)
上面為改變`columns`，再來改變`index`：
```python
bond.rename(index={"Dr. No":"Doctor No",
                   "GoldenEye":"Golden Eye",
                   "The World Is Not Enough":"Best bond Movie Ever"},inplace=True)
```
![Imgur](https://i.imgur.com/kjdN1Cb.png)
可以看到圖片上名稱被改掉了！

## drop()
來看看如何刪除吧！
```python
bond.drop(labels=["Box Office","Actor"], axis="columns")
```
刪除直接使用`.drop()`，裡面放入要刪除的`labels`，設定`axis="columns"`
```python
bond.drop(labels=["Box Office","Actor"], axis=1)
```
`axis=1`跟`axis="columns"`是一樣的！`axis=0`則是和`asxis = "row"`一樣。

## 總結
繼上次講解了如何過濾資料，今天說明了索引的運用，像是換位置、取代、查找或刪除等等，相信對資料的整理已經有一定的概念跟瞭解了，下一篇，也就是第十天會說明Groupby的概念！

那就到這囉，感謝各位觀看（扭）！（應該是鞠躬才對啦！）


# [Day07]Pandas操作資料的函數！

嗨嗨！第七天了，上一篇提介紹了python內的一個套件pandas內兩個重要的資料結構，
可以到這邊回顧：
[[Day06]Pandas的兩種資料類型！](https://ithelp.ithome.com.tw/articles/10193394)

接下來要會介紹pandas內重要的函數，包含資料的顯示、新增、刪除與排序，那我們就開始吧！
**溫馨提醒** : 建議使用電腦做觀看，以下包含內容較小的圖片。


最最最開始一定要先`import pandas`
```python
import pandas as pd
```

## 檔案讀取
使用`read_csv()`讀取一個CSV的檔案
```python
df = pd.read_csv('./csv檔案位置')
```
使用`.head()`可以顯示5筆資料（預設是5筆）也可以自訂，只需要在括弧內加上要的數字：
```python
df.head(3)
```
要顯示最後五筆資料則可以使用`.tail()`，和`head()`一樣，可以在括號內加上要顯示幾筆資料：
```python
df.tail()
```

如下圖，匯入資料後分別顯示前五筆資料與最後三筆資料：
![Imgur](https://i.imgur.com/eOf70BA.png)

## 資料資訊
使用.info()可以看到該檔案的資訊：
```python
df.info()
```

![Imgur](https://i.imgur.com/9vJ0RPb.png)
可以看到上面顯示了有哪些columns、大小和資料類型等等。

#### .shap
要如何知道檔案的大小呢？使用`shape`。
```python
df.shape
```
就會顯示(rows,columns)
輸入：
```
df.shape
```
輸出：
```
(458, 9)
```

## 資料選擇
先來看一下我們的資料：
![Imgur](https://i.imgur.com/pGLhlBA.png)

### 選擇一項資料：
如上圖，我們選擇`Name`好了，要怎麼選呢？
```python
df['Name']
```

若只要選擇某幾筆資料則：
```python
df['Name'][0:4]
```
輸出：
```python
0    Avery Bradley
1      Jae Crowder
2     John Holland
3      R.J. Hunter
Name: Name, dtype: object
```
在上面這一行程式碼內會先挑出Name這個column內所有資料，[0:4]則是我們之前在python語法內所提過的，會從第0筆選到小於4的資料。

### 選擇多項資料：
選擇多項資料也非常得簡單，只需要把要選擇的資料用`list的資料格式`就可以了！
```python
df[['Name','Team']]
```

## 資料新增：
上一篇的最後我有提到怎麼新增column並加上資料，不過這邊還有另外一個方式可以新增，就是`insert()`
```python
df.insert(3,column="sport",value="Basketball")
```
來解釋一下上面這個函式在做什麼吧，新增一個叫`sport`的column在`第三個`位置，裡面的值是"Basketball"，如圖：
![Imgur](https://i.imgur.com/0DRbj1P.png)

## 資料刪除：
知道如何新增資料之後，來看看如何`刪掉資料`吧！很多時候我們所得到的資料不一定是完全都有數值的很可能含有NaN，這時候就需要把它給刪除。

我們先讀取檔案
```python
nba = pd.read_csv("csv/nba.csv")
```
有一個叫做`dropna()`的函式可以幫我們`刪除NaN`的資料！
```python
nba.dropna()
```
記得把它存到一個變數，不然它是不會改變的哦！
```python
nba = nba.dropna()
```

如下圖，其實可以看到在上圖有NaN的資料內容，執行`dropna()`後，可以看到它不見了。
（或是可以看到幾個index不見了！）
![Imgur](https://i.imgur.com/fSbgchh.png)

## 空白資料填充
若我們不打算刪除空的資料，我們還有一個方法可以做就是把NaN的資料代換掉。
```python
nba = nba.fillna(0)
```
使用fillna()函式，在括弧中填入自己想要填入的值，在上面的程式中我們把它換成0。

## 資料排序
除了前面介紹的新增刪除修改外，當然可以做資料的排序！
```python
nba.sort_values("Name")
```
在上面的程式中，我想`排序Name`的資料，只需要在資料後面加上`.sort_values()`並在括弧內加上要排序的column，如下圖：
![Imgur](https://i.imgur.com/zZdvL4i.png)

若你在括弧內使用shift加上tab可以看到有哪些參數可以使用，其中有一項ascending預設為True，我們改成False試試看：
```python
nba.sort_values("Name",ascending= False)
```

可以發現它順序反過來了！
![Imgur](https://i.imgur.com/QyN6VCc.png)

## 總結
我們今天說明了如何用pandas操作資料的函數！
包含資料顯示、資料新增、資料刪除、資料取代以及資料排序。

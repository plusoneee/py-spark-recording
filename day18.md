# [Day18]Numpy檔案輸入與輸出！

嗨，今天來到第18天了！
今天來說說檔案的輸入與輸出吧，在Pandas中我們講過如何讀取檔案，在Numpy也能夠將資料輸出或輸入，今天來說明`Binary`格式和一般`text`檔案的輸入與輸出吧！

回顧其他天Numpy的文章：
* [[Day14]Numpy的ndarray！](https://ithelp.ithome.com.tw/articles/10195434)
* [[Day 15]Numpy操作索引＆局部資料！](https://ithelp.ithome.com.tw/articles/10195645)
* [[Day16]Numpy的廣播&方法！](https://ithelp.ithome.com.tw/articles/10195830)
* [[Day18]Numpy檔案輸入與輸出！](https://ithelp.ithome.com.tw/articles/10196167)

# Binary Format
先建立一筆資料：
```python
x = np.arange(10)
```
# save()
接著儲存：
```python
np.save('my_array', x)
```
這樣就完成了！接著就可以回Jupyter目錄看看是否有多出一個`my_array.npy`的檔案。

# load()
接下來我們將剛剛儲存的資料載入：
```python
np.load('my_array.npy')
```
這邊的話請記得加上`.npy`，不然可能會找到其他的檔案去了喔！
![Imgur](https://i.imgur.com/6Pc21cF.png)

這就是save和load的概念了，有沒有非常的簡單呢？

# savez()
我們可以儲存多個陣列在一個`zip`的檔案中，使用`np.savez`就可以了！
首先，我們先建立兩個陣列：
```python
aData = [1,2,3,4,5,6]
bData = [7,8,9,10,11,12]
```
使用`np.savez()`
```python
np.savez('my_archive.npz', a=aData, b=bData)
```
在參數裡面，宣告`a = aData`和`b = bData`，並且存成`my_archive.npz`檔案。

若要使用zip檔案的資料只需要跟剛剛一樣使用`load()`：
```python
myArch = np.load('my_archive.npz')
```
這樣檔案內的資料就在`myArch`內了，現在要分別取出`aData`以及`bData`只需要：
```python
myArch['b']
```
和
```python
myArch['a']
```
![Imgur](https://i.imgur.com/jBypzZu.png)

# Text Files
我們在之前都有用Pandas來做到讀取檔案（像是`read_csv`）並且進行資料操作，現在來看看Numpy怎麼做吧！

在這裡我先建立一個txt檔案放入資料，在Jupyter內可以用`!cat`查看內容（跟在終端機的`cat`一樣）：
```python
!cat my_txt.txt
```
![Imgur](https://i.imgur.com/Gl2D0yo.png)
# load
在Numpy內會使用`.loadtxt`或特定的`np.genfromtxt`來讀取它：
```python
myArr = np.loadtxt('my_txt.txt', delimiter=',')
```
我們使用`np.loadtxt()`，裡面的參數放入txt的檔案，`delimiter=','`則是設定分隔的符號！
可以看到下面這張圖，我們透過分隔將資料變成一個2維的陣列：
![Imgur](https://i.imgur.com/Wl39ZXU.png)

# savetxt 
要將資料反向存成另外一個`txt`檔案只需要：
```python
np.savetxt('txtfile.txt', myArr)
```
上面的程式碼，我們將剛剛`load`出來的`myArr`再存成一個`txt`檔案，並且名稱為`txtfile.txt`。
好了之後可以回到Jupyter目錄，會看的到`txtfile.txt`這個檔案，將檔案打開：
![Imgur](https://i.imgur.com/soj2z54.png)

就可以看到它裡面先前我所建立的資料了！


## 總結：
我們可以運用Numpy中的檔案操作去輸出或輸入檔案，例如像是npy或是zip，當然我們也可以匯出或匯入成一般的文字檔，只需要一行的程式碼，是不是超級方便！

想看更多的可以到：
[numpy.savez](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.savez_compressed.html)
[numpy.savetxt](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.savetxt.html)
[numpy.genfromtxt](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.genfromtxt.html)



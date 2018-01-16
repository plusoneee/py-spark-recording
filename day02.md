#[Day02]Jupyter Notebook操作介紹！

第二天了！
昨天介紹了如何安裝`Anconda`，因為接下來我都會使用**Jupyiter notebook**做程式編寫，還沒有安裝好環境的話趕快看一下上一篇 [[Day01]Anaconda環境安裝！](https://ithelp.ithome.com.tw/articles/10192460)！
那就開始介紹**Jupyiter notebook**是什麼吧！

**Jupyiter notebook**是用來編寫python程式碼的*（但現在已經支持其他語言了喔！）*
Jupyiter有很多項優點，其中一項就是可以在內部寫`Markdown語法`，不需要在另外用一份文檔說明程式碼或是寫很多的註解來說明程式碼，且支持輸出成其他文件格式，所以我們可以使用一個ipynb(Jupyiter notebook檔案)就能完成這兩件事情！
需要其他語言（例如R），只需要安裝特定的kernal就可以了。

### nbviewer
Jupyiter notebook在GitHub上可以直接顯示，或是你可以上使用[nbviewer](http://nbviewer.jupyter.org)分享。
![Imgur](https://i.imgur.com/XL2C8BY.png)

## 開啟Jupyter的大門吧！

還記得上一次我們在虛擬環境內也安裝jupyter，現在只需要在虛擬環境內輸入:
```
$ jupyter notebook
```

就會自動跳出頁面了！**（若沒有請到localhost:8888)**
在終端機上會看到下面這樣的畫面表示成功安裝了。
![Imgur](https://i.imgur.com/PQM1UM7.png)

上面的` http://localhost:8888/?token=21(略）` 是可以直接使用它貼到網頁上做登入。
*** Jupyter內預設是`8888 port *** 。

### 更改Jupyter port！

如果8888port已經使用中了，或是想更改它成自己想要的只需要後面加上 `--port 9999`（9999可以改成任何你想要的port)，像這樣：
```
$ jupyter notebook --port 9999
```

可以看到最下面已經改變port號變成9999了！
![Imgur](https://i.imgur.com/PQM1UM7.png)

### Jupyter的token！

假如太久沒有使用它（也未把服務關掉），在打開網頁的時候會出現`要求輸入token`，這時候就貼上後面那串在jupyter上就好囉！
![Imgur](https://i.imgur.com/7fEnRYP.png)
畫面上也有提示你，如果要查看token就在終端機輸入：
```
$ jupyter notebook list 
```

若還沒有安裝的話先進入虛擬環境： 
```
$ source activate my_it30days 
```

進入後，下安裝指令：
```
$ conda install jupyter
```

若習慣使用`pip`安裝的話，也是把conda改成pip就可以了。
```
$ pip install --upgrade pip
$ pip install jupyter
```

在虛擬環境下，我們先建立一個叫做 jupyter_notebook的目錄：
```
$ mkdir jupyter_notebook
$ cd jupyter_notebook
```
接著在這個jupyter_notebook目錄下執行jupyter	 
```
$ jupyter notebook 
```
會看到裡面是空的完全沒有東西，因為我們是在剛剛新增的目錄下做執行，在哪裡執行jupyter notebook就會從哪個目錄開始當根目錄（home）。
![Imgur](https://i.imgur.com/0fovxPL.png)

## 執行第一個ipynb檔

新增檔案在右上角的 `New`點選後有`python3`，我們可以點選它並建立一個python3的kernel的jupyter notebook，若你要其他的kernel可以自行安裝，這裡我們先點選`python3`。
![Imgur](https://i.imgur.com/8LfGMBV.png)

點選`python3`之後就會跳到一個頁面就是jupyter的畫面，點選Untitled可以更改檔案的名稱，你可以改成任何你想要的名稱，這裡我會改名叫`01_hello_python`。
![Imgur](https://i.imgur.com/4xDpLUn.png)

接著按左上角`Jupyter標題`回到剛剛的目錄，在Files標籤內會看到剛剛建立的01_hello_python檔案，`綠色`表示它正在執行。
![Imgur](https://i.imgur.com/PsY79Br.png)

那就來使用它吧，點進去檔案跳到剛剛的頁面會看到一個一個的cell，我們開始輸入一些簡單的語法吧，
輸入
```python
a = 0
b = 1
a + b
```
輸入完後在cell上按`Run Cells`，就會看到Out出現1：
![Imgur](https://i.imgur.com/aTbofBe.png)

這裡也有一個快捷鍵方式按 `shift + enter` 會自動執行目前正在選取的cell，不知道有沒有發現當你點選一個cell的旁邊的線條會變成`綠色`，
這時候就可以做`編寫`的動作，接著按下`ESC`會看到變成`藍色`就可以做其他“動作”而不會是輸入指令。

#### 在cell旁邊為藍色時
* 按下`x`：刪除當前選擇的cell
* 按下`a`：在當前選擇的上方新增一個cell
* 按下`b`：在當前選擇的下方新增一個cell
* 按下`Shift-Enter`：執行當前的cell並且選到下一個cell
* 按下`Ctrl-Enter`：執行當前cell
* 按下`M`：轉成markerdown模式，可以看到紅色框框內容從code變成markerdown
想看更多[Jupyter 快捷鍵](http://opus.konghy.cn/ipynb/jupyter-notebook-keyboard-shortcut.html)


下圖為code模式：
![Imgur](https://i.imgur.com/nBykLOh.png)

轉成markdown：
![Imgur](https://i.imgur.com/VI6DbA8.png)

總結一下，今天我們瞭解了Jupyter notebook的優點、如何使用它還有它的快捷鍵操作，再來會繼續使用它做更多資料分析介紹，明天我會說明需要的python語法觀念！

更多資訊：
[Jupyter document]( https://jupyter.readthedocs.io/en/latest/content-quickstart.html)
[Jupyter 快捷鍵](http://opus.konghy.cn/ipynb/jupyter-notebook-keyboard-shortcut.html)

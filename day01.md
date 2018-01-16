
# [Day01]Anaconda環境安裝！
Python是一個強大快速且易讀的程式語言，裡面包含非常多的套件可以使用，在資料分析裡除了用R語言，可以使用python作為開發工具！
可以在[python官網](https://www.python.org/downloads/)下載。

在這裡我選擇使用Anaconda，它特點便是它已經包含了各種的科學數學和數據分析的套件是專門用於數據分析用途。

### 那就開始吧！
到[Anaconda](https://www.anaconda.com/download/)下載，選擇python3的版本。

### conda是什麼？
如果慣用`pip`的人對於`conda`的指令一定也可以馬上上手，因為它和`pip指令`非常非常的相似，`Conda`是套件管理系統，也可用來建立虛擬環境，不過因為`Anaconda`本身專注於數據分析，所以我們會使用到的像是`pandas`、`Numpy`、`Scipy`的python package在安裝完成時就已經包含在裡面不需要另外安裝了哦！

### 使用Anaconda做package的管理
#### 1.安裝package：
```
conda install packageName
```
將packageName換成你想要的任何套件像是：
```
$ conda install pandas
```
#### 2.若要移除package：
```
$ conda remove packeName
```
若想知道目前電腦內安裝了哪些套件只需要下`conda list`指令

另外，若要安裝特定版本的python：
```
$ conda install python=3.5
```

### Anaconda虛擬環境管理
使用虛擬環境來開發可以避免版本衝突。
將envName換成你所要的名稱：
```
$ conda create -n envName
```
這邊我創建了一個`my_it30days`的虛擬環境，後面的jupyter是我想在裡面就事先安裝好的package，你可以在名稱後面加上自己想要的package。
```
$ conda create -n my_it30days jupyter
```
下指令之後會看到：
```
Package plan for installation in environment 你的路徑/anaconda3/envs/my_it30days:

The following NEW packages will be INSTALLED: 

…(省略)
Proceed ([y]/n)?
```
輸入y，接著就等待它把整個環境安裝起來吧！
![Imgur](https://i.imgur.com/tRM2N4Z.png)


建立後可以看到它很貼心的有指示：
```
To activate this environment, use:
source activate my_it30days
To deactivate an active environment, use:
source deactivate
```

#### 進入環境便：
```
$ source activate envName
```
這裡我輸入：
```
$ source activate my_it30days
```
會看到你的名稱前面會多了（my_it30days）表示已經進入到虛擬環境。

下`python`指令看是否有python環境。
```
$ python
```
輸入conda list查看內部的所有的package
```
conda list
```
![Imgur](https://i.imgur.com/t0XOLeM.png)

#### 退出虛擬環境：
```
$ source deactivate 
```

#### 看有哪些虛擬環境：
```
$ conda env list
```
會出現你現有的虛擬環境，星號部分代表你目前正在使用的，若不在虛擬環境則星號會在root旁邊。

#### 若要刪除虛擬環境：
```
conda env remove -n envName
```
這樣環境的安裝介紹就到這裡了！
接下來我會用`jupyter notebook`作為`python`編寫工具，並運用做更多資料分析介紹。



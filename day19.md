# [Day19]Matplotlib讓資料視覺化！

前幾天說明完了`Pandas`跟`Numpy`現在就來說說怎麼讓資料視覺化吧！

> 一張圖畫勝過千言萬語

這也是為什麼要做視覺化，視覺化是為了理解數據的變化過程，透過一堆數字我們無法直接看出結果，但透過圖形、圖表資料的呈現，就可以讓人明確的知道資料的走向和結果。

# Import matplotlib
首先我們先 import ：
```python
import matplotlib.pyplot as plt
```
# Create data
```python
years = [1000,1500,1600,1700,1750,1800,1850,
        1900,1950,1960,1965,1970,1975,1980,
        1985,1990,1995,2000,2005,
        2010,2015]

pops = [200,400,458,580,662,791,1000,
        1262,1650,2525,2758,3018,3322,3682,
        4061,4440,4853,5310,6520,
        6930,7349]
```
# plt.plot()
使用`plt.plot()`，將years,pops資料內容放到函數內：
```python
plt.plot(years,pops)
```
# plt.show()
接著要將圖表顯示出來：
```python
plt.show()
```
![Imgur](https://i.imgur.com/4kTRKiR.png)

## change color
要怎麼改變線條的顏色呢？
只需要在`plt.plot()`內加入一個`color`參數：
```python
plt.plot(years,pops,color=(255/255,100/255,100/255))
```
![Imgur](https://i.imgur.com/pOVoVd5.png)

# label
會基本的將圖型顯示出來之後，可以新增`label`，我們來寫個人口成長的圖表(資料純屬虛構)：
先給資料：
```python
years = [1950,1960,1965,1970,1975,1980,
        1985,1990,1995,2000,2005,
        2010,2015]
pops = [2.5,2.7,3,3.3,3.6,4.0,
        4.4,4.8,5.3,6.1,6.5,6.9,7.3]
```
設定`label`：
```python
plt.title("Population Growth") # title
plt.ylabel("Population in billions") # y label
plt.xlabel("Population growth by year") # x label
```
在上面我們新增了title：Population Growth，
y座標：Population in billions
x座標：Population growth by year
顯示：
```python
plt.show()
```
![Imgur](https://i.imgur.com/9IlM3TE.png)

# Multilines
上面我們顯示了人口成長的圖表，假設我們想再加上死亡率：
新增一筆資料：
```pyhton
deaths = [1.2,1.7,1.8,2.2,2.5,2.7,2.9,3,3.1,3.2,3.5,3.6,4]
```
修改`plt.plot()`的部分：
```
plt.plot(years,pops, color=(255/255,100/255,100/255))
plt.plot(years,deaths, '--', color=(100/255,100/255,255/255))
```
可以看到`'--'`部分，這個是顯示顯條的樣子。

給予label：
```python
plt.title("Population Growth") # title
plt.ylabel("Population in billions") # y label
plt.xlabel("Population growth by year") # x label
```

顯示資料：
```python
plt.show()
```
![Imgur](https://i.imgur.com/X8tbx3o.png)

OK!這樣就完成了兩條線的圖表了，要繼續增加只需要新增`plt.plot()`就可以了。
或者：
```python
lines = plt.plot(years,pops,years,deaths)
```
我們可以將它們寫在一起，都是一樣的！

# Configure graph
能夠顯示多筆資料了，接下來看看圖型可以有哪些設置吧！
先用一樣的資料：
```python
years = [1950,1960,1965,1970,1975,1980,
        1985,1990,1995,2000,2005,
        2010,2015]
pops = [2.5,2.7,3,3.3,3.6,4.0,
        4.4,4.8,5.3,6.1,6.5,6.9,7.3]
deaths = [1.2,1.7,1.8,2.2,2.5,2.7,2.9,3,3.1,3.2,3.5,3.6,4]

lines = plt.plot(years,pops,years,deaths)
```

## plt.grid()
`grid()`用來顯示網格：
```
plt.grid(True)
```
![Imgur](https://i.imgur.com/RaAib54.png)

可以看到它後面多了網格！

## plt.setp()
接下來我們來設定線的`mark`：
資料我們使用剛剛設定的：
```python
years = [1950,1960,1965,1970,1975,1980,
        1985,1990,1995,2000,2005,
        2010,2015]
pops = [2.5,2.7,3,3.3,3.6,4.0,
        4.4,4.8,5.3,6.1,6.5,6.9,7.3]
deaths = [1.2,1.7,1.8,2.2,2.5,2.7,2.9,3,3.1,3.2,3.5,3.6,4]
lines = plt.plot(years,pops,years,deaths)
```
在這裡我們將要繪的線都放到`lines`這個變數內，再來就可以用`plt.setp()`了：
```python
plt.setp(lines,marker = "o") 
```
上面我們先放入參數`lines`，就是我們剛剛存放的變數`lines`，
`color = `ㄧ樣可以設定資料顏色，不過這邊我不另外設定，
`marker = "o"`，設定點點的樣式。
`linewidth =`可以設定線的粗細，不過這邊我不另外設定。
執行結果：
![Imgur](https://i.imgur.com/RU9EIcK.png)

## With Numpy：

此篇的最後我們結合`Numpy`來繪出兩個不同速率的`sin`波形吧：
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 1.0, 0.01)
y1 = np.sin(4*np.pi*x)
y2 = np.sin(2*np.pi*x)
lines = plt.plot(x, y1, x, y2)
l1, l2 = lines
plt.setp(lines, linestyle='--')      
plt.show()
```
![Imgur](https://i.imgur.com/5Tcae62.png)

參考資料來源：
[matplotlib.org](https://matplotlib.org/devdocs/api/pyplot_summary.html)

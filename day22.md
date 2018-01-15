# [Day22]Bokeh更簡單的資料視覺化！

嗨嗨，來到第22天了！

今天要說明的是python中一個叫`Bokeh`的套件，在前面所提到的都是讓圖以靜態的方式呈現，而`Bokeh`則可以讓圖表呈現動態的樣子，像是可以用滑鼠拖曳或縮放！

首先，先import：
```python
from bokeh.plotting import figure, show
```

# Scatter plot
定義繪圖板寬高：
```python
p = figure(plot_width=500, plot_height=500)
```
定義資料：
```python
x = [1,2,3,4,5,6,7,8,9,10,11]
y = [6,3,7,2,4,6,1,2,3,5,6]
```
將資料放到圖上並顯示：
```python
p.circle(x, y, size=20, color="gray", alpha=0.6)
show(p)
```
![Imgur](https://i.imgur.com/qT7wBbV.png)

# Single Lines
定義繪圖板寬高：
```python
p = figure(plot_width=500, plot_height=500)
```
定義資料：
```python
x = [1,2,3,4,5,6,7,8,9,10,11]
y = [6,3,4,2,5,2,5,1,3,5,4]
```
唯一的差別是`line()`：
```python
p.line(x, y, line_width=3)
show(p)
```
![Imgur](https://i.imgur.com/pUHY8zf.png)

# Multiple Lines
定義繪圖板寬高：
```python
p = figure(plot_width=500, plot_height=500)
```
定義資料：
```python
x1 = [1, 2, 3]
x2 = [2, 3, 4, 5, 6]
y1 = [3, 2, 5]
y2 = [3, 2, 4, 1, 3]
```
使用`multi_line()`：
```python
p.multi_line([x1,x2] , [y1, y2],
             color=["firebrick", "navy"], alpha=[0.8, 0.3], line_width=5)
show(p)
```
![Imgur](https://i.imgur.com/a3Uno6z.png)

# Bars
使用`vbar`：
```python
p = figure(plot_width=500, plot_height=500)
p.vbar(x=[1, 2, 3, 4], width=0.5, bottom=0,
       top=[1.2, 2.5, 3.7, 2.9], color="black",alpha=0.4)
show(p)
```
![Imgur](https://i.imgur.com/Bl7ILdn.png)

# Multiple Patches
使用`patches`
```python
p = figure(plot_width=500, plot_height=500)
x1 = [1, 4, 5, 2]
x2 = [3, 4, 5, 6]
x3 = [1,3,2]
y1 = [2, 3, 5, 6]
y2 = [4, 7, 7, 5]
y3 = [7,8,5.5]
p.patches([x1,x2,x3 ], [y1,y2,y3],
          color=["black", "navy","firebrick"], alpha=[0.2, 0.2,0.3], line_width=2)

show(p)
```
![Imgur](https://i.imgur.com/rrVC3K0.png)

那這就是基本的使用`Bokeh`繪圖了！

參考資料：
[bokeh.pydata.org](https://bokeh.pydata.org/en/latest/docs/user_guide.html)



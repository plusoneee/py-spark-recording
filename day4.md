#[Day04]Python的基本運算！（下）


在上一篇，說明了python各個數據類型的使用函式，接下來我會介紹流程控制以及迴圈應用，有流程控制我們可以讓程式加入判斷，決定要執行哪些程式碼！
如果想看上一篇python基本運算可以到：
[[Day03] Python的基本運算！（上）](https://ithelp.ithome.com.tw/articles/10192814)

那我們就開始啦！

## 布林值
在上一篇所講的`整數`、`字串`等等都包含了無限種可能得數值，但是**布林只有兩個數值** `成立(True)`或`不成立(False)`。 注意開頭是大寫喔！
```python
mybool = True
print(mybool)
```

### 比較運算子
```
== 等於
!= 不等於 
> 大於
< 小於
>= 大於等於
<= 小於等於
```
會依據比較的結果是否成立而產生`True`或`False`的結果。

輸入：
```python
print('1',8 == 8)
print('2',8 != 8)
print('3',2 < 0)
print('4',2 <= 2)
print('5','hello' == 'hello')
print('6','hello'== 'Hello')
```

輸出：
```
1 True
2 False
3 False
4 True
5 True
6 False
```


### 布林運算子
and、or、not三個布林運算子是用來比較布林值的，回傳的值也是`True`或`False`。

* and: 兩者都成立才為true
* or: 其中一個成立就為true
* not: 反向

輸入：
```python
print('1',True and True)
print('2',True and False)
print('3',True or False)
print('4',False or False)
print('5',not True)
print('6',not False)
```

輸出：
```python
1 True
2 False
3 True
4 False
5 False
6 True
```


### 混合使用
因為兩個輸出都為布林值，因此可以一起使用，讓我們來看看怎麼一起使用吧:
```
(4 > 5) and (1 == 1)
```
會得到輸出False
以上運算子的運用對接下來的**流程控制**非常重要，所以請務必一定要搞懂哦！那接下來我們繼續來看流程控制吧！

## 流程控制
上面提到的布林我們可以當作是條件，條件會有一個布林值（True、False），流程控制就是運用它來當條件判斷的。
我們在前一篇也提到了python的縮排方式規則，流程控制內沒有括弧存在，請務必要記得縮排！

### if else
```python
name = 'apple'
if name == 'apple':
    print('hello apple')
else:
    print('you are not apple')
```
在上面這個例子中我們可以看到在一個if下面接著else，這是所謂的if陳述句，
如果A成立則執行冒號：下面的程式，否則執行else冒號下面的程式。


### if elif else
```python
name = 'apple'
if name == 'banana':
    print('hello banana')
elif name == 'apple':
    print('hello apple')
elif name == 'pinapple':
    print('hello pinapple')
else:
    print('you are not apple')
```
上面這個例子裡面，可以看到中間多了elif提供了更多條件判斷，但只有前面不成立才會繼續檢查。

## while 迴圈陳述句
可以使用while讓程式區塊不斷的執行，當while內的條件成立就會執行區塊內的程式碼。

分別執行看看以下的程式碼吧：
```python
count = 0
while count < 5:
    print(count)
    count = count +1
```
再來將while換成if：
```python
count = 0
if count < 5:
    print(count)
    count = count +1
```
可以發現while執行了五次而if只有執行一次，while會在每次迭代時前先檢查是否成立，若成立則執行。搭配上面的運算子練習寫看看吧！

### 陷入無窮迴圈？
想看看執行下面的程式會如何？
```python
while True:
    print('hello!')
```
迴圈會永遠成立會一直印'hello!'，所以使用的時候請小心啊！

### for 迴圈
我們可以在for迴圈內放入range()函式，當程式的起始、停止與進步數，來看看例子吧：
```python
for i in range(3,5):
    print(i)
```
上面這個會從3開始印到小於5的數字，所以會印出3,4

```python
for i in range(3,9,2):
    print(i)
```
那這個呢？最後面的2是指一次加的數量，這個會輸出3到小於9的數但每次都+2，所以是3,5,7。

## 函式
接下來就到python基本語法的最後一部分了！前面提到的很多像是`print()`、`input()`的都是所謂的函式，現在我們也來自己寫函式吧！

```python
def my_first_func():
    print('Call this function!')
my_first_func()
```
def 後面加上函式的名稱，在上面我們將我們的函式取名叫做`my_first_func`（記得縮排）接著我們在程式區塊外呼叫它。

輸出：
```
Call this function!
```

## 總結
最後結合上面的流程控制迴圈與函式，我們來寫一個小型的程式吧！猜數字遊戲！
```python
import random
scrnum = random.randint(1,10)
print('guess a number between 1 and 10')
for geuss_num in range(1,7):
    print('guess!')
    guess = int(input())
    if guess < scrnum:
        print('too low')
    elif guess > scrnum:
        print('too high')
    else:
        print('good job!')
        break
```
今天我們講解了運算子的使用並結合回圈，最後說明了函式，並且結合之前的完成一個簡單的小程式，懂了python的運算後接下來就要進行到資料分析的部分了啊！準備好了嗎！

**更多關於此主題的文章**
[[Day01]Anaconda環境安裝！](https://ithelp.ithome.com.tw/articles/10192460)
[[Day02]Jupyter Notebook操作介紹！](https://ithelp.ithome.com.tw/articles/10192614)
[[Day03]Python的基本運算！（上）](https://ithelp.ithome.com.tw/articles/10192814)
[[Day05]聊聊重要的三個package吧！](https://ithelp.ithome.com.tw/articles/10193295)
[[Day06]Pandas的兩種資料類型！](https://ithelp.ithome.com.tw/articles/10193394)
[[Day07]Pandas操作資料的函數！](https://ithelp.ithome.com.tw/articles/10193421)

更多資訊：
[Python tutorial-深入 Python 流程控制](http://www.pythondoc.com/pythontutorial3/controlflow.html)



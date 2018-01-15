#[Day03]Python的基本運算！（上）
在上一篇瞭解了jupyter notebook的操作使用，這一篇跟下一篇會用來說明python的基本語法，使用Jupyter notebook。


如果沒有**Anaconda**的話可以到：
[[Day01]Anaconda環境安裝！](https://ithelp.ithome.com.tw/articles/10192460)
想知道什麼是**Jupyter Notebook**可以到：
[[Day02]Jupyter Notebook操作介紹](https://ithelp.ithome.com.tw/articles/10192614)

## Python特點？
為什麼用python？對我來說主要是好學習，語法很簡單，同樣是印出hello world：

這是**Java**
```java
public class Main {
  public static void main(String[] args) {
     System.out.println("hello world");
   }
}
```
而這是**python**
```python
print(‘hello world’)
```
也因此開啟了我的python學習之路，但python的速度並不快，這是它的缺點！

## python的不同

python和其他程式語言不同的是python是用縮排排列並不需要括弧{}，這也是python的特點之一，是缺點還是優點就見仁見智啦！

下面這程式碼這是一般使用{}的語法。
```
for x in array {
    print(x)
}
```

而這是python的格式，一般來說會使用4個space或是tab。
```python
array = [1,2,3,4]
for x in array:
    print(x)
```
**請注意！若沒有縮排將會出現錯誤啊！**

## Hellow World
請在cell內輸入
```python
print('hellow world')
```
就可以看到out輸出hellow world了！

## 註解
python要下註解只需要在前面加上#
```python
#註解掉不會執行
print('hello ')
```

## 多行註解
```python
'''
多行註解
多行註解
多行註解
多行註解
'''
```

## 用戶輸入input()
```python
user_input = input()
```

範例輸入：
```python
user_input = input()
print("input text:",user_input)
```

執行會出現對話筐輸入`hello world`會看到下面輸出：
```
hello world
input text: hello world
```

> input()不管輸入什麼都是返回字串哦 這點要注意！


## 匯入模組import
使用import匯入需要的模組，通常我們會寫在程式的最上方。
```python
import time
print(time.localtime())
```


## 執行python檔案
要執行一個python的檔案只需要在終端機輸入 
```bash
$ python my_python_file.py
```


## jupyter內呼叫python檔案

若是要在jupyter內呼叫python的檔案呢？
```bash
%run -i 目錄/my_python_file.py
```

提示：在選擇目錄的時候可以按一下`tab`鍵，會出現提示！

## 變數宣告
在python的變數宣告中不需要特別宣告變數的類型。
```python
my_number = 10 
my_float = 1111.1 # 浮點數
my_name = "apple" # 字串
print(my_number,my_float,my_name)
```

## Python數據類型
以下五種是python的數據類型
* Number 數字
* String 字串
* boolean 布林
* List 列表
* Tuple 元組
* Dictionary 字典

這邊當作大家對number和string已經有基本的認知，接下來我會針對 List 與 Dictionary 做說明。
若想對number有更多的瞭解可以到：
[Python Number|菜鳥教程](http://www.runoob.com/python/python-numbers.html)
若想對string有更多的瞭解可以到：
[Python String|菜鳥教程](http://www.runoob.com/python/python-strings.html)
裡面有詳細的說明！


## Python List列表
list列表內可以放入很多數據類型當然包含列表，表示方法為：
```python
list_data = [1,'string',3.1,[5,6,7]]
print(list_data)
```

```python
print list_data               # 輸出完整的list
print list_data[0]            # 輸出第一個元素
print list_data[1:3]          # 輸出第二個到第三個個元素 
print list_data[1:]           # 輸出第二個到最後一個元素
```

若list為以下格式，要怎麼取出10這個數字呢？
```python
list_data = [1,'string',3.1,[5,6,7],[8,9,10]]
```
list_data內總共有0到4，而數字10則是在第4個index內的第2個元素，我們可以：
```python
print(list_data[4][2])
```

就可以看到輸出為0了！

### List中的index()方法
在list中有一個`index()`的方法，若搜尋的值存在在list中，就會返回索引位置給我們。
```python
list_data = [1,'string',3.1,[5,6,7],[8,9,10]]
index = list_data.index('string')
print(index)
```

會得到輸出1，因為'string字串在第1個。'

### Append()和Insert()方法
想要在list中加入新的值可以使用`append()`和`insert()`

```python
mylist = ['cat','dog','bird']
mylist.append('mouse')
print(mylist)
```

輸出：
```
['cat', 'dog', 'bird', 'mouse']
```

`append()`會將新加入的值放在最後一個，`insert()`中前面的值是所要插入的索引位置：
```python
mylist2 = ['cat','dog','bird']
mylist2.insert(1,'mouse')
print(mylist2)
```

輸出：
```
['cat', 'mouse', 'dog', 'bird']
```

**這樣有理解到兩個的差別了嗎？雖然都是新增元素但還是不一樣的喔！**

### Remove()方法
使用`remove()`可以做資料的刪除：
```python
mylist3 = ['cat','dog','bird']
mylist3.remove(1)
print(mylist3)
```

輸出：
```
['cat', 'bird']
```

### Sort()方法進行排序
數值或是字串都可以用sort()排序：
```python
mylist4 = ['cat','dog','bird']
mylist4.sort()
```

輸出：
```
['bird', 'cat', 'dog']
```

或是數字排序：
```python
mylist5 = [3,5,6,3,8,9]
mylist5.sort()
mylist5
```

輸出：
```
[3, 3, 5, 6, 8, 9]
```


## Python Dictionary字典
dictionary是python內最靈活的數據類型，它不像list有順序，字典是通過關鍵字來存取資料，和list用[]來包資料不同，dictionary是用{}。
```python
my_dic =  {
'name': 'apple','country':'taiwan', 'luckynumber': 8
}

```

### 取得資料
```python
my_dic['country'] 
my_dic['name']
my_dic['luckynumber']
```

輸出：
```
taiwan apple 8
```

### 列出關鍵字
要列出關鍵字可以用`.key()`
```python
my_dic.keys()
```

輸出：
```python
dict_keys(['name', 'country', 'luckynumber'])
```

### 列出內容（數值）
要列出value可以用`.value()`
```pyhton
my_dic.values()
```
輸出：
```python
dict_values(['apple', 'taiwan', 8])
```

## 數值轉換
### str( ) 函式
若想連接整數和字串則需要先將整數轉成字串才行！
```python
a = 8
s_str = str(a)
print(s_str+' Is my lucky number')
```
會得到輸出：8 Is my lucky number
```
8 Is my lucky number
```

### int()函式
則是將傳入的數值變成整數
```python
a = str(3)
print(a)
b = int(a)
print(b)
```

### float() 函式
便是將傳入的數值轉成浮點數啦，自己試試看吧！

> 若要將整數或浮點數與字串做連接，則可以用str()轉成字串。若要將字串進行運算則可以用int()、float()的函式。

## 總結
今天我們學會`匯入檔案`還有`執行檔案`以及各個數據類型的使用函式，在處理字串的觀念在之後分析資料會常常運用到，在下一篇將會繼續介紹更多的python的語法！

更多資訊：
[Why Python Is the Best Programming Language With Which to Learn](https://www.huffingtonpost.com/entry/why-python-is-the-best-programming-language-with-which_us_59ef8f62e4b04809c05011b9)





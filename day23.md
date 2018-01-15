# [Day23]Beautiful Soup網頁解析！

哈囉！今天是鐵人賽的第23天！
今天要來說明`Beautiful Soup`這個Python的套件！

> Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work.

什麼是Beautiful Soup？簡單來說它是用來抓取資料（像是HTML或是XML）的工具，你可以用自己習慣的解析程序（parser）在短時間來做到爬資料的工作！


**那就開始吧！**

# HTML
在這邊我們先定義ㄧ個html類型的檔案：
```html
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
```

# bs4
import bs4：
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
```
上面這邊我們是使用`html.parser`這個python的解析程序

## prettify()
用`prettify()`函數將soup這個物件美化，soup就是的html_doc解析的結果，最後`print`將它印出來：
```python
print(soup.prettify())
```
美化後的結果：
![Imgur](https://i.imgur.com/KoCvRk9.png)

# navigate that data structure
接下來我們要開始解析結構了，看一下在html中有<title>標籤，要如何看標籤裡的內容？
```python
soup.title
```
會得到結果：
```html
<title>The Dormouse's story</title>
```

取得`head`：
```python
soup.head
```
會得到
```html
<head><title>The Dormouse's story</title></head>
```
可以看到內部還有一層<title>，我們也可以這樣取出title：
```python
soup.head.title
```

若只想取字串內容：
```python
soup.title.string
```
結果：
```
"The Dormouse's story"
```

# find_all()
找出所有<p>的標籤：
```python
soup.find_all('p')
```
結果：
```html
[<p class="title"><b>The Dormouse's story</b></p>,
 <p class="story">Once upon a time there were three little sisters; and their names were
 <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
 <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
 <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
 and they lived at the bottom of a well.</p>,
 <p class="story">...</p>]
```

# get()
找出所有超連結`a`的標籤，可以看到`a`標籤中有一`href`屬性，用`get()`就可以取到它的連結位置：
```python
for link in soup.find_all('a'):
    print(link.get('href'))
```
結果：
```
http://example.com/elsie
http://example.com/lacie
http://example.com/tillie
```
所以要找出所有<p>標籤內的class名稱，只要：
```python
for className in soup.find_all('p'):
    print(className.get('class'))
```
結果：
```
['title']
['story']
['story']
```

# find(id)
依照`id`去取資料：
```python
soup.find(id="link3")
```
結果：
```html
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
```

# get_text()
取出文字內容：
```python
print(soup.get_text())
```
結果：
```
The Dormouse's story
The Dormouse's story
Once upon a time there were three little sisters; and their names were
Elsie,
Lacie and
Tillie;
and they lived at the bottom of a well.
...
```

OK，以上就是Beautiful Soup的基本操作方法！
我所介紹的都是依照官方文件上的範例做講解的，
若有興趣可以到[Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)看更多它如何使用的相關說明以及使用！



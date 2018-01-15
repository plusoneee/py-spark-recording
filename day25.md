# [Day25]機器學習：特徵與標籤！

嗨，今天是第25天，昨天開始介紹了何謂機器學習，機器學習有哪些類型，
今天我們說明機器學習內的名詞：`特徵(features)`與`標籤(labels)`，未來也會用這個說法。

上一次說明了什麼是機器學習：
簡單來說就是讓機器學習透過觀察分辨特徵來分類。


# 特徵與標籤
現在我們將簡單的用`特徵`與`標籤`來介紹機器學習的原理！

現在來說明什麼是特徵吧，假設要讓機器分辨`橘子`或是`蘋果`該怎麼區分？
你可能會覺得用`顏色`分辨！
這是一個非常好的答案，但假設我們得到的照片是黑白照片我們要如何分辨？

# 範例

來看下面這個例子：

重量 | 表面 | 標籤
------------- | ------------- | ------------- 
150g | 皺 | 橘子
170g | 皺 | 橘子
130g | 平滑 | 蘋果
140g | 平滑 | 蘋果
... | ... | ...|

利用`重量`跟`表面`來當我們訓練的資料，而`重量`跟`表面`的資料就是我們所謂的`特徵`，
而`標籤`就是定義這些特徵的結果是哪一種水果，也就是我們透過機器學習想讓電腦告訴我們的答案。

## 轉換符號

接下來將上面的字改成電腦看得懂的二元數字：`0`或`1`

重量 | 表面 | 標籤
------------- | ------------- | ------------- 
150g | 1 | 0
170g | 1 | 0
130g | 0 | 1
140g | 0 | 1

像上面這樣，我們將`皺`用`1`表示、平滑用`0`表示。橘子用`0`、蘋果用`1`，用這種資料格式餵給電腦可以讓電腦容易理解。

# Sklearn
有了資料之後，我們就可以用`Sklearn`來做機器學習了，來看看如何使用：

我們會用到簡單的二元樹分類，所以先`import`
```import
from sklearn import tree 
```

## 特徵定義：
透過上面的表格我們可以這樣寫：
```python
features = [[150,1],[170,1],[130,0],[140,0]]
```

## 標籤定義：
透過上面的表格我們可以這樣寫：
```python
labels = [0,0,1,1]
```

## DecisionTreeClassifier
建立一個DecisionTreeClassifier二元樹分類：
```python
clf = tree.DecisionTreeClassifier()
```
上面這邊我們參數使用預設的，當然，你可以參考：[sklearn.tree.DecisionTreeClassifier](http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)自行修改。

放入資料到分類模型內：
```python
clf = clf.fit(features,labels)
```

## 預測：
假設我們重量`120g`表面為`平滑`是什麼水果？
```python
wantPredict = clf.predict([[120,0]]) 
if wantPredict == [1]:
    print('This is an apple')
elif wantPredict == [0]:
    print('This is an orange')
```
會得到結果：This is an apple。
![Imgur](https://i.imgur.com/HPh0q6v.png)

好的！那這個就是機器學習特徵與標籤的概念，是不是非常簡單呢！

## 總結
今天介紹了什麼是`特徵`與`標籤`的概念，我們用簡單的範例做說明，也簡單介紹了`Sklearn`是如何快速的幫助我們做分類的動作，接下來我們將用`Sklearn`介紹更多的機器學習分類的範例！

更多參考資料：
[sklearn.tree.DecisionTreeClassifier](http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)



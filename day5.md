# [Day05]聊聊重要的三個package吧！

今天，這個美好的平安夜來聊聊python數據分析的三個又重要又基本的package吧！

如果想知道python的語法可以到之前的文章：
[[Day03] Python的基本運算！（上）](https://ithelp.ithome.com.tw/articles/10192814)
[[Day04] Python的基本運算！（下）](https://ithelp.ithome.com.tw/articles/10193001)


## 數據分析的第一步！

開啟數據分析的大門，學會了Python也有了數據分析需要的環境了，就可以開始進入數據分析的部分了啊（激動！）要使用python做數據分析，其實現有很多很好用的package可以讓我們輕易的上手，網路上也有很多豐富的資源。

### 所以說有哪些重要的package？
* Pandas 
* Numpy
* Matplotlib

Pandas、Numpy與Matplotlib構成了資料科學的強大基礎，蹲馬步要練穩，才可以打十個啊！未來也會依照這個順序一項一項的做更多介紹以及使用方法，當然少不了介紹`Scipy`這個重要的package，不過最主要的還是上述的三個，而我們之前安裝的`Anaconda`中就已經含有這幾個重要的python程式庫了請放心！

## Pandas是什麼？
Pandas是一個基於numpy的package（不是什麼很多隻熊貓啦！），在處理數據方面非常的好用和簡單，透過標籤和索引，Pandas讓我們可以非常輕易的處理數據，pandas
在學習pandas之前我們要先知道pandas的兩種特有的資料結構DataFrame與Series，很快就會直接介紹怎麼用pandas了！


## Numpy是什麼？

> NumPy‘s array type augments the Python language with an efficient data structure useful for numerical work, e.g., manipulating matrices. NumPy also provides basic numerical routines, such as tools for finding eigenvectors.

Numpy是一個提供矩陣運算非常非常非常好用的工具，雖然python處理大量資料時有list可以讓我們做到似矩陣的功能但list效能表現並不理想，而Numpy具備平行處理的能力，可以將操作動作一次套用在大型陣列上，幫助我們做更多方法建立多維數據以及矩陣運算，像是Pandas就是建立在Numpy的基礎延伸的套件呢！



## Matplotlib是什麼？

> The matplotlib module produces high quality plots. With it you can turn your data or your models into figures for presentations or articles. No need to do the numerical work in one program, save the data, and plot it with another program.

假設你做了好了資料分析要怎麼讓大家可以一目瞭然呢？這時候就需要用到它了！（登冷！）
Matplotlib是Python繪圖的它包含了大量的工具，你可以使用這些工具創建各種圖形，包括簡單的散點圖、直方圖，甚至是三維圖形，將你的資料轉成圖表，在python的數據分析中會經常使用Matplotlib完成數據可視化的工作！

## SciPy是什麼？

> SciPy contains additional routines needed in scientific work: for example, routines for computing integrals numerically, solving differential equations, optimization, and sparse matrices.

我們說pandas用來整理數據表格，Numpy是以矩陣基礎做數據的數學運算，SciPy就是以Numpy為基礎做科學、工程的運算處理的package，包含統計、優化、整合、線性代數、傅立葉轉換圖像等較高階的科學運算。

接下來會深入做更多的介紹，以及如何用這些套件做數據分析的實作，那就下一篇見！


更多資訊：
[Getting Started - SciPy.org](https://scipy.org/getting-started.html)
[Pandas tutorials](http://pandas.pydata.org/pandas-docs/stable/tutorials.html)


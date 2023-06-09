# Python 基礎教學
## 介紹
這個項目是為想要學習 Python 編程語言的初學者準備的。我們提供了一些基本的概念和練習，幫助你快速掌握 Python 的基礎知識。

利用一些有趣的應用題
在這個項目中，我們提供了以下有趣的應用題，幫助你更好地掌握 Python 編程語言。

### 一、生日問題 (Birthday Paradox)
生日問題是指最少需要幾人，當中兩人同生日的機率才會過半。答案是23人，所以30人的小學班級中兩人同生日的機率更高。對於60人或更多人，機率大於99%。這問題有時也稱生日悖論，但從引起邏輯矛盾的角度來說生日問題並非悖論，它稱作悖論只因這事實與一般直覺相牴觸而已。大多數人會認為23人中兩人同生日的機率應該遠小於一半。計算與此相關的機率稱為生日問題，在這個問題之後的數學理論已用於設計著名的密碼攻擊方法：生日攻擊。

![Birthday Paradox](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Birthday_Paradox.svg/1280px-Birthday_Paradox.svg.png)


```bash=
pip install -r requirements.txt
python Birthday_Paradox.py
```


### 二、凱撒密碼 (Caesar Cipher)
在這個數位時代，網絡安全已經成為了一個日益重要的問題。想要保護自己的隱私，學習密碼學技術已經成為了不可或缺的一部分。而凱撒密碼作為最古老也最基本的加密技術之一，是入門學習密碼學的最佳選擇。本文將詳細介紹凱撒密碼的原理與使用方法，讓你輕鬆掌握基本的加密技術，開啟你的網絡安全之旅。

![Caesar Cipher](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Caesar_cipher_left_shift_of_3.svg/1280px-Caesar_cipher_left_shift_of_3.svg.png)

```bash=
python Caesar_Cipher.py
```

#### 簡單測試功能是否正確 Unit Test Caesar Cipher
```bash=
python Caesar_Cipher_Test.py
```

### 三、終極密碼 (Ultimate Code)
有聽過始祖破冰團體遊戲「終極密碼」嗎？那就來挑戰一下使用Python還原經典的終極遊戲吧！在這個遊戲中，你需要利用直覺和邏輯來猜出對手的秘密數字，並且不斷調整猜測範圍，讓對手束手無策。挑戰極限，看看你是否能成為猜密碼遊戲的大師！

```bash=
python Ultimate_Code.py
```

### 四、猜數字 (1A2B)
挑戰你的謎底猜測技能！經典猜數字遊戲，讓你在線上與朋友一決高下。你可以通過直覺和邏輯逐漸逼近謎底，每次猜測後根據提示調整策略。這個遊戲需要你動腦筋，提高數字辨識能力，讓你愉快地度過休閒時光。來挑戰一下吧！

![Bulls and Cows](https://upload.wikimedia.org/wikipedia/commons/d/d4/4digits_0.4_screenshot.png)

```bash=
python 1A1B.py
```


### 五、設計函式解決問題 (Time_Complexity_Experience)
1 + 2 - 3 + 4 - 5 + 6 - ... + / - N ，當 N =314159265358979

```bash=
python Time_Complexity_Experience.py
```

#### 簡單測試功能是否正確 Unit Test Caesar Cipher
```bash=
python Time_Complexity_Experience_Test.py
```


### 六、抽卡問題
KDD721這款手機遊戲結合了抽卡與計算機技能，為玩家帶來了前所未有的刺激體驗。在這個遊戲中，玩家可以通過抽卡來獲取不同等級的卡片，進而學習和提升各種計算機技能，例如基礎Python、資料庫管理、網頁設計等等。透過這些技能的提升，玩家可以不斷地挑戰遊戲中的各種關卡，最終達到終點並獲得勝利。

以下是各個等級的卡片與對應的計算機技能舉例：

|卡片等級|卡片名稱|卡片名稱|卡片名稱|卡片名稱|卡片名稱|卡片名稱|卡片名稱|
|  :-:  |  :-:  |  :-:  |  :-:  |  :-:  |  :-:  |  :-:  |  :-:  |
|UR     |精通人工智慧|
|SSR    |熟悉雲端技術|
|SR     |熟練資料結構與演算法|熟練機器學習|
|R      |掌握資料庫管理|掌握通訊協定|掌握作業系統原理|
|N      |了解電腦組裝|文件編輯排版|網路基礎認知|資訊安全基礎|基礎Python|基礎C++|基礎Java|



請寫出一個程式可以「隨機」的抽取「不重複」的卡片，且： \
● UR  抽中的機率為 3%  \
● SSR 抽中的機率為 7%  \
● SR  抽中的機率為 20% \
● R   抽中的機率為 30% \
● N   抽中的機率為 40% 

所以，顯示結果的範例：（這裡只是示意，目的是避免大家花時間在在理解題目上面）

本次活動所有卡片為：

[精通人工智慧 , 熟悉雲端技術 , 熟練資料結構與演算法 , 熟練機器學習 , 掌握資料庫管理 , 掌握通訊協定 , 掌握作業系統原理 , 了解電腦組裝 , 文件編輯排版, 網路基礎認知, 資訊安全基礎, 基礎Python, 基礎C++, 基礎Java]

抽到 UR 卡片目前尚未抽取的獎勵為：

[熟悉雲端技術, 熟練資料結構與演算法 , 熟練機器學習 , 掌握資料庫管理 , 掌握通訊協定 , 掌握作業系統原理 , 了解電腦組裝 , 文件編輯排版, 網路基礎認知, 資訊安全基礎, 基礎Python, 基礎C++, 基礎Java]
 
抽到 SR 卡片目前尚未抽取的獎勵為：

[熟悉雲端技術, 熟練機器學習 , 掌握資料庫管理 , 掌握通訊協定 , 掌握作業系統原理 , 了解電腦組裝 , 文件編輯排版, 網路基礎認知, 資訊安全基礎, 基礎Python, 基礎C++, 基礎Java]  

抽到 SR 卡片目前尚未抽取的獎勵為：

[熟悉雲端技術, 掌握資料庫管理 , 掌握通訊協定 , 掌握作業系統原理 , 了解電腦組裝 , 文件編輯排版, 網路基礎認知, 資訊安全基礎, 基礎Python, 基礎C++, 基礎Java]
  .
  .
  .
直到抽到卡片箱內沒有卡片為止

```=bash
python Kdd_Game.py
```



## Anaconda安裝

### 步驟 1：下載 Anaconda
![Anaconda](https://lennychen.com/wp-content/uploads/2022/02/%E4%B8%8B%E8%BC%89-1.png)

#### 首先，你需要從 Anaconda 的官方網站下載適合你電腦作業系統的版本。在下載頁面上，你可以看到兩個不同的版本：Anaconda 和 Miniconda。Anaconda 是一個全面的Python發行版，包括了數據科學和機器學習的相關包，而Miniconda則是一個更輕量的發行版，只包含了最基本的工具。在這裡，我們選擇下載 Anaconda，若是要使用在嵌入式系統建議安裝Miniconda。

### 步驟 2：安裝 Anaconda

#### 下載完 Anaconda 安裝程式後，你可以按照下面的步驟進行安裝：

##### 1.開啟 Anaconda 安裝程式。
##### 2.選擇你要安裝的語言，點選「Next」。
##### 3.閱讀使用協議，接受後點選「Next」。
##### 4.選擇你要安裝的安裝路徑，點選「Next」。建議使用預設路徑。

![Anaconda_path](https://docs.anaconda.com/_images/win-install-destination.png)


##### 5.選擇你要安裝的用戶，點選「Next」。建議使用預設用戶。
##### 6.選擇你要安裝的組件，點選「Next」。如果你不確定，建議使用預設組件。

##### 7.選擇你要安裝的開始菜單項目，點選「Next」。

##### 8.安裝開始，點選「Install」(兩個都勾選)。
![Anaconda_options](https://docs.anaconda.com/_images/win-install-options.png)

##### 9.安裝完成後，點選「Next」。
![Anaconda_next](https://docs.anaconda.com/_images/win-install-options.png)
##### 10.建議勾選「Learn more about Anaconda Cloud」和「Learn how to get started with Anaconda」，然後點選「Finish」。
![Anaconda_next](https://docs.anaconda.com/_images/win-install-complete.png)
### 步驟 3：使用 Anaconda

#### 1.安裝完成後，你可以開始使用 Anaconda 中的 Python 環境和工具了。你可以在終端機中輸入以下命令啟動 Anaconda Navigator：

```=bash
anaconda-navigator
```
![Anaconda_start](https://docs.anaconda.com/_images/nav-tabs.png)


#### 2.如果你需要安裝其他 Python 套件，可以使用 Anaconda 中的 conda 命令進行安裝。例如，如果你想要安裝 numpy 套件，可以在終端機中輸入以下命令：

```=bash
conda install numpy
```

#### 3.創建和管理環境
#### 【使用GUI】Anaconda 允許你創建多個環境，以便在不同的專案中使用不同的 Python 版本和套件。在「Anaconda Navigator」中，你可以透過「Environments」選項卡創建和管理環境。
#### 點選「Create」按鈕，輸入新環境的名稱，並從下拉式選單中選擇要使用的 Python 版本。接下來，你可以透過「Add」按鈕向環境中添加套件。

#### 【使用Terminal】如果你想從終端機中管理環境，可以使用 conda 命令。例如，要創建一個名為 myenv 的環境，可以在終端機中輸入以下命令：

```=bash
conda create --name 虛擬環境名稱
# or
conda create -n 虛擬環境名稱
```
#### 4.要啟動此環境，可以在終端機中輸入以下命令：

```=bash
conda activate 虛擬環境名稱
```

##### 若使用GUI如下

![Anaconda_start_GUI](https://docs.anaconda.com/_images/nav-env.png)


#### 5.要退出環境，可以在終端機中輸入以下命令：

```=bash
conda deactivate 虛擬環境名稱
```

## 常見問題解答
### 待更新

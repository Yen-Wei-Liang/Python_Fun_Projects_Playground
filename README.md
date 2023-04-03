# Python 基礎教學
## 介紹
這個項目是為想要學習 Python 編程語言的初學者準備的。我們提供了一些基本的概念和練習，幫助你快速掌握 Python 的基礎知識。

利用一些有趣的應用題
在這個項目中，我們提供了以下有趣的應用題，幫助你更好地掌握 Python 編程語言。

### 一、生日問題 (Birthday Paradox)
生日問題是指最少需要幾人，當中兩人同生日的機率才會過半。答案是23人，所以30人的小學班級中兩人同生日的機率更高。對於60人或更多人，機率大於99%。這問題有時也稱生日悖論，但從引起邏輯矛盾的角度來說生日問題並非悖論，它稱作悖論只因這事實與一般直覺相牴觸而已。大多數人會認為23人中兩人同生日的機率應該遠小於一半。計算與此相關的機率稱為生日問題，在這個問題之後的數學理論已用於設計著名的密碼攻擊方法：生日攻擊。

```bash=
python Birthday_Paradox.py
```


### 二、凱撒密碼 (Caesar Cipher)
在這個數位時代，網絡安全已經成為了一個日益重要的問題。想要保護自己的隱私，學習密碼學技術已經成為了不可或缺的一部分。而凱撒密碼作為最古老也最基本的加密技術之一，是入門學習密碼學的最佳選擇。本文將詳細介紹凱撒密碼的原理與使用方法，讓你輕鬆掌握基本的加密技術，開啟你的網絡安全之旅。

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

### 四、猜數字 (1A1B)
挑戰你的謎底猜測技能！經典猜數字遊戲，讓你在線上與朋友一決高下。你可以通過直覺和邏輯逐漸逼近謎底，每次猜測後根據提示調整策略。這個遊戲需要你動腦筋，提高數字辨識能力，讓你愉快地度過休閒時光。來挑戰一下吧！

```bash=
python 1A1B.py
```


## Anaconda安裝

### 步驟 1：下載 Anaconda
![Anaconda](data:image/png;base64,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)
首先，你需要從 Anaconda 的官方網站下載適合你電腦作業系統的版本。在下載頁面上，你可以看到兩個不同的版本：Anaconda 和 Miniconda。Anaconda 是一個全面的Python發行版，包括了數據科學和機器學習的相關包，而Miniconda則是一個更輕量的發行版，只包含了最基本的工具。在這裡，我們選擇下載 Anaconda，若是要使用在嵌入式系統建議安裝Miniconda。

### 步驟 2：安裝 Anaconda

#### 下載完 Anaconda 安裝程式後，你可以按照下面的步驟進行安裝：

##### 1.開啟 Anaconda 安裝程式。

##### 2.選擇你要安裝的語言，點選「Next」。

##### 3.閱讀使用協議，接受後點選「Next」。

##### 4.選擇你要安裝的安裝路徑，點選「Next」。建議使用預設路徑。

##### 5.選擇你要安裝的用戶，點選「Next」。建議使用預設用戶。

##### 6.選擇你要安裝的組件，點選「Next」。如果你不確定，建議使用預設組件。

##### 7.選擇你要安裝的開始菜單項目，點選「Next」。

##### 8.安裝開始，點選「Install」。

##### 9.安裝完成後，點選「Next」。

##### 10.建議勾選「Learn more about Anaconda Cloud」和「Learn how to get started with Anaconda」，然後點選「Finish」。

### 步驟 3：使用 Anaconda

#### 安裝完成後，你可以開始使用 Anaconda 中的 Python 環境和工具了。你可以在終端機中輸入以下命令啟動 Anaconda Navigator：

```=bash
anaconda-navigator
```

#### 如果你需要安裝其他 Python 套件，可以使用 Anaconda 中的 conda 命令進行安裝。例如，如果你想要安裝 numpy 套件，可以在終端機中輸入以下命令：

```=bash
conda install numpy
```

#### 創建和管理環境
#### 【使用ＧＵＩ】Anaconda 允許你創建多個環境，以便在不同的專案中使用不同的 Python 版本和套件。在「Anaconda Navigator」中，你可以透過「Environments」選項卡創建和管理環境。
#### 點選「Create」按鈕，輸入新環境的名稱，並從下拉式選單中選擇要使用的 Python 版本。接下來，你可以透過「Add」按鈕向環境中添加套件。

#### 【使用Terminal】如果你想從終端機中管理環境，可以使用 conda 命令。例如，要創建一個名為 myenv 的環境，可以在終端機中輸入以下命令：

```=bash
conda create --name 虛擬環境名稱
# or
conda create -n 虛擬環境名稱
```
#### 要啟動此環境，可以在終端機中輸入以下命令：

```=bash
conda activate 虛擬環境名稱
```

#### 要退出環境，可以在終端機中輸入以下命令：

```=bash
conda deactivate 虛擬環境名稱
```

## 常見問題解答
### 待更新

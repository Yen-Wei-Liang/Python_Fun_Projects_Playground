#===============================================================
# Lab     : Kdd 721
# Name    : Yen-Wei-Liang
# function: Ultimate Code
#===============================================================

import random

print("歡迎來到終極密碼遊戲！")
print("我們將隨機選擇一個數字，請猜測這個數字是多少。")
print("猜測的數字必須介於 1 到 100 之間。")
    
# 隨機選擇一個數字當作密碼
secret_number = random.randint(1, 100)

while True:
    guess = int(input("請輸入你的猜測："))
        
    if guess == secret_number:
        print("恭喜你猜對了！")
        break
        
    elif guess < secret_number:
        print("你的猜測太低了！")
            
    else:
        print("你的猜測太高了！")
    
print("遊戲結束")
#===============================================================
# Lab     : Kdd 721
# Name    : Yen-Wei-Liang
# function: 1A1B
#===============================================================


import random

element = [0,1,2,3,4,5,6,7,8,9]
question = random.sample(element, 4)

print ("答案：",question,"測試使用","\n")  #觀察隨機亂數使用

print("=======================猜數字遊戲=======================")
print("遊戲規則：A為數字與位置皆猜對，B為數字猜對但位置猜錯","\n")
print("遊戲開始：請猜4個不重複的數字")
print("=======================================================")


while 1:
    error = 0
    user_answer = input("請輸入4個不同的數字：　")
    


#===============================================================
#防呆1：輸入字數不同
#===============================================================    
    if len(user_answer) != 4:
        print("輸入字數不同，請重新輸入")
        continue

#===============================================================
#防呆2：輸入重複數字
#===============================================================

    for k in range(4):
        if user_answer[k] in user_answer[k+1:4]:                
            print("輸入重複數字，請重新輸入")
            error = 1
            break
        
    if error==1:
        continue



    answer=[]
    count_A=0
    count_B=0

#===============================================================
#將輸入插入list中順便比對位置計算出A的數量
#===============================================================    
        
    for i in range(4):
        answer.append(int(user_answer[i]))
        if question[i] == answer[i]:
           count_A+=1 
    #print (count_A)  觀察使用
        
        
#===============================================================
#使用 in 指令 計算出B的數量會將A重複計算故要刪扣掉 (B-A)
#===============================================================    
    
    for j in range(4):
        if answer[j] in question:
            count_B+=1
    #print(count_B)   觀察使用
    
    
    print(count_A,"A",count_B-count_A,"B")

#===============================================================
#終止條件  4A  4B   (因為B有額外做加工使用原始data)
#===============================================================    

    if count_A == 4 & count_B == 4:
        print("恭喜你答對囉~~~~")
        break
#===============================================================
# Lab     : Kdd 721
# Name    : Yen-Wei-Liang
# function: Time_Complexity_Experience
#===============================================================

# 1 + 2 - 3 + 4 - 5 + 6 - ... + / - N ，當 N =314159265358979
# 1 例外先移除(最後在加回來)
# 觀察知偶數都是+的、奇數都是-的
# 假設一組(偶數 + 奇數 = -1 ) 
# 答案 = -(組別數量) + 1
# 組別數計算 N//2 or (N-1)/2

class Time_Complexity_Experience:
    def Time_Complexity (self, n):
        if n % 2 == 1:
            Group_Num = (n-1) // 2
            Answer = 1 - Group_Num
            return Answer
        else:
            Group_Num = (n-1) // 2
            Answer = 1 - Group_Num
            return Answer + n
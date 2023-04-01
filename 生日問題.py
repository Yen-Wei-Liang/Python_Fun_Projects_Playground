import datetime, random
from tqdm import tqdm

def Get_Birthdays(Number):
    """
    主要用來設定班上每位小朋友的生日
    """
    BIRTHDAYS = []
    for i in range(Number):
        This_Year = datetime.date(2023, 1, 1)
        Random_Birthday = datetime.timedelta(random.randint(0, 364))
        Birthday = This_Year + Random_Birthday
        BIRTHDAYS.append(Birthday)
    return BIRTHDAYS



def Repeat_Comparison(BIRTHDAYS):
    """
    主要用來比對是否班上有人同一天生日
    """
    if len(BIRTHDAYS) == len(set(BIRTHDAYS)):
        return None
    
    for Num1, Birthday1 in enumerate(BIRTHDAYS):
        for Num2, Birthday2 in enumerate(BIRTHDAYS[a + 1 :]):
            if Birthday1 == Birthday2:
                return Birthday1 
            
            
MONTHS = ('1 月', '2 月', '3 月', '4 月', '5 月', '6 月',
          '7 月', '8 月', '9 月', '10 月', '11 月', '12 月')


Number = int(input('班上有幾位同學?(隨機生成生日個數)：'))

BIRTHDAYS = Get_Birthdays(Number)
for num1, Birthday in enumerate(BIRTHDAYS):
    Month = MONTHS[Birthday.month - 1]
    Generate_Birthday = str(num1+1) + '.'+' {} {}'.format(Month, Birthday.day)
    print(Generate_Birthday, end='\n')
    
Match = Repeat_Comparison(BIRTHDAYS)


Number_Of_Experiments = input ("為計算成功的機率預想實驗幾次?")
print('班上有'+ str(Number) +'位同學' ,'隨實驗'+ Number_Of_Experiments +'次')
Match_Number = 0  

for num1 in tqdm (range(int(Number_Of_Experiments))):
    BIRTHDAYS = Get_Birthdays(Number)
    if Repeat_Comparison(BIRTHDAYS) != None:
        Match_Number = Match_Number + 1


probability = round(Match_Number / int(Number_Of_Experiments)  * 100, 2)

print('執行了'+Number_Of_Experiments+'次實驗'+'班上有兩人同一天生日的機率為'+str(probability)+'%')


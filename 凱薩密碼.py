#===============================================================
# Lab     : Kdd 721
# Name    : Yen-Wei-Liang
# function: Cryptography with Caesar Cipher
#===============================================================

while True:  
    try:
        KEY = int(input("請輸入要使用的密鑰(0-25)："))
        MODEL = input("請選擇模式，加密請輸入e，解密請輸入d：")
    
        if  0 <= KEY < 26 and MODEL == 'e':
            break
        elif  0 <= KEY < 26 and MODEL == 'd':
            break
        else:
            print("輸入密鑰或是模式有誤，請重新輸入!")
            
    except ValueError:
        print("輸入密鑰或是模式有誤，請重新輸入!")
        
MESSAGE = input("請輸入明文或密文：")

if   MODEL == 'e':
    CIPHER=""
    for num in MESSAGE:
        if (64 <int(ord(num)+KEY) < 91) or (96 < int(ord(num)+KEY) < 122):
            CIPHER += chr(ord(num)+KEY)
        elif num == ' ':
            CIPHER += " "
        else:
            CIPHER += chr(ord(num)+KEY-26)
    print("加密完成！密文：",CIPHER)
    
elif MODEL == 'd':
    PLAINTEXT=""
    for num in MESSAGE:
        if (64 < int(ord(num)-KEY) < 91) or (96 < int(ord(num)-KEY) < 122):
            PLAINTEXT += chr(ord(num)-KEY)
        elif num == ' ':
            PLAINTEXT += " "
        else:
            PLAINTEXT += chr(ord(num)-KEY+26)  
    print("解密完成！明文：",PLAINTEXT)
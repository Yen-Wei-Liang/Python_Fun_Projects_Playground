#===============================================================
# Lab     : Kdd 721
# Name    : Yen-Wei-Liang
# function: Cryptography with Caesar Cipher
#===============================================================

class Caesar_Cipher:
    
    def encrypt(self,MESSAGE,KEY):
        CIPHER=""
        for num in MESSAGE:
            if (96 < int(ord(num)+KEY) < 123) and num.islower():
                CIPHER += chr(ord(num)+KEY)
            elif (64 <int(ord(num)+KEY) < 91) and num.isupper():
                CIPHER += chr(ord(num)+KEY)
            elif num == ' ':
                CIPHER += " "
            else:
                CIPHER += chr(ord(num)+KEY-26)
        return CIPHER


    def decrypt(self,MESSAGE,KEY):
        PLAINTEXT=""
        for num in MESSAGE:
            if (96 < int(ord(num)-KEY) < 123) and num.islower():
                PLAINTEXT += chr(ord(num)-KEY)            
            elif (64 < int(ord(num)-KEY) < 91) and num.isupper():
                PLAINTEXT += chr(ord(num)-KEY)        
            elif num == ' ':
                PLAINTEXT += " "
            else:
                PLAINTEXT += chr(ord(num)-KEY+26)   
        return PLAINTEXT


#=================================================================
# 使用凱薩加解密，可以解除下面註解，註解只是為了方便 unit test。
#=================================================================
#while True:  
#    try:
#        KEY = int(input("請輸入要使用的密鑰(0-25)："))
#        MODEL = input("請選擇模式，加密請輸入e，解密請輸入d：")
#    
#        if  0 <= KEY < 26 and MODEL == 'e':
#            break
#        elif  0 <= KEY < 26 and MODEL == 'd':
#            break
#        else:
#            print("輸入密鑰或是模式有誤，請重新輸入!")
#            
#    except ValueError:
#        print("輸入密鑰或是模式有誤，請重新輸入!")
#        
#MESSAGE = input("請輸入明文或密文：")
#
#CaesarCipher = CaesarCipher()
#
#if   MODEL == 'e':
#    result = CaesarCipher.encrypt(MESSAGE,KEY)
#    print("加密完成！密文：",result)
#elif MODEL == 'd':
#    result = CaesarCipher.decrypt(MESSAGE,KEY)   
#    print("解密完成！明文：",result)
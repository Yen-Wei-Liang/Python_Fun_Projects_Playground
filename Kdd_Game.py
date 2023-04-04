import random

Cards = ['精通人工智慧', '熟悉雲端技術', '熟練資料結構與演算法', '熟練機器學習', '掌握資料庫管理', '掌握通訊協定', '掌握作業系統原理', '了解電腦組裝', '文件編輯排版', '網路基礎認知', '資訊安全基礎', '基礎Python', '基礎C++', '基礎Java']

while True:
    if len(Cards) == 0:
        print("獎項以全數抽完")
        break
    else:
        Draw_Card = random.choice(Cards)

        if Draw_Card == '精通人工智慧':
            Probability = random.randint(1,100)
            if Probability < 4:
                print("\n恭喜抽到 UR".format(Draw_Card))
                Cards.remove(Draw_Card)
                print("\n目前尚未抽出的獎勵還有：\n{}".format(Cards))
            else:
                print("\n銘謝惠顧，獲得其他任務道具")

        elif Draw_Card == '熟悉雲端技術':
            Probability = random.randint(1,100)
            if Probability < 8:
                print("\n恭喜抽到 SSR".format(Draw_Card))
                Cards.remove(Draw_Card)
                print("\n目前尚未抽出的獎勵還有：\n{}".format(Cards))              
            else:
                print("\n銘謝惠顧，獲得其他任務道具")

        elif Draw_Card == '熟練資料結構與演算法' or Draw_Card =="熟練機器學習":
            Probability = random.randint(1,100)
            if Probability < 20:
                print("\n恭喜抽到 SR {}".format(Draw_Card))
                Cards.remove(Draw_Card)
                print("\n目前尚未抽出的獎勵還有：\n{}".format(Cards))
            else:
                print("\n銘謝惠顧，獲得其他任務道具")
        
        elif Draw_Card == '掌握資料庫管理' or Draw_Card =="掌握通訊協定" or Draw_Card =="掌握作業系統原理":
            Probability = random.randint(1,100)
            if Probability < 30:
                print("\n恭喜抽到 R {}".format(Draw_Card))
                Cards.remove(Draw_Card)
                print("\n目前尚未抽出的獎勵還有：\n{}".format(Cards))
            else:
                print("\n銘謝惠顧，獲得其他任務道具")
        
        
        elif Draw_Card == '了解電腦組裝' or Draw_Card =="文件編輯排版" or Draw_Card =="網路基礎認知" or Draw_Card =="資訊安全基礎" or Draw_Card =="基礎Python" or Draw_Card =="基礎C++" or Draw_Card =="基礎Java":
            Probability = random.randint(1,100)
            if Probability < 40:
                print("\n恭喜抽到 N {}".format(Draw_Card))
                Cards.remove(Draw_Card)
                print("\n目前尚未抽出的獎勵還有：\n{}".format(Cards))
            else:
                print("\n銘謝惠顧，獲得其他任務道具")
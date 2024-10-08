selam = { "CRINGE": "Garip ya da utandırıcı bir şey",
             "LOL": "Komik bir şeye verilen cevap",  }
word = input("Anlamadığınız bir kelime yazın ")
if word in selam.keys():
    print(selam[word])
else:
    print("boyle bir kelime bulanamadi")
    print("kendinizde bir tanesini olusturun")
    ask = input("Sizin listeniz olusturun")
    selamm = {}
    selamm[ask] = "anlami yok"
    print("sizin sozun menasi",selamm[ask])
    soru2 = input("Peki nasilsin isler nasil gidiyor")
    soru3 = input("iyi mi kotumu")
    kullanicinruhu = {}
    kullanicinruhu[soru2] = soru3
    print("senin ruhun",soru3)

selam = { "CRINGE": "Garip ya da utandırıcı bir şey",
             "LOL": "Komik bir şeye verilen cevap",  }
word = input("Anlamadığınız bir kelime yazın ")
if word in selam.keys():
    print(selam[word])
else:
    print("boyle bir kelime bulanamadi")

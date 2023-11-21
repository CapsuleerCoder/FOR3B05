# #Dæmi A - Goðan daginn 1 
# klukkan = int(input("Hvað er klukkan? "))
# if klukkan <= 18:
#     print ("Góðan daginn")
# else:
#     print ("Gott Kvöld")

# #Dæmi B - Góðan daginn 2
# klukkan = int(input("Hvað er klukkan? "))
# if klukkan < 0 or klukkan > 24:
#     print ("Rangur innsláttur.")
# elif klukkan <= 18:
#     print ("Góðann daginn ")
# else:
#     print ("Gott kvöld")

# #Dæmi C - Minnsta tala
# tala_1 = int(input("Sláðu inn tölu: "))
# tala_2 = int(input("Sláðu inn aðra tölu: "))
# if tala_1 == tala_2:
#     print ("Tölur eru jafn stórar")
# elif tala_1 < tala_2:
#     print (tala_1, "er minni en ", tala_2)
# else:
#     print (tala_2, "er minni en ", tala_1)

# #Dæmi D - Minnsta tala
# tala_1 = int(input("Sláðu inn tölu: "))
# tala_2 = int(input("Sláðu inn aðra tölu:"))
# tala_3 = int(input("Sláðu inn þriðju tölu "))
# minnsta_tala = tala_1
# if tala_2 < minnsta_tala:
#     minnsta_tala = tala_2
# if tala_3 < minnsta_tala:
#     minnsta_tala = tala_3
# print ("Minnsta talan er: ", minnsta_tala)

# #Dæmi E - Aldur 1
# aldur = int(input("Hvað ertu gamalt eintak? "))
# if aldur >= 0 and aldur <= 19:
#     print ("Vonandi ætlar þú í Háskólann í Reykjavík")
# else:
#     print ("Það var nú fróðlegt!")

# #Dæmi F - Aldur 2
# aldur = int(input("Hvað ertu gamalt eintak? "))
# if aldur > 105: 
#     print ("Þú hefur svarað mögulega svara vitlaust")
# elif aldur >= 0 and aldur <= 6:
#     print ("Nú, svo þú ferð að byrja í skóla")
# elif aldur >= 7 and aldur <= 15:
#     svar = input("Ætlar þú í menntaskóla? svaraðu j eða n ")
#     if svar == "j":
#         print ("það er frábært að heyra")
#     else:
#         print("Það er nú leiðinlegt! ")
# elif aldur >= 16 and aldur <= 105:
#     print("Já ok en fróðlegt, sjáumst þá!")

# #Dæmi G - Hlaupaár 1
# ar =  int(input("Veldu ár og við kíkjum hvort það sé hlaupaár: "))
# if ar % 4 == 0:
#     print ("Já, þetta er hlaupaár!")
# else:
#     print ("Nei, því miður er þetta ekki hlaupaár!")

# #Dæmi H - Hlaupaár 2
# ar =  int(input("Veldu ár og við kíkjum hvort það sé hlaupaár: "))
# if ar % 4 != 0 or (ar % 100 == 0 and ar % 400 != 0):
#     print ("Þetta er ekki hlaupaár.")
# else:
#     print ("Þetta er hlaupaár.")


#Dæmi H - Hlaupaár 2
hlaupaar = int(input("Sláðu inn ár hér til að komast að því hvort það sé hlaupaár: "))
if hlaupaar % 100 == 0 and hlaupaar % 400 !=0:
    print ("Þetta er ekki hlaupaár")
elif hlaupaar % 400 == 0:
    print ("Þetta er hlaupaár ")
elif hlaupaar % 4 == 0:
    print ("Þetta er hlaupaár. ")
else:
    print ("Þetta er ekki hlaupaár")






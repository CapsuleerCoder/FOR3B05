# #Dæmi A - Lykkja
# svar = "j"
# while svar == "j":
#     tala = float(input("Sláðu inn tölu "))
#     print ("Þú hefur slegið inn töluna ", tala)
#     svar = input("Langar þér að slá inn aðra tölu? (j fyrir já)")

# #Dæmi B Talnabil - 1
# for x in range(5, 16):
#     print (x)

# #Dæmi C Talnabil - 2
# tala_1 = int(input("Veldu minni tölu fyrir bilið: "))
# tala_2 = int(input("Veldu stærri tölu fyrir bilið: "))
# for x in range(tala_1+1, tala_2):
#     print (x)

# #Dæmi D Talnabil - 3
# tala_1 = int(input("Veldu minni tölu fyrir bil: "))
# tala_2 = int(input("Veldu stærri tölu fyrir bilið: "))
# if tala_1 == tala_2 or tala_1+1 == tala_2 or tala_1 > tala_2:
#     print ("Villa 404, vitlaust innsláttur")
# else:
#     for x in range(tala_1+1, tala_2):
#         print (x)

# #Dæmi E Talnabil - 4
# tala_1 = int(input("Veldu minni tölu fyrir bil: "))
# tala_2 = int(input("Veldu stærri tölu fyrir bilið: "))
# for x in range(tala_1, tala_2+1):
#     print (x, "í öðru veldi: ", x**2)

# #Dæmi F Talnabil - Summa
# summa = 0
# tala_1 = int(input("Veldu minni tölu fyrir bil: "))
# tala_2 = int(input("Veldu stærri tölu fyrir bilið: "))
# for x in range(tala_1, tala_2+1):
#      summa +=x
#      print ("bil tala: ", x, "Samtals summa: ", summa)
    
# #Dæmi G Talnabil - Hropmerkt
# tala_1 = int(input("Veldu minni tölu fyrir bil: "))
# tala_2 = int(input("Veldu stærri tölu fyrir bilið: "))
# samtals = tala_1
# while tala_1 <= tala_2:
#     for undirtölur in range(1, tala_1):
#         samtals = samtals*undirtölur
#     print ("Talan er: ",tala_1,"\t", "talan sinnum allt undir er : ", samtals)
#     tala_1 += 1
#     samtals = tala_1

# #Dæmi H Margföldunartafla 1
# tala = int(input("Sláðu inn tölu til að sjá margföldunartöflu hennar: "))
# for einn_til_tiu in range (1,10+1):
#     print (tala,"*", einn_til_tiu, "=", tala*einn_til_tiu)

# #Dæmi I Margföldunartafla 2
# for fyrsta_tala in range (1, 10+1):
#     for seinni_tala in range(1, 10+1):
#         print (fyrsta_tala,"*", seinni_tala,"=", fyrsta_tala*seinni_tala)












# #Dæmi 1
# staf = input("Sláðu inn streng og fáðu fyrstu 2 stafinu sinnum 4 til baka: ")
# nystaf = (staf[0:2])*4
# print (nystaf)

# #Dæmi 2
# print ("Nú ætlum við að slá inn tvær tölur og fá allar tölur á bilinu nema þær sem 4 gengur upp í.")
# lægri = int(input("Sláðu inn lægri tölu: "))
# hærri = int(input("Sláðu inn hærri tölu: "))
# for tölu in range(lægri, hærri+1):
#     if tölu % 4 != 0:
#         print (tölu)

# #Dæmi 3
# print ("Input 2 numbers and we will print out the range either in regular or reverse order, then we will print the sum")
# lower = int(input("Input lower number: "))
# higher = int(input("Input higher number: "))
# reverse = int(input("input 0 for reverse order, input anything else for regular order: "))
# sum = 0
# if reverse == 0:
#     for tala in range(higher, lower-1, -1):
#         print (tala)
#         sum += tala
# else:
#     for tala in range (lower,higher+1):
#         print (tala)
#         sum += tala
# print (sum)

# #Dæmi 4
# def reikna_vsk(total_before, vsk):
#     total_after = (total_before*vsk/100)+total_before
#     return total_after
# before = int(input("Sláðu inn vöruverð áður en vsk: "))
# tax = int(input("Sláðu inn vsk skattprósentu: "))
# breyta = reikna_vsk(before, tax)
# print (f"Samtals vöruverð er: {breyta}")

# #Dæmi 5
# def lengd_strengs(string):
#     length = 0
#     for i in string:
#         length += 1
#     return length
# strengur = input("Sláðu inn einhver orð og fáðu lengd setningar eða orðaruglinu sem þú settir fram: ")
# lengd = lengd_strengs(strengur)
# print (f"Orðafjöldinn í þessu rugli hjá þér er {lengd}")


#Dæmi 6
# 6.	(14%) Hver er tilgangurinn með því að nota föll í forritun?
# Hvaða ókostir myndu fylgja því að geta ekki notað föll? Útskýrið í eigin orðum.


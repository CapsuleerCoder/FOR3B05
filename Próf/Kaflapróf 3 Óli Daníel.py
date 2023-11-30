# #Dæmi 1
# Höfuðborgir = ["Róm", "Washington", "Reykjavík", "París", "Kaupmannahöfn"]
# borg = input("Sláðu inn höfuðborg og við athugum hvort hún sé í listanum: ")
# if borg in Höfuðborgir:
#     print (f"Já hún {borg} er í listanum okkuar")
#     print (f"Listinn okkar er eftirfarandi: {Höfuðborgir}")
# if borg not in Höfuðborgir:
#     svar = int(input("Sláðu inn 1 til að bæta henni við listann eða hvað sem er annað til þess að sleppa því"))
#     if svar == 1:
#         Höfuðborgir.append(borg)
#         print (f"Nú er listinn okkar {Höfuðborgir}")
#     else:
#         print (f"Nú jæja, þá er listinn okkar bara basic enn {Höfuðborgir}")



# def ultimate_fall(listi):
#     summa = 0
#     hæsta = listi[0]
#     lægsta = listi[0]
#     for i in listi:
#         if i > hæsta:
#             hæsta = i
#         if i < lægsta:
#             lægsta = i
#         summa += i
#     count = listi.count(10) # Gæti svo sem notað for loop hér ef þarf, þá væri það bara for i in listi: if i == 10: count += 1 dæmi
#     return summa/len(listi), hæsta, lægsta, count
# #Dæmi 2
# fjöldi_nemenda = int(input("Hversu margir nemendur voru í hagfræðiprófi: "))
# einkunnarlisti = []
# count = 1
# while fjöldi_nemenda != count-1:
#     einstaklingseinkunn = int(input(f"Sláðu inn einkunn fyrir nemanda {count} : "))
#     count += 1
#     einkunnarlisti.append(einstaklingseinkunn)
# Kall_to_fall = ultimate_fall(einkunnarlisti)
# print (f"Þá er listinn okkar {einkunnarlisti}")
# print (f"Meðaleinkunn okkar er {Kall_to_fall[0]}")
# print (f"Hæsta einkunn er {Kall_to_fall[1]}")
# print (f"Lægsta einkunn er {Kall_to_fall[2]}")
# print (f"Fjöldi nemenda með 10 er : {Kall_to_fall[3]}")


# # #Dæmi 3
# orðalisti = []
# with open ("BorgesTilvitnun.txt", "r") as borges:
#     for line in borges:
#         borgeslínur = line.split()
#         for orð in borgeslínur:
#             strippað = orð.strip(", .")
#             orðalisti.append(strippað)
#     orðalistisett = set(orðalisti)
# for i in orðalistisett:
#     print (i, end=" , ")
# print ("\nÞetta er listinn yfir orð sem koma fram í textaskránni: BorgesTilvitnun.txt")

# Dæmi 3 revised
orðalisti = []
orða_upflettitafla = {}
with open ("BorgesTilvitnun.txt", "r") as temp_var:
    borges = temp_var.read()
orðalisti = borges.split()
for orð in orðalisti:
    orð.strip(",. ;:")
    if orð in orða_upflettitafla:
        orða_upflettitafla[orð] += 1
    if orð not in orða_upflettitafla:
        orða_upflettitafla[orð] = 1
orðaset = set(orðalisti)
lengd = len(orðaset)
teljari_algengast = max(orða_upflettitafla.values())
algengasta_orð =max(orða_upflettitafla, key=orða_upflettitafla.get)
print (f"Það eru {lengd} mismunandi orð í skránni okkar.")
print (f"Algengasta orðið er {algengasta_orð}, það kemur fram {teljari_algengast}")



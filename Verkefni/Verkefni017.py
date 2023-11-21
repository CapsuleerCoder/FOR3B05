#Verkefni 17
# #Dæmi A
# with open("SV1.txt", "r") as file:
#     SV1_lagað = file.read()
# SV1_lagað = SV1_lagað.replace("\n", "")
# SV1_lagað = SV1_lagað.replace(" ", "")
# with open("SV1_lagað.txt", "w+") as newf:
#     newf.write(SV1_lagað)

# #Dæmi B
# with open ("SV2.txt", "r") as file:
#     SV2_2 = file.read()
# SV2_2 = SV2_2.split(", ")
# SV2 = open ("SV2_lagað.txt", "w+")
# for name in SV2_2:
#     SV2.write(name)
#     SV2.write("\n")
# SV2.close()

# #Dæmi C
# file = open ("SV2_lagað.txt", "r")
# eftirnöfn = open("eftirnöfn.txt", "w+")
# count = 1
# for line in file:
#     # print (line)
#     spliter = line.split()
#     # print ("splittað", spliter)
#     eftirnafn =spliter[-1]
#     count += 1 
#     skrifað = (f"Nemandi {count}: {eftirnafn} \n")
#     eftirnöfn.write(skrifað)
#     # print (skrifað)
# file.close()
# eftirnöfn.close()

# #Dæmi D
# file = open("Setningar.txt", "w+")
# innsláttur = ""
# while innsláttur != "EOF":
#     innsláttur = input("Sláðu inn eitt orð í einu, ef þú slærð inn . þá munum við fara í næstu línu, sláðu inn EOF til að hætta:   ")
#     if innsláttur == "EOF":
#         break
#     if "." in innsláttur:
#         file.write(innsláttur)
#         file.write("\n")
#         # print (innsláttur)
#     else:
#         file.write(innsláttur)
#         file.write(" ")
#         # print (innsláttur)
# file.close()

# #Dæmi E
# svar = input("Við erum með SV1, SV2, SV1_lagað, SV2_lagað og eftirnöfn, skrifið inn eitt af þeim til að fá lengsta orðið sem er í þeirri skrá")
# svar2 = f"{svar.upper()}.txt"
# # print (svar2)
# skrá1 = open(svar2, "r")
# file = skrá1.read()
# file = file.split()
# lengst = max(file, key=len)
# lengd = len(lengst)
# # print (file)
# # print (lengst)
# print (f"Lengsta orðið er {lengst}, það er {lengd} langt")















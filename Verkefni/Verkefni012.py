#Dæmi A 
texti = "hallo heimur"
print (texti[0])
print (texti[-1])
print ("það eru ", len(texti), "stafir í hallo heimur")

# #Dæmi B
# breyta = "A Santa at Nasa"
# print (breyta)
# for i in breyta:
#     print (i)
# for x in breyta[::-1]:
#     print (x)

# #Dæmi C
# strengur = input ("Sláðu inn einhern texta: ")
# lengd = int(input("Hversu marga stafi af þessu viltu prenta út? "))
# print (strengur[:lengd])

# #Dæmi D 
# strengur = input ("Sláðu inn einhern texta: ")
# hopp = int(input("prentum þetta út, hverstu oft viltu hoppa yfir staf? "))
# if hopp == 0 :
#     hopp = 1
#     print (strengur[::hopp])
# else:
#     print (strengur[::hopp])

# #Dæmi E 
# texta = input("Sláðu inn texta með hástöfum og lágstöfum: ")
# stafir = input("sláðu inn h ef þú vilt bara hástafi eða l ef þú vilt bara lágstafi: ")
# if stafir == "h":
#     print (texta.upper())
# elif stafir == "j":
#     print (texta.lower())
# else:
#     print ("vitlaus innsláttur, heimski notandi")

# #Dæmi F
# nafn = input("sláðu inn nafn þitt, notandi: ")
# aldur = int(input("Sláðu inn aldur þinn {} :".format(nafn)))
# starf = input("Sláðu inn starfið þitt {} :".format(nafn))
# print ("Góðan daginn {} :\nþú ert nú orðinn {}, ertu ekki orðinn of gamall til að vera {} ".format(nafn, aldur, starf))

# #Dæmi G 
# streng = input("Sláðu inn orð: ")
# if "halló" in streng:
#     print ("texti inniheldur halló ")
# else:
#     print("Texti inniheldur ekki halló ")

# #Dæmi H
# strengur = input("sláðu inn eitthvað, kæra notandi : ")
# stafir = False
# tölur = False
# special = 0
# for x in strengur: 
#     if x.isalpha() and not x.isdigit():
#         stafir = True
#     if x.isdigit() and not x.isalpha():
#         tölur = True
#     if not x.isdigit() and not x.isalpha():
#         special = 1
# if special == 1:
#     print ("Þú ert nú meiri rugludallurinn")
# elif tölur == True and stafir == False:
#     print ("Bara tölur")
# elif stafir == True and tölur == False:
#     print ("Bara stafir")
# else:
#     print ("Þú ert nú meiri rugludallurinn")









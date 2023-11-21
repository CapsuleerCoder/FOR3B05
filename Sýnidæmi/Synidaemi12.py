
sanngildi = True
print(type(sanngildi))
# sanngildi er af taginu bool, en ekki int, float eda string
# bool breytur geta einungis innihaldid gildin 1 eda 0, einnig kollud
# True eda False

tala1 = 1
tala2 = 5
tala3 = 10
if tala1 < tala2 < tala3:
    print("Tala 2 er i midjunni")
# eins og sest her ad ofan ta er haegt ad hafa kedju samanburda
# ef tala2 er baedi staerri en tala1 og minni en tala3 ta prentast
# skilabodin ut, annars ekki.

if not (tala2 == tala3):
    print("Einmitt, 5 er ekki 10.")
# ef vid viljum snua sanngildi vid ta getum vid notad lykilordid not. Her erum vid ad segja
# ad ef tad er EKKI satt ad 5 se 10, ta viljum vid prenta ut skilabodin. Samanburdurinn
# tala2 == tala3 skilar gildinu False sem myndi tyda ad talvan faeri EKKI inn i blokkina
# en not snyr False vid og yfir i True tannig ad talvan fer inn i blokkina og prentar ut
# skilabodin "Einmitt, 5 er ekki 10."

if not ("Jon" == "Jon"):
    print("Tad er ekki sama Jon og sera Jon!")
else:
    print("Tad var ekki talad um sera neitt og talvan skilur allt bokstaflega tannig ad ...")
# Her skilar samanburdurinn "Jon" == "Jon" gildinu True en not snyr tvi vid yfir i False
# svo talvan fer inn i blokkina sem fylgir lykilordinu else







# #Dæmi 1 ártal
# year = int(input("Sláðu inn ár: "))
# if year % 1000 == 0:
#     print ("þarna byrjaði nýtt árþúsund!")
# elif year % 100 == 0:
#     print ("þarna byrjaði ný öld!")
# elif year == 1964:
#     print ("þarna byrjaði saga HR!")
# else:
#     print ("ósköp venjulegt ár þarna á ferð!")

# #Dæmi 2 talnabil
# tala_1 = int(input("Vinsamlega sláðu inn fyrri tölu: "))
# tala_2 = int(input("Vinsamlega sláðu inn seinni tölu: "))
# vaxandi = int(input("Sláðu inn 1 fyrir vaxandi og 0 fyrir minnkandi: "))
# if vaxandi == 1:
#     for i in range(tala_1, tala_2+1):
#         if i % 3 == 0 or i % 5 == 0:
#             continue
#         print (i)
# elif vaxandi == 0:
#     for i in range(tala_2, tala_1-1, -1):
#         if i % 3 == 0 or i % 5 == 0:
#             continue
#         print (i)

#Dæmi 3 binary number
# Við lesum þetta frá hægri til vinstri og fer alltaf upp sinnum tveir
# þannig 110101 verður 1 + 0 + 4 + 0 + 16 + 32 = 53
# Við getum sannreynt þetta með print (int(0b110101))sem gefur okkur 53, print (bin(53)) er öfugt
# getum einnig hugsað þetta sem 1**0 + 0**1 + 2**2 + 0**3 + 2**4 + 2**5 = 53

# #Dæmi 4 strengur
# string = input("Sláðu inn eitthvað orð eða setningu: ")
# tala = int(input("Sláðu inn einhverja heiltölu, helst lága: "))
# print (f"Nú ætlum við að prenta út orðið/setningu þínu og við ætlum að hoppa yfir {tala} marga stafi")
# reverse = int(input("Sláðu inn 1 fyrir öfuga röð, eða 0 fyrir venjulega: "))
# if reverse == 0:
#     for i in string[::tala]:
#         print (i, end="")
# elif reverse == 1:
#     for i in string[::-tala]:
#         print (i, end="")

#Dæmi 5

# def flatarmal_hrings(radius_hrings):
#     return radius_hrings**2*3.14
# def rummal_kulu(radius_kulu):
#     return  (4*3.14*radius_kulu**3)/3

# print (flatarmal_hrings(20))

# #Dæmi 6 
# class Kula:
#     def __init__(self,radius):
#         self.radius = radius   
#     def rummal_kulu(self):
#         math = (4*3.14*self.radius**3)/3
#         return f"Rummál Kúlunnar okkar er {math}"
#     def __str__(self):
#         return f"Radius kúlunnar okkar er {self.radius}"
# def main():
#     tala = float(input("Sláðu inn radíus kúlunnar: "))
#     kulan_okkar = Kula(tala)
#     print (f"{kulan_okkar}, {kulan_okkar.rummal_kulu()}")
# main()

#Dæmi 7
diction_words = {}
with open("HanSolo.txt", "r") as file:
    for line in file:
        new_line = line.lower().replace(",", "").replace(".", "").replace("?", "").split()
        for i in new_line:
            if i in diction_words:
                diction_words[i] += 1
            else:
                diction_words[i] = 1
            print (i)
summa = sum(diction_words.values())            
counter_above_1 = 0
for i in diction_words.values():
    if i > 1:
        counter_above_1 += 1
print (f"Orða sem koma oftar en einu sinni: {counter_above_1}")
print (f"total orð: {summa}")


    # Lengd = sum(orðabók.values())
    # Algengast_orð = max(orðabók, key=orðabók.get)
    # Algengast_tilfelli = orðabók[Algengast_orð]


#Traveling through hyperspace aint like dusting crops, farm boy. 
# Without precise calculations we could fly right through a star or 
# bounce too close to a supernova, and thatd end your trip real 
# quick, wouldnt it?
# Han Solo

#Forritið á að tilkynna notandanum hversu mörg orð koma oftar fyrir
# en einu sinni í skránni og einnig hver var heildarfjöldi orða í skránni




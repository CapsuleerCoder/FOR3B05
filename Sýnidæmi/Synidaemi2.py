
a = 2
# her gerum vid breytu sem heitir a og gefum henni gildid 2. Breyta er plass i minni tolvunnar
# sem vid hofum tekid fra til ad geyma upplysingar. Med = merkinu gefum vid breytu eitthvad
# gildi, reglan er su ad TAD SEM ER HAEGRA MEGIN FER INN I TAD SEM ER VINSTRA MEGIN.

print(a)
# nu prentast ud 2

a = 3
print(a)
# nu prentast ud 3, athugid ad 3 baetist ekki vid heldur er skrifad yfir fyrra innihald breytunnar

a = a+1
print(a)
# nu prentast ud 4, a vard ad tvi sem hun var + 1. Eda tad sem var haegra megin var 3+1 og
# tad for inn i tad sem var vinstra megin svo a tok i raun vid 3+1 eda 4

a += 1
print(a)
# nu prentast ud 5, += 1 gerir sama og ad segja a = a + 1

b = 5 + 5
print(b)
# b er nu 10, fyrst verdur reikniadgerd tar sem 5 + 5 verdur 10, sidan verdur
# gildisveiting, tar sem 10 er sett inn i b

c = type(b)
print(c)
# vid faum ad vita ad b se af tegundinni int sem tydir ad tad er heiltolubreyta

radiusHrings = 10
flatarmalHrings = radiusHrings*radiusHrings*3.14
print(flatarmalHrings)
# nu kemur 314.0

flatarmalHrings = radiusHrings**2 * 3.14
print(flatarmalHrings)
# nu kemur lika 314.0, ** tydir bara ad vid setjum tolu i veldi svo 10**2 tydir 10 i odru veldi

d = type(flatarmalHrings)
print(d)
# vid faum ad vita ad b se af tegundinni float sem tydir ad tad er kommutolubreyta




túpla1 = (1,2,3)
print("Öll túplan er: ")
print(túpla1)
print("En fyrsta stakið má nálgast á sama hátt og um lista væri að ræða")
print(túpla1[0])
# eftirfarandi lína myndi valda villu vegna þess að ólíkt listum þá eru 
# túplur óbreytanlegar.
# túpla1[0] = 100
print("-----------------------------------------")
# við getum gengið yfir túplu eins og hún væri strengur eða listi
for i in túpla1:
    print(i)



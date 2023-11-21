
forNafn = input("Sladu inn fornafn titt. ")
eftirNafn = input("Sladu inn eftirnafn titt. ")

if forNafn == "Sveinn Arnar" and eftirNafn == "Stefansson":
    print("Godan daginn Sveinn Arnar Stefansson")
# Her koma skilabodin adeins ef notandi slaer inn "rett" i badum tilvikum
elif forNafn == "Sveinn Arnar" or eftirNafn == "Stefansson":
    print("Ok, halfrett.")
# Her koma skilabodin ef a.m.k. annad atridid var rett.
else:
    print("!$#&")
# Hingad forum vid ef baedi atridi voru rong





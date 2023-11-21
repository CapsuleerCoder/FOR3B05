def margföldun(tala):   
    print (tala, "sinnum tafla: " , end = "")
    for x in range(1,11):
        print (x*tala, end=" ")
def margföldun2():
     for t in range(1,11):
        margföldun(t)
        print()
def fall1(t1, t2):
    for e in range(t1,t2+1):
        print (e, end=" ")
def fall2(e1, e2):
    if e1 == e2 or e1-e2 == 1  or e2-e1 == 1:
        print ("Þú ert greinilega rugludallur!")
    for l in range(e1+1, e2):
        print (l, end= " ")
def veldi(tala,veldi):
    return tala**veldi
def modulus(heild,deild):
    for i in range(0,heild+1, deild):
        if i == heild:
            return 0
        elif (i+deild) > heild:
            return (heild-i)
def hlaupa(ar):
    if modulus(ar,400) == 0:
        return True
    elif modulus(ar, 4) == 0 and modulus (ar, 100) != 0:
        return True
    else:
        return False

answer = "J"
while answer.lower() != "n":
    answer = input("\nSláðu inn 1 til að slá inn tölu og sjá margföldunartöflu hennar\nSláðu inn 2 til að sjá 1-10 margföldunartöflu\nSláðu inn 3 til að slá inn tvær tölur og fá bilið með þeim meðtöldum\nSláðu inn 4 ef þú vilt slá inn tvær tölur og sjá bilið á milli þeirra\nSláðu inn 5 til að slá inn tölu og veldi hennar og sjá útkomu\nSláðu inn 6 til að slá inn heildartölu og deilingatölu og sjá afganginn\nSláðu inn 7 ef þú vilt slá inn ár og athuga hvort það sé hlaupaár\n:")
    if answer == "1":
        print ("Sláðu inn tölu til að fá margföldunartöflu hennar")
        margföldun(int(input("Sláðu inn tölu: ")))
    if answer == "2":
        print ("Hérna er margföldunartöflur 1-10: ")
        margföldun2()  
    if answer == "3":
        print ("Sláðu inn tvær tölur til að fá bilið á milli meðtöldum tölunum: ")
        fall1(int(input("Sláðu inn tölu: ")), int((input("SLáðu inn aðra tölu: "))))
    if answer == "4":
        print ("Sláðu inn tvær tölur til að fá bil á milli: ")
        fall2(int(input("Sláðu inn tölu: ")), int(input("Sláðu inn aðra hærri tölu")))
    if answer == "5":
        print ("Sláðu inn tölu og veldisvísi hennar:")
        print (veldi (int(input("Sláðu inn tölu: ")), int(input("Sláðu inn veldisvís hennar: "))))
    if answer == "6":
        print ("Nú ætlum við að modulusa án modulus, en spennandi!")
        print ("Modulus/afgangur er:", modulus(int(input("Hvaða heildartölu viltu: ")), int(input("Hvaða tölu viltu deila með: "))))
    if answer == "7":
        print ("Nú skulum við athuga hvort árið sem þú velur er hlaupaár ")
        print (hlaupa(int(input("Sláðu inn árið: "))))



























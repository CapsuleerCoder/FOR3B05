
Símaskrá = {}
Símaskrá2 = {
    "Óli Daníel" : "679-1515",
    "Jísli Hirtason" : "919-2500",
    "Turd mcfly" : "143-1000"
}
upflettitafla_tölur = {
    1 : 5000,
    2 : 10000,
    3 : 150000,
    4 : 420000,
    5 : 5000000000
}
#Dæmi A
def nafn_símanr():
    while True:
        print ("Sláðu inn s til að hætta og prenta út símaskránna")
        nafn = input("Sláðu inn nafn á manneskju: ")
        if nafn == "s":
            break
        símanúmer = input("Sláðu inn símanúmer: ")
        Símaskrá[nafn] = símanúmer
    print ("Símaskrá : ", Símaskrá)
#Dæmi B
def símaskráprent():
    for key, value in Símaskrá2.items():
        print (key, value)
    return "Símaskrá lokið"
#Dæmi C
def uppfletting(tala, tafla=upflettitafla_tölur):
    for key in tafla:
        if tala == key:
            return print ("lykillinn", key, "gefur okkur: ", tafla[key])
#Dæmi D 
def summa_orðabók(tafla=upflettitafla_tölur):
    total = 0
    for key in tafla:
        total += tafla[key]
    return total
def summa_lykla(tafla=upflettitafla_tölur):
    total = 0
    for i in tafla:
        total += i
    return total
    





while True:
    print ("Veldu 0 til að stoppa. ")
    print ("Veldu 1 til að gera símaskrá.")
    print ("Veldu 2 til að prenta út símaskrá. ")
    print ("Veldu 3 til að samreyna tölu með uppflettitöflu. ")
    print ("Veldu 4 til að summa öll gildi orðabókar.")
    print ("Veldu 5 til að summa alla lykal orðabókar. ")
    answer = input(":")
    if answer == "0":
        break
    if answer == "1":
        nafn_símanr()
    if answer == "2":
        print (símaskráprent())
    if answer == "3":
        búa_til_töflu_sjálf = input("Viltu Búa til töflu sjálfur? j fyrir já, n fyrir Nei ")
        if búa_til_töflu_sjálf == "j":
            upflettitafla_tölur.clear()
            print ("Þá skulum við gera það.")
            count = 1
            while True:
                print ("Sláðu inn 0 ef þú ert ánægður með þessa töflu")
                gildi = float(input("Veldu tölugildi: "))
                if int(gildi) == 0:
                    break
                upflettitafla_tölur[count] = gildi
                count += 1
                print ("Taflan okkar hingað til :", upflettitafla_tölur)
        print ("Taflan lítur svona út: ", upflettitafla_tölur)
        svar = int(input("Veldu tölu: "))
        uppfletting(svar, upflettitafla_tölur)
    if answer == "4":
        búa_til_töflu_sjálf = input("Viltu Búa til töflu sjálfur? j fyrir já, n fyrir Nei ")
        if búa_til_töflu_sjálf == "j":
            ný_tafla = {}
            print ("Þá skulum við gera það.")
            count = 1
            while True:
                print ("Sláðu inn 0 ef þú ert ánægður með þessa töflu")
                gildi = float(input("Veldu tölugildi: "))
                if int(gildi) == 0:
                    break
                ný_tafla[count] = gildi
                count += 1
                print ("Taflan okkar hingað til :", ný_tafla)

            print ("Taflan lítur svona út: ", ný_tafla)
            fall_kall = summa_orðabók(ný_tafla)
        else:
            print ("Taflan lítur svona út: ", upflettitafla_tölur)
            fall_kall = summa_orðabók()            
        print ("Samtals er þetta: ", fall_kall)
    if answer == "5":
        búa_til_töflu_sjálf = input("Viltu Búa til töflu sjálfur? j fyrir já, n fyrir Nei ")
        if búa_til_töflu_sjálf == "j":
            ný_tafla = {}
            print ("Þá skulum við gera það.")
            count = 1
            while True:
                print ("Sláðu inn 0 ef þú ert ánægður með þessa töflu")
                gildi = float(input("Veldu tölugildi: "))
                if int(gildi) == 0:
                    break
                ný_tafla[count] = gildi
                count += 1
                print ("Taflan okkar hingað til :", ný_tafla)
            print ("Taflan lítur svona út: ", ný_tafla)
            summa_lyklana = summa_lykla(ný_tafla)
        else:
            print ("Taflan lítur svona út: ", upflettitafla_tölur)
            summa_lyklana = summa_lykla()  
        print ("Summa lykla er: ", summa_lyklana)



































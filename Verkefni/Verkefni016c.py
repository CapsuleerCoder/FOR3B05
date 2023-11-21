#16C verkefni
import random
manuðir = ["Janúar", "Febrúar", "Mars", "Apríl", "Mai", "Júni", "Júlí", "Ágúst", "September", "Október", "Nóvember", "Desember"]
def mánaðarhitastig_1():
    hitastig = []
    for i in range(12):
        AVATAR = float(input(f"hvað var hitastig í {manuðir[i]}: "))
        hitastig.append(AVATAR)
    hæst = max(hitastig)
    place = manuðir[(hitastig.index(hæst))]
    lægst = min(hitastig)
    thirst = manuðir[(hitastig.index(lægst))]
    return f"{place} er með mesta hitan sem er {hæst}, {thirst} er með versta hitan sem er {lægst}"
def mánaðarhitastig_2():
    hitastig = []
    for i in range(0, 12):
        pod = float(input(f"hvað var hitastig í {manuðir[i]}: "))
        hitastig.append(pod)
    hæst = hitastig[0]
    hæsti_mán = manuðir[0]
    læ_g_st = hitastig[0]
    Lægsti_man = manuðir[0]   
    for t in range(12):
        if hitastig[t] > hæst:
            hæst = hitastig[t]
            hæsti_mán = manuðir[t]
        if hitastig[t] < læ_g_st:
            læ_g_st = hitastig[t]
            Lægsti_man = manuðir[t]
    return f"Mánuðurinn með hæsta hitastigið er {hæsti_mán} með {hæst}, lægsti er {Lægsti_man} með {læ_g_st}"
def draga_spil():
    sortir = ["Hjarta", "Spaði", "Tígull", "Lauf"]
    merkt = ["ás", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Gosi", "Drottning", "Kóngur"]
    firsta = random.choice(sortir)
    seconda = random.choice(merkt)
    return f"Þú dróst {firsta} {seconda}"
def tic_tac_toe():
    listinn = [[], [], []]
    for t in range(9):
        if t % 2 == 0:
          listinn[t%3].append("X")
        if t % 2 != 0:
            listinn[t%3].append("O")
    for x in range(3):
        print (*listinn[x], sep="")
    return ""
answer = "J"
while answer.lower() != "n":
    print ("Veldu 1 til að fara í mán 1 verkefni ")
    print ("Veldu 2 til að fara í mán 2 verkefni ")
    print ("Veldu 3 til að draga spil ")
    print ("Veldu 4 til að prenta tic tac toe borð ")
    answer = input("Veldu 1-4:   ")
    if answer == "1":
        print ("Ný byrjar grindið ")
        stabber = mánaðarhitastig_1()
        print (stabber)
    if answer == "2":
        print ("Ný byrjar grindið ")
        capsule = mánaðarhitastig_2()
        print (capsule)
    if answer == "3":
        print ("Nú drögum við spil því við erum sad og höfum ekkert betra að gera")
        griffin = draga_spil()
        print (griffin)
    if answer == "4":
        print ("Nú ætlum við að prenta skemmtilegt tic-tac-toe borð því við erum froskamenn")
        scorpion = tic_tac_toe()
        print (scorpion)






























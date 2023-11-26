
#Dæmi A
def lesa_tesla():
    with open ("/home/olidb/Forritun/Tesla.txt", "r") as skrá:
        for line in skrá:
            orðalisti = line.split()
            for orð in orðalisti:
                    strip_orð = orð.strip(", .")
                    if strip_orð in orðabók:   
                        orðabók[strip_orð] += 1
                    else:
                        orðabók[strip_orð] = 1
    for key, value in orðabók.items():
        print (key, value)
    return "og það er lokatalning"
#Dæmi C 
def lesa_Borges():
    with open("/home/olidb/Forritun/Borges.txt", "r") as borges:
        for line in borges:
            orðalisti = line.split()
            for orð in orðalisti:
                strippað_orð = orð.strip(", .")
                if strippað_orð in orðabók:
                    orðabók[strippað_orð] += 1
                else:
                    orðabók[strippað_orð] = 1
    Lengd = sum(orðabók.values())
    print ("Það eru", Lengd, "orð í skjali")
    Algengast_orð = max(orðabók, key=orðabók.get)
    print ("Algengasta orðið er ", Algengast_orð)
    print (orðabók)





while True:
    print ("Veldu 1 til að lesa Tesla.txt og telja orð. ")
    print ("Veldu 2 til að lesa Borges.txt og telja orð. ")
    svar = input(":")
    orðabók = {}
    if svar == "1":
        keyra_fall_A= lesa_tesla()
        print(keyra_fall_A)
    if svar == "2":
        keyra_fall_b = lesa_Borges()
        print (keyra_fall_b)




















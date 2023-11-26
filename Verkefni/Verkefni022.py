
#Dæmi A
def lesa_tesla():
    with open ("Tesla.txt", "r") as skrá:
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
    with open("Borges.txt", "r") as borges:
        for line in borges:
            orðalisti = line.split()
            for orð in orðalisti:
                strippað_orð = orð.strip(", .")
                if strippað_orð in orðabók:
                    orðabók[strippað_orð] += 1
                else:
                    orðabók[strippað_orð] = 1
    Lengd = sum(orðabók.values())
    Algengast_orð = max(orðabók, key=orðabók.get)
    Algengast_tilfelli = orðabók[Algengast_orð]
    return Lengd, Algengast_orð, Algengast_tilfelli
def lesa_bæði():
    borges_list = []
    tesla_list = []
    with open("Borges.txt","r") as borges:
        for line in borges:
            borges_orð = line.split()
            for orðb in borges_orð:
                strippað = orðb.strip(", .")
                borges_list.append(strippað)
            borges_list_set = set(borges_list)
    with open("Tesla.txt", "r") as tesla:
        for line in tesla:
            tesla_orð = line.split()
            for orðt in tesla_orð:
                stripped = orðt.strip(", .")
                tesla_list.append(stripped)
            tesla_list_set = set(tesla_list)
    sniðmengi = borges_list_set & tesla_list_set
    #stal set af Atla því ég hef ekki hugmynd hvað mengi er, 
    # myndi annars nota for loop til að mynda lista úr báðum
    return sniðmengi
while True:
    print ("Veldu 1 til að lesa Tesla.txt og telja orð. ")
    print ("Veldu 2 til að lesa Borges.txt og telja orð. ")
    print ("Veldu 3 til að fá orðin sem eru í báðum skrám")
    svar = input(":")
    orðabók = {}
    if svar == "1":
        keyra_fall_A= lesa_tesla()
        print(keyra_fall_A)
    if svar == "2":
        keyra_fall_c = lesa_Borges()
        print (f"Það eru {keyra_fall_c[0]} orð í skjalinu")        
        print (f"Algengasta orðið er {keyra_fall_c[1]}")
        print (f"Það kemur fyrir {keyra_fall_c[2]} sinnum")
    if svar == "3":
        keyra_fall_d = lesa_bæði()
        print (f"orðin sem eru í báðum eru {keyra_fall_d}")


















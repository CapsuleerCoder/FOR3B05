
presidents = ["Ronald Reagen", "George H. W. Bush", "Bill Clinton", "George W. Bush", "Barak Obama", "Donald Trump", "Joe Biden"]

def pres(tala):
    if tala == 1:
        return presidents [:-4]
    if tala == 2:
        return presidents [-4:]
def pres2(foreseti):
    for x in presidents:
        if x.lower() == foreseti.lower():
            return f"Já hann {x} er í listanum"
    return "Nei, taktu hausinn úr rassgatinu"
def pres3(arara):
    for x in presidents:
        if x.lower() == arara.lower():
            return f"Já hann {x} er í listanum"        
        elif x.lower()[:3] == arara.lower()[:3]:
            return f"Já hann {x} eða eins og þú kallar hann {arara} er í listanum"
    return "Nei held nú ekki kæri notandi"
def pres4(forbr):
     presidents.insert(0, forbr)
     return presidents
def pres4c(forba):
    if forba.lower() == "joe biden":
        return presidents
    else:
        presidents.append(forba)
        return presidents

answer = "J"
while answer.lower() != "n":
    answer = input("1 = Dæmi 1\n2 = Dæmi 2 \n3 = Dæmi 3\n4 = Dæmi 4\n")
    if answer == "1":
       print(pres(int(input("Veldu 1 til að sjá forseta sem réðu ríkjum 1980 til 2000 og 2 til að sjá foreseta sem hafa ráða ríkjum síðan þá: "))))
    if answer == "2":
        print(pres2(input("Hvaða forseta bandaríkjanna hefur þú áhuga á, við skulum kíkja hvort hann sé í listanum okkar: ")))
    if answer  == "3":
        print(pres3(input("Sláðu inn forseta USA USA USA til að athuga hvort hann sé í listanum: ")))
    if answer == "4":
        print(pres4(input("Hver var forseti á undan Ronald Reagan? ")))
        print(pres4c(input("Hvað forseti er  næstur? ")))
    presidents = ["Ronald Reagen", "George H. W. Bush", "Bill Clinton", "George W. Bush", "Barak Obama", "Donald Trump", "Joe Biden"]



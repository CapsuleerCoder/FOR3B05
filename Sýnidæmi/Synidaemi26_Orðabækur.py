# lítil hreiðruð símaskrá
símaskrá = {"Sveinn Arnar Stefánsson": {"Símanúmer": 7723954, "Heimilisfang": "Menntavegi 1"}, "Jón Jónsson": {"Símanúmer": 5812345, "Heimilisfang": "Menntavegi 2"}}

print("Sveinn hefur símanúmerið: ", símaskrá["Sveinn Arnar Stefánsson"]["Símanúmer"])
print("Jón hefur símanúmerið: ", símaskrá["Jón Jónsson"]["Símanúmer"])
print("Sveinn býr á: ", símaskrá["Sveinn Arnar Stefánsson"]["Heimilisfang"])
print("Jón býr á: ", símaskrá["Jón Jónsson"]["Heimilisfang"])
print("----------------------------------------------")
# önnur lítil orðabók
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# ef við viljum ganga yfir orðabók og prenta alla lyklana þá gerum við það svona
for i in thisdict:
    print(i)
print("----------------------------------------------")
# en ef við viljum ganga yfir orðabók og prenta öll gildi lyklanna þá er það gert svona
for i in thisdict:
    print(thisdict[i])
print("----------------------------------------------")
# við getum líka nýtt okkur items aðferðina en hún skilar okkur svokallaðri túplu (túplur minna 
# á lista, en eru samt að sumu leyti öðruvísi, t.d. eru þær óbreytanlegar). Næstu tvær línur 
# innan # sýna hvernig hægt er að gera túplu og prenta hana.
# túpla1 = (2,3)
# print(túpla1)
for key, value in thisdict.items():
  print("Lykill: ", end="")
  print(key, end=", ")
  print("Gildi: ", end="")
  print(value)

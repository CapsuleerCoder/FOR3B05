
a = int(input("Sladu inn tolu "))
# profid ad sla inn 1, 2 eda 3
print("Hun verdur borin saman vid breytuna b sem hefur gildid 2.")
b = 2

if (a < b):
    print("a er minni en b")
elif (a == b):
    print("a er jafnstor og b")
else:
    print("a er staerri en b")
# talvan athugar fyrst hvort a se minni en b, ef svo er ekki ta utilokar hun tann moguleika
# og heldur afram ad athuga skilyrdi (eins og a < b, eda a == b) tangad til hun finnur eitthvad
# sem er satt. Ef hun finnur ekkert satt skilyrdi ta endar hun a ad velja blokkina sem fylgir 
# else lykilordinu.



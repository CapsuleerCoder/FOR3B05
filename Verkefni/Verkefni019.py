#Dæmi A
# svar = ""
# while type(svar) is not int:
#     svar = input("Sláðu inn heiltölu:")
#     try:
#         svar = int(svar)
#         print ("Inntak er í lagi, ")
#     except ValueError:
#         print ("Inntak er ekki heiltala. ")

#Dæmi B
def sum(a, b):
    try:
        return a+b
    except TypeError:
        return "Rangur innsláttur"
innsláttur1 = "svar"
innslátttur2 = 3
svar = sum(innsláttur1, innslátttur2)
print (svar)











































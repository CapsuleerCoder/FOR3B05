# Dæmi 1
class Hundur:
    def __init__(self, nafn, aldur):
        self.nafn = nafn
        self.aldur = aldur

    def __str__(self):
         return f"Nafn: {self.nafn}, aldur: {self.aldur}"
    
    def gelt(self):
        return  "\nvoff"

def main(gelt = False):  
    dog = Hundur("Böðvar", "81")
    print (dog, dog.gelt()) if gelt == True else print(dog) 

svar = input("langar þér að hann Böðvar hinn hrikalegi gelti á þig? j eða n ")

if svar.lower() == "j":
    main(True)
else:
    main()

#Dæmi 2
class Nemandi:
    def __init__ (self, einkunn = 10):
        self.einkunn = einkunn
    

    def hækka_einkunn(self):
        self.einkunn += 10

    def lækka_einkunn(self):
        self.einkunn -= 10        

    def __str__(self):
        return f"Einkunn hjá nemenda er {self.einkunn} "

bob = Nemandi()
print (f"normal {bob}")

bob.hækka_einkunn()
print (f"hækkar {bob}")

bob.lækka_einkunn()
print (f"lækkar {bob}")
#Dæmi C
class Ferhyrningur:
    def __init__ (self, lengd, breidd):
        self.lengd = lengd
        self.breidd = breidd
    
    def flatarmál(self):
        return self.breidd*self.lengd

    def ummál(self):
        return ((self.breidd + self.lengd )*2)

    def __str__(self):
        return f"Lengd: {self.lengd}, breidd: {self.breidd}"

def main():
    kassinn = Ferhyrningur(5, 5)
    print (kassinn)
    ummal = kassinn.ummál()
    print (f"Ummálið er: {ummal}")
    print (f"Flatarmálið er: {kassinn.flatarmál()}")
main()












class Hundur:
    def __init__(self, nafn, aldur):
        self.nafn = nafn
        self.aldur = aldur

    def __str__(self):
        return f"Nafn: {self.nafn}, aldur: {self.aldur}"
    
    def gelt(self):
        return print ("voff")

def main(gelt = False): # Næ ekki að fá geltið eftir hundinn. 
    dog = Hundur("Böðvar", "81")
    return print (dog.gelt() , dog) if gelt == True else print(dog) 

svar = input("langar þér að hann Böðvar hinn hrikalegi gelti á þig? j eða n ")

if svar.lower() == "j":
    main(True)
else:
    main()
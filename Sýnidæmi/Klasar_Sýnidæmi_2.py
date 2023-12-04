# gerum klasann ferhyrning en nú með lengd og breidd sem "einka" breytum
class Ferhyrningur:
    # smiður
    def __init__(self, lengd, breidd):
        self.__lengd = lengd
        self.__breidd = breidd
    # strengja útgáfa (á ensku representation) af klasanum
    def __str__(self):
        return "Lengd: {}, Breidd: {}".format(self.__lengd, self.__breidd)
    # fall til að reikna flatarmálið
    def flatarmál(self):
        return self.__lengd*self.__breidd
    # getter fyrir lengd
    def get_lengd(self):
        return self.__lengd
    # getter fyrir breidd
    def get_breidd(self):
        return self.__breidd
    # setter fyrir lengd
    def set_lengd(self, lengd):
        self.__lengd = lengd
    # setter fyrir breidd
    def set_breidd(self, breidd):
        self.__breidd = breidd


fer1 = Ferhyrningur(2, 3)
print("Nú er flatarmálið: ", fer1.flatarmál())
# línan hér á eftir myndi ekki virka því við gerðum breytuna að prívat breytu
#print("Lengdin er: ", fer1.__lengd)
# næsta lína virkar að vísu en þetta er ekki heppileg leið til að fá lengdina
print("Lengdin er: ", fer1._Ferhyrningur__lengd)
# betra er að nota get fallið
print("Lengdin er: ", fer1.get_lengd())
# ef við viljum breyta lengdinni þá er réttast að nota setterinn
fer1.set_lengd(5)
print("Lengdin er: ", fer1.get_lengd())
print("Nú er flatarmálið: ", fer1.flatarmál())

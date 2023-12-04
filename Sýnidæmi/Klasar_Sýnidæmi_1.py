# við gerum klasann Person en tilvik af honum hefur nafn, aldur og kyn
class Person:
    # smiðurinn/constructorinn
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    # strengjaútgáfan af klasanum
    def __str__(self):
        return "Nafn: {}, Aldur: {}, Kyn: {}".format(self.name, self.age, self.gender)

# aðalforritið okkar býr til tilvik af klasanum og vinnur svo með tilvikin
def main():
    Sveinn = Person("Sveinn", 40, "kk")
    Grýla = Person("Grýla", 1000, "kvk")
    Jólakötturinn = Person("Jólakötturinn", 1000, "kk")
    print(Sveinn)
    print(Grýla)
    print(Jólakötturinn)

    print(Sveinn.__class__)

# keyrum aðalforritið
main()



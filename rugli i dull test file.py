# text = ""

# while(len(text) < 1):
#     text = input("Sláðu inn texta: ")

# if text.isdigit():
#     print("Textinn inniheldur bara tölustafi")
# elif text.isalpha():
#     print("Textinn inniheldur bara bókstafi")
# else:
#     print("þú ert kex")

# if __name__ == '__main__':
#     n = int(input())
#     string = ""

#     for i in range(1, n):
#         string = string +str(i)

#     print (string)

# listinn = [[], [], []]

# for t in range(9):
#     if t % 2 == 0:
#         listinn[t%3].append("X")
#     if t % 2 != 0:
#         listinn[t%3].append("O")
# for x in range(3):
#     print (*listinn[x], sep="")


class hundur:
    def __init__(self, nafn, aldur):
        self.nafn = nafn
        self.aldur = aldur

    def gelt(self):
        print("Voff!")

snati = hundur("Snati", 5)

print(snati)

snati.gelt()


































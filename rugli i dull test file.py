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


skjal1 = "Borges.txt"
skjal2 = "Tesla.txt"

ordin_borges = []
ordin_tesla = []

with open(skjal1, "r") as file:
    tempList = file.read().split()
for temp in tempList:
    ordin_borges.append(temp.strip(".").strip(","))
ordin_borges_set = set(ordin_borges)

with open(skjal2, "r") as file:
    tempList = file.read().split()
for temp in tempList:
    ordin_tesla.append(temp.strip(".").strip(","))
ordin_tesla_set = set(ordin_tesla)

ordin_snid_set = ordin_borges_set & ordin_tesla_set

print("Orðin sem eru í báðum skránum:")
for ord in ordin_snid_set:
    print(ord)




































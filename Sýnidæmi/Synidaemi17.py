
kvedja = "Hallo heimur!"
print(kvedja[-1])
print(kvedja[-2])
print(kvedja[-3])
# i python er lika haegt ad nalgast stok aftanfra
print("---------------")
for i in range(len(kvedja)-1, -1, -1):
    print(kvedja[i])
print("---------------")
for i in reversed(kvedja):
    print(i)


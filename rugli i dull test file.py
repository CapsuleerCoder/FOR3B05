#Dæmi 7
diction_words = {}
with open("HanSolo.txt", "r") as file:
    for line in file:
        new_line = line.lower().replace(",", "").replace(".", "").replace("?", "").split()
        for i in new_line:
            if i in diction_words:
                diction_words[i] += 1
            else:
                diction_words[i] = 1
            print (i)
summa = sum(diction_words.values())            
counter_above_1 = 0
for i in diction_words.values():
    if i > 1:
        counter_above_1 += 1
print (f"Orða sem koma oftar en einu sinni: {counter_above_1}")
print (f"total orð: {summa}")











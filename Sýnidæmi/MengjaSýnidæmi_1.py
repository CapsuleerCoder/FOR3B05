
mengi_1 = set()

with open("Tesla.txt", "r") as skráin_tesla:
    for lína in skráin_tesla:
        snyrt_lína = lína.replace(".", "").replace(",", "")
        orðalisti = snyrt_lína.split()
        for orð in orðalisti:
            mengi_1.add(orð)

print(mengi_1)

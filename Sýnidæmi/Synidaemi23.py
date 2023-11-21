# við opnum skrána með open fallinu og það er góð venja að loka henni aftur með close
skráin_mín = open("Synidaemi23.txt", "r")
for line in skráin_mín:
    print(line, end="")
skráin_mín.close()

# en við getum líka notað "with" lykilorðið og það er stundum þægilegra
with open("Synidaemi23.txt", "r") as skráin_mín:
    for line in skráin_mín:
        print(line, end="")

ny_skra = open("Nytt_Skjal.txt", "w")
ny_skra.write("To write or not to write, that is the question.\n")
#hér má líka gera eins og sést í næstu línu
#print("To write or not to write", file=ny_skra)
ny_skra.close()

# hvað gerist ef við virkjum/afkommentum næstu línur og keyrum forritið svo?
# jú það skrifar yfir, við verðum að passa okkur á því að "w" möguleikinn yfirskrifar allt skjalið
# til að bæta aðeins við og yfirskrifa ekki er hentugt að nota "a+"
"""
ny_skra = open("Nytt_Skjal.txt", "w")
ny_skra.write("This above all, too thine own self be true.")
ny_skra.close()
"""


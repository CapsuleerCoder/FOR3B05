
# Þetta sýnidæmi sýnir hvernig gildissvið (á ensku scope) breytu virkar í Python
# Python hefur svokallað function scope eða fallagildissvið en það þýðir að gildissvið breytu
# er global/víðvært nema hún sé gerð inni í falli en þá er gildissviðið local/staðvært inni
# í fallinu.
name = "Sveinn"

def say_hello():
    # breytan name er víðvær/global og við höfum aðgang að henni inni í fallinu
    print("Hello", name)
    local_breyta = 5

# hinsvegar myndum við ekki geta keyrt eftirfarandi skipun vegna þess að hún er staðvær/local
# og við höfum þess vegna ekki aðgang að henni þegar við erum ekki stödd inni í fallinu, 
# prófið að taka # af næstu línu og keyra svo forritið til að sjá hvað gerist
#print(local_breyta)

def change_my_name(new_name):
    # ef við hefðum sleppt línunni sem segir global name þá hefðum við gert nýja breytu
    # sem hefði staðvært gildissvið og víðværa breytan name hefði ekki breyst
    # prófið að setja # fyrir framan global name og sjáið hvað say_hello() fallið 
    # gerir þá.
    global name
    name = new_name    

say_hello()
change_my_name("Arnar")
say_hello()

tala1, tala2 = 2, 3

def add_and_plus_one(stiki1, stiki2):
    # stiki1 verður nú 3
    stiki1 += 1
    # summan af 3+3 er 6
    return stiki1 + stiki2

print(add_and_plus_one(tala1, tala2))
# en raunstikinn tala1 er óbreyttur, skipunin stiki1 += 1 breytti ekki raunstikanum
print(tala1, tala2)



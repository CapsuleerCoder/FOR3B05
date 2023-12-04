# Svona gerir maður tóma orðabók
bók = {}
print("Tóma bókin er þessi: ", bók)

# svona má gera orðabók með lyklum þar sem lyklarnir eru númer
bók_númeralyklar = {1: "Háskólinn", 2: "Í", 3: "Reykjavík"}
print("Bókin er þessi: ", bók_númeralyklar)

# en það má líka gera bók þar sem lyklarnir eru strengir, eða ýmist tölur eða strengir
# gildin mega líka vera hvort sem er tölur eða strengir
bók_allskonarlyklar = {"Nafn": "Sveinn", 1: "Kennari", "Aldur": 40}
print("Bókin er þessi: ", bók_allskonarlyklar)

# dæmi um litla símaskrá
símaskrá = {"Sveinn Arnar Stefánsson": 7723954, "Jón Jónsson": 5812345}
print("Símaskráin er: ", símaskrá)
print("Síminn hans Sveins er: ", símaskrá["Sveinn Arnar Stefánsson"])

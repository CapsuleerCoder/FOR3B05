
# oft viljum við að fallið skili einhverri breytu/gildi og þá notum við lykilorðið return
# fallið skilar þá því sem kemur á eftir return og hættir keyrslu sinni, þannig að ef 
# það er einhver kóði eftir þegar fallið kemur að return þá verður restin af kóðanum
# í fallinu ekki keyrður.
def return_hallo():
    return "Hallo"

# fallakallið skilar nú "Hallo" inn í breytuna heilsa
heilsa = return_hallo()
# innihald heilsa er þá "Hallo" eins og sést ef við prentum heilsa út
print(heilsa)

# hér er fall sem finnur hvor af 2 tölum er stærri, takið eftir að þó hér komi return 
# tvisvar fyrir þá verður aldrei nema annað þeirra keyrt
def max_of_two(x, y):
    if x > y:
        return x
    return y

tala1, tala2 = input("Sladu inn tölu: "), input("Sladu inn aðra tölu: ")
print("Stærri talan er: ", max_of_two(tala1, tala2))


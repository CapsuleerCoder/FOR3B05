
teljari = 1
while teljari < 6:
    print(teljari)
    teljari+=1
# a medan gildi breytunnar teljari er minna en 6 ta verdur ny umferd i lykkjunni keyrd
# svo haekkum vid teljarann alltaf um 1 svo hann muni einhvern timan verda 6
# tegar tad gerist ta haettir lykkjan
print("----------------")

teljari = 1
while teljari < 6:
    if teljari == 3:
        break
    print(teljari)
    teljari+=1
# ef forritid keyrir break skipun ta haettir lykkjan
print("----------------")

teljari = 1
while teljari < 6:
    if teljari == 3:
        teljari+=1
        continue
    print(teljari)
    teljari+=1
# ef forritid keyrir continue skipun ta hoppum vid yfir restina af blokkinni (i raun yfir 
# ta umferd lykkjunnar) og holdum afram med naestu umferd.
# Athugid ad her kemur linan: teljari+=1 sem haekkar teljarann um 1 fyrir tvisvar, hvers vegna?
# Hvad gerist ef tid strokid ut teljari+=1 inni i if setningunni og keyrid? Hvers vegna aetli
# tad se?




    


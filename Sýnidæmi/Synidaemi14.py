
# Hvad ef vid viljum vixla innihaldi tveggja breyta? Tad getur verid floknara en 
# madur gaeti fyrst haldid eins og eftirfarandi daemi synir.

heiltalaA = 2
heiltalaB = 3
# Nu skulum vid vixla svo A verdi 3 og B verdi 2

heiltalaA = heiltalaB
heiltalaB = heiltalaA
print(heiltalaA) # aettum ad fa 3
print(heiltalaB) # aettum ad fa 2
# Hvad gerdist? Vid faum ad A og B seu badar 3!
# Ju, i linunni: heiltalaA = heiltalaB ta skrifudum vid B yfir A svo tvisturinn sem var i A
# tapadist. Nu skulum vid lita a hvernig ma vixla a rettan hatt en til tess turfum vid
# tridju breytuna til ad vardveita timabundid gildid i A

print("-------------------")
heiltalaA = 2
heiltalaB = 3
temp = heiltalaA
heiltalaA = heiltalaB
heiltalaB = temp
print(heiltalaA) # aettum ad fa 3
print(heiltalaB) # aettum ad fa 2




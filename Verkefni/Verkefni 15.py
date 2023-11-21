def sum_of_three(num1, num2, num3):
    return ((num1+num2+num3))
def prófa_bil(tölu, upphaf, endir):
    for i in range(upphaf, endir+1):
        if i == tölu:
            return "\nTalan er á bilinu"
    return "\nTalan er ekki á bilinu"
def factorial(hopm):
    tala = 1
    for x in range(1, hopm+1):
        tala *= x
    return (tala)

answer = "J"
while answer.lower() != "n":
    print ("\nýttu á 1 til að sjá summu þriggja talna ")
    print  ("ýttu á 2 til að sjá hvort tala sé a bili")
    print ("Ýttu á 3 til að slá inn tölu og sjá summu hennar ef hún er hrópmerkt! ")
    answer = input("Eða sláðu inn n ef þér leiðist: ")
    if answer == "1":
        print ("Summa af þrem tölum")
        print(sum_of_three(int(input("Sláðu inn tölu. ")),(input("Sláðu inn tölu 2. ")), (input("Sláðu inn tölu 3. ")) ))
    if answer == "2":
        print ("Prófa hvort tala er á bili")
        print (prófa_bil(int(input("Sláðu inn tölu: ")), int(input("SLáðu inn byrjun á bili: ")), int(input("Sláðu inn enda á bili: "))))
    if answer == "3":
        print ("Sláðu inn tölu til að sjá hvað hún er hrópmerkt")
        print (factorial(int(input("Sláðu inn tölu til að sjá summu hennar ef hún væri hrópmerkt"))))



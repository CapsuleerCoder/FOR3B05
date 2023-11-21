#16b

#Dæmi 1 fallið meðlimur í lista
def member(number_input):
    list1 = [6, 5, 4, 3]
    if number_input in list1:
        return f"{number_input} er í listanum."
    else:
        return f"{number_input} er ekki í listanum."
def elements(list_size):
    rit = []
    leng = list_size
    for i in range(list_size):
        single = int(input(f"we need {leng} more, Input an int: "))
        leng -= 1
        rit.append(single)
    return rit
def summ(list_size):
    rit = []
    leng = list_size
    for i in range(list_size):
        single = int(input(f"we need {leng} more, Input an int: "))
        leng -= 1
        rit.append(single)
    return rit
def averg(size):
    listin = []
    total = 0
    for i in range(size):
        svar =int(input("Sláðu inn tölu: "))
        listin.append(svar)
    for x in listin:
        total += x
    return total/size
def highest(size):
    listin = []
    for x in range(size):
        svar = int(input("Sláðu inn tölu í listann: "))
        listin.append(svar)
    max = listin[0]
    for i in listin:
        if i > max:
            max = i
    return max



answer = "J"
while answer.lower() != "n":
    print ("Type 1 for checking if number is in list. ")
    print ("Type 2 for making a list. ")
    print ("Type 3 for making a list and seeing the sum of it")
    print ("Type 4 for making a list and seeing the average of it ")
    print ("Type 5 for making a list and getting the max value of it back ")
    answer = input(":") 
    if answer == "1":
        print ("Now we are going to accept an input number and check if its in our list")
        function_number = int(input("input your number: "))
        svar = member(function_number)
        print (svar)
    if answer == "2":
        size = int(input("How big a list do you want? be careful, you have to input the list manually."))
        list_after = elements(size)
        print (list_after)
    if answer == "3":
        size = int(input("How big a list do you want? be careful, you have to input the list manually."))
        list_after = elements(size)
        print (list_after)
        summa = 0
        for i in list_after:
            summa += i
        print (f"Sum of the list is {summa}")
    if answer == "4":
        size = int(input("How big a list do you want? "))
        abaddon = averg(size)
        print (abaddon)
    if answer == "5":
        size = int(input("How big a list you want you userman: "))
        tempest = highest(size)
        print (tempest)






















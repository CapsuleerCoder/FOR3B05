def sum_of_two(num1, num2):
    return num1+num2
def subtract(num1, num2):
    return num1-num2
def circle(radius):
    return radius * 3.14*2
def area_of_rectangle(length, height):
    return length*height
answer = "j"
while answer.upper() != "N":
    answer = input("Sláðu inn 1-4 fyrir dæmi, skrifaðu n til að fara úr forriti  ")
    if answer == "1":
        print ("Summa"); print (sum_of_two(int(input("Sláðu inn tölu: ")), int(input("Sláðu inn aðra tölu: "))))  
    elif answer == "2":
        print ("Mismunur"); print (subtract (int(input("Sláðu inn tölu: ")), int(input("sláðu inn tölu til að draga frá fyrri: "))))
    elif answer == "3":
        print ("Ummál hrings"); print (circle(int(input("Sláðu inn radíus  til að fá ummálið: "))))
    elif answer == "4":
        print ("Flatarmál ferhyrnings "); print (area_of_rectangle(int(input("Sláðu inn lengd ferhyrnings: ")), int(input("Sláðu inn hæð hans: "))))

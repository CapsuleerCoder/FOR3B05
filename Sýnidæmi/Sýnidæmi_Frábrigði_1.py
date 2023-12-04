
try:
    with open("EinhverSkráSemErEkkiTil.txt", "r") as skrá_inn:
        for line in skrá_inn:
            print(line)
# næstu tvær línur sýna hvernig við gætum gert betur og höndlað villur af meiri nákvæmni            
#except FileNotFoundError:
    #print("Þessi skrá er ekki til!")
except:
    print("Einhver villa er í forritinu!")



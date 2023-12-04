import random

class Snowflake():
    # smiður
    def __init__(self):
        self.shape = "+"
        self.position = " "*random.choice(range(1, 100))

    # strengjaútgáfan
    def __str__(self):
        return "Shape is {} , Position is {} .".format(self.shape, self.position)
    
    # fall til að prenta snjókornin
    def printSnowflake(self):
        print(self.position, end="")
        print(self.shape)
    

def main():
    jólasnjór = []
    for i in range(0, 20):
        snjókorn = Snowflake()
        jólasnjór.append(snjókorn)
    
    while True:
        for korn in jólasnjór:
            korn.printSnowflake()

    
main()


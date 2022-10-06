import random
val = ["sten", "sax", "påse"]
riggat = val
scoreboard = []

siffra = 0
_continue = "y"
while True:
    if _continue == "Y" or _continue == "y":
        print("Tree rundor...")
        for i in range (0, 3):
            random.shuffle(riggat)
            riggat = (riggat[:1])
            i += 1

            user_Choice = int(input("Sten = 1, Sax = 2 eller Påse = 3 \n Svar --> ")) - 1
            if val[user_Choice] == val[0] and riggat == val[1] or val[user_Choice] == val[1] and riggat == val[2] or val[user_Choice] == val[2] and riggat == val[0]:
                print("Du vann rundan")
                scoreboard.append("Användare")

            elif val[user_Choice] == val[0] and riggat == val[2] or val[user_Choice] == val[2] and riggat == val[1] or val[user_Choice] == val[1] and riggat == val[0]:
                print("Dator vann rundan")
                scoreboard.append("NPC")

            elif val[user_Choice] == riggat:
                print("Draw")
                scoreboard.append("Draw")
            # else: 
            #     print("Skriv ett giltigt svar", end=" ")
            
    _continue = input("Köra igen? Y/n \n Svar --> ")
    if _continue == "n" or _continue == "N":
        for j in scoreboard:
            siffra += 1
            print(siffra," ", j)
        quit()
    else:
        print("Skriv ett giltigt svar", end= " ")
    


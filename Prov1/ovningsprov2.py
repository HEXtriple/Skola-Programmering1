from operator import truediv
import random
from traceback import print_tb

test = "abcdefgh"
print(test[9:0:-1])


#A upg
mojliga_ord = ["katt", "hund", "flugabzz"]
bokstav = ""
bokstavs_lista = ""
felgissningar = ""
valt_ord = random.choice(mojliga_ord)

dolt_ord = ""
for i in valt_ord:
    dolt_ord += "*"

while True:
    print(f"Längden på ordet är: {len(valt_ord)}")
    print(f"Felgissningar: {felgissningar}")
    print(dolt_ord)
    bokstav = str(input("Ange gissning -->")).lower()

    if bokstavs_lista.count(bokstav) > 0:
        print("Redan använt denna bokstav")
    elif bokstav in valt_ord:
        print("Korrekt!")
        for i in range(0, len(valt_ord)):
            if bokstav == valt_ord[i]:
                dolt_ord = dolt_ord[:i] + bokstav + dolt_ord[i+1:]

    else:
        felgissningar += f"{bokstav}_"
    bokstavs_lista += bokstav
    
    print("-------------------------------- \n\n")

    if dolt_ord == valt_ord:
        print("Du Vann!")
        break
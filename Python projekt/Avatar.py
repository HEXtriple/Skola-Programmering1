from asyncore import loop
from pickle import TRUE
import random
from tkinter.tix import InputOnly
import time

loopNamn = True
loopFarg = True
loopStyrka = True
loopPronomen = True
animalChecked = False
preConfigNamn = ["Loke", "Roids Monstret", "Lorem Ipsum", "Ööööööh kappe", "Hoges"]

antalDjur = ["katt", "hund", "råtta", "fågel", "fisk", "kanin", "sköldpadda", "marsvin", "orm", "rysk Björn"]
mestKraftfullaDjuret = 0

farg = "Blå"


print("Welcome to character-creator.com")
while True:
    antalForsok = 0
    while loopNamn == True:
        print(" \n ------------------------------------------")
        print(f"(Försök kvar {2 - antalForsok})")
        antalForsok += 1
        print("Skriv in ett namn")
        Namn = input("Input:")

        if antalForsok == 2:
            print("Du får nu ett eget genererat namn")
            Namn = preConfigNamn[random.randint(0, len(preConfigNamn))]
            loopNamn = False
        elif (len(Namn) >= 20) or len(Namn) == 0:
            print("För många / för få bokstäver, välj ett nytt namn")
            continue
        else: loopNamn = False
    print(f"Du har valt: {Namn}")
    time.sleep(1)
    while loopFarg == True:
        print(" \n ------------------------------------------")
        print("Välj en färg")
        fargKontroll = input("Röd eller Blå: ")
        if fargKontroll == "Röd" or "Blå":
            loopFarg = False
        else: print("Var god och välj en giltig färg"); continue

    print(f"Perfekt, ditt val är... {farg}")
    time.sleep(1)

    while loopStyrka:
        mestKraftfullaDjuret = antalDjur[random.randint(0, len(antalDjur))]
        print(" \n ------------------------------------------")
        print("Nu ska du välja styrka")
        print("FavoritDjur?")
        print(f"Välj mellan {antalDjur}")
        favvoDjur = input("Välj:")

        if favvoDjur == mestKraftfullaDjuret:
                styrkaNiva = random.randint(40, 100)
                loopStyrka = False
                break
        elif len(favvoDjur) == 0:
            print("välj ett giltigt djur")
            continue
        else:
            for i in antalDjur:
                if favvoDjur == i:
                    animalChecked = True
                    break
                else: animalChecked = False; continue
        if animalChecked == True:
            styrkaNiva = random.randint(0, 60)
            loopStyrka = False
            break
        else: antalDjur.append(favvoDjur); continue
    print(f" {favvoDjur} tillagd")
    time.sleep(3)
    print("\n ------------------------------------------")
    print(f"Du heter {Namn} och röstar på {farg}, din nuvarande styrkenivå är {styrkaNiva} eftersom du har en {favvoDjur} som djur")
    print("------------------------------------------")
    print(antalDjur)
    break


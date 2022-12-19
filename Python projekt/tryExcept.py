def Loke():
    try:
        KappeMfsBeLike = int(input("Gib tälj -->"))
        Snurr = int(input("Gib Nämn -->"))
        print(KappeMfsBeLike/Snurr)
    except ValueError:
        print("ööööööh")
    except ZeroDivisionError:
        print("ummmmmm")
    except:
        print("idk man, jus figure it oyut")
Loke()
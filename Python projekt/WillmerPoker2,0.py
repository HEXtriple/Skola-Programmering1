def Poker():
    while True:
        print("""Alternativ: \n
                1. Fold
                2. Check
                3.Raise \n Välj 2 """)
        
        for i in range(2):
            try: 
                Snurr = int(input(f"Val {i + 1} av 2st --> "))
                if Snurr == 1:
                    print("Fold")
                elif Snurr == 2:
                    print("check")
                elif Snurr == 3:
                    print("Raise")
            except ValueError:
                print("Dumb Fucc")


 
Poker()
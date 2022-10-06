import random; import time 

raderAntal = int(input("antal rader? :: "))
for i in range(raderAntal):
    RandomInt = []
    for f in range(7):
        RandomInt.append(rand.randint(1, 35))
        print(f"numba {f+1} is {RandomInt[f]}")   
    print("-------------")



le_list = list(range(0, 35))
random.shuffle(le_list)
list2 = (le_list[0 : 8])
print(list2)
for i in range(0, 27):le_list.pop()
le_list.sort()

def inspect(le_list): 
        print(le_list); time.sleep(2)
        return #1
def inspectPos(le_list): 
    print(le_list[int(input("Skriv position i listan: "))])
    time.sleep(1)
    return #2
def _add(le_list): 
    le_list.append(int(input("vad vill du lägga till:")))
    time.sleep(1)
    return #3
def remove(le_list):
     le_list.pop(int(input("Skriv en position: ")))
     time.sleep(1)
     return #4
def s_sort(le_list): 
    le_list.sort(); print(le_list)
    time.sleep(1)
    return #5
def _sum(le_list): 
    print(sum(le_list)/len(le_list))
    time.sleep(1)
    return #6

while True:
    print("Vad vill du göra? \n")
    print("1. Titta på hela listan    2. Titta på en specifik listposition \n3. Lägga till ett värde i listan   4. Ta bort ett värde i listan \n5. Sortera listan   6. Beräkna listans medelvärde \n7. Avsluta")
    choosingthingy = input("Ditt val: ")
    if int(choosingthingy) == 1: inspect(le_list)
    elif int(choosingthingy) == 2: inspectPos(le_list)
    elif int(choosingthingy) == 3: _add(le_list)
    elif int(choosingthingy) == 4: remove(le_list)
    elif int(choosingthingy) == 5: s_sort(le_list)
    elif int(choosingthingy) == 6: _sum(le_list)
    elif int(choosingthingy) == 7: quit()
    else: print("Inte ett val, men...", end=" "); continue
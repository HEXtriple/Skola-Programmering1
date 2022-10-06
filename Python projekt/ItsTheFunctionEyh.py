import random as rand

the_list = list(range(1, 50)); new_list = []
for i in the_list: 
    if i % 2 == 0: new_list.append(i)
print(new_list)

def is_prime(a_number):
    if a_number==2 or a_number == 3:
        return True
    if a_number % 2 == 0 or a_number<2:
        return False
    else:
        return True
print(is_prime(13))

# def spela():
#     theTal = rand.randint(1, 100)
#     antalGissningar = 0

#     while True:
#         antalGissningar += 1
#         Gissning = int(input("Speak! :: "))
#         if Gissning == theTal:
#             print("gut")
#             print(f"antal gissningar: {antalGissningar}")
#             break
#         if Gissning < theTal:
#             print("to smol")
#             continue
#         elif Gissning > theTal:
#             print("soOOOooo big")
#             continue
#         else:
#             print("whut")
#             continue
#     return antalGissningar

# print(f"du klarade det på antal {spela()} försök")


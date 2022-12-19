#C upg
def FlugaBzz(siffra):
    if siffra % 5 == 0 and siffra% 3 == 0:
        return "Fizz Buzz"
    elif siffra % 3 == 0:
        return "Fizz"
    elif siffra % 5 == 0:
        return "Buzz"
    else:
        return siffra
for i in range(1, 101):
    Result = FlugaBzz(i)
    print(Result)

#C upg 2
ASLI = "bcdfghjklmnpqrstvwxz"
def ASLINATOR6000(stri):
    new_str = ""
    for i in stri:
        if i in ASLI:
            new_str += f"{i}o{i}"
        else:
            new_str += i
    return new_str
print(ASLINATOR6000("Alfons!".lower()))


#A upg Run Length Encoding

def RLE2000(not_compressed):
    bokstav_lista = ""
    compressed = ""
    for i in not_compressed:
        if i in bokstav_lista:
            continue
        else:
            recurring = not_compressed.count(i)
            if recurring <= 1:
                compressed = compressed + i
            else:
                compressed = compressed + f"{recurring}{i}"
            bokstav_lista = bokstav_lista + i
    return compressed
print(RLE2000("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"))

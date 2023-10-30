# Napisz funkcję która powie czy podana liczba jest liczbą pierwszą.

# pokazuje jkaie liczby w liscie pierwsze

liczby = [-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13]

import math
def czy_to_liczba_pierwsza(liczba):
    if liczba < 2:
        return False
    if liczba == 2:
        return True  # 2 jest liczbą pierwszą
    if liczba % 2 == 0:
        return False  # odrzuć parzyste liczby
    i = 3
    while math.sqrt(liczba) >= i:
        if liczba % i == 0:
            return False
        i += 2
    return True



def sprwdz_ktore_pierwsze(lst):
    for el in lst:
        print(f"{el} --- {czy_to_liczba_pierwsza(el)}")


sprwdz_ktore_pierwsze(liczby)



# ile liczb jest pierwszych w liscie


def ile_liczb_pierwszych(lst):
    ile = 0
    for el in lst:
        if czy_to_liczba_pierwsza(el):
            ile += 1
    return ile


print(ile_liczb_pierwszych(liczby))

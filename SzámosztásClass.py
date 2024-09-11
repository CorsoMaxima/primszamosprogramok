from prime_numbers_class import prímszámtábla

def SzámOsztás(szám: int):
    prím = ""
    while szám > 1:
        for osztó in prímszámtábla:
            if szám % osztó != 0:
                continue
            
            prím += f"{osztó}, "
            szám /= osztó
            print(f"{szám} {osztó}")
            break
    
    return prím 
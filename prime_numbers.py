import sympy
import prime_numbers_class

primenumbers = []
szám = 2

while szám < 9999:
    if szám <= 1:
        szám += 1
        continue
    
    foundPrime = True
    for Osztó in primenumbers:
        if szám % Osztó != 0:
            continue
        
        foundPrime = False
        break
    
    if not foundPrime:
        szám += 1
        continue
    
    primenumbers.append(szám)

print("first part done")
for szám in primenumbers:
    if sympy.isprime(szám):
        continue
    
    print(f"well thats unexpected {szám}", sep="\n")
    primenumbers.pop(primenumbers.index(szám))
    
with open("prime_numbers_class.py", "w") as file:
    file.write(f"prímszámtábla = {primenumbers}")
from prime_numbers_class import prímszámtábla
from SzámosztásClass import SzámOsztás

elsőszám = int(input("\nelsőszám "))
másodikszám = int(input("másodikszám "))

elsőprím = SzámOsztás(elsőszám)
másodikprím = SzámOsztás(másodikszám)

elsőprímtáblázat = elsőprím.split(", ")
másodikprímtáblázat = másodikprím.split(", ")

vegleges = ""
for többszörös in prímszámtábla:
    osztó1 = elsőprímtáblázat.count(str(többszörös))
    osztó2 = másodikprímtáblázat.count(str(többszörös))
    
    if osztó1 == 0 and osztó2 == 0:
        continue
    
    if osztó1 < osztó2:
        vegleges += f"{többszörös}^{osztó2}, "
    elif osztó1 > osztó2:
        vegleges += f"{többszörös}^{osztó1}, "
    else:
        vegleges += f"{többszörös}^{osztó2}, "
    
    continue

print(vegleges)
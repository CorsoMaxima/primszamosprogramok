from prime_numbers_class import prímszámtábla
from SzámosztásClass import SzámOsztás

elsőszám = int(input("\nelsőszám "))
másodikszám = int(input("másodikszám "))

elsőprím = SzámOsztás(elsőszám)
másodikprím = SzámOsztás(másodikszám)

elsőprímtáblázat = elsőprím.split(", ")
másodikprímtáblázat = másodikprím.split(", ")

vegleges = ""
for osztó in prímszámtábla:
    osztó1 = elsőprímtáblázat.count(str(osztó))
    osztó2 = másodikprímtáblázat.count(str(osztó))
    
    if osztó1 == 0 or osztó2 == 0:
        continue
    
    if osztó1 > osztó2:
        vegleges += f"{osztó}^{osztó2}, "
    elif osztó1 < osztó2:
        vegleges += f"{osztó}^{osztó1}, "
    else:
        vegleges += f"{osztó}^{osztó2}, "
    
    continue

print(vegleges)
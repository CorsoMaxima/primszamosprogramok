szám = int(input("\nszám"))
rendszer = int(input("milyen számrendszerben?"))

eddigieredmeny = ""
while szám != 0:
    eddigieredmeny += str(szám % rendszer)
    print(f"{szám // rendszer} x {rendszer} + {szám % rendszer}")
    szám //= rendszer
    
print(eddigieredmeny[::-1])
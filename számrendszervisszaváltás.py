szám = input("\nszám")
rendszer = int(input("milyen számrendszerben van az a szám?"))
# 10-es számrendszerbe való visszaváltás

forma = "0"
for számhanyadik in range(len(szám)):
    forma += f" + {szám[0]} * {rendszer ** számhanyadik}"

print(eval(forma))
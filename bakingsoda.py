import string
n:int = int(input("Times: "))
for i in range(n):
    g: float = float(input("Grams of Baking Soda: "))
    print(str(g/84.0) + "g/mol")
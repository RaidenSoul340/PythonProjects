print("#==========================#")
print("DÉCIMO TERMOS DE UMA P.A")
print("#==========================#")

pt = int(input("Digite o Primerio Termo: "))
r = int(input("Digite a razão: "))
decimo = pt + (10-1) * r
for c in range(pt, decimo + r, r):
    print("{}".format(c), end="-> ")
print("FIM")
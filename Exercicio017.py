from math import hypot

co = float(input("Digite o numero do cateto oposto: "))
ca = float(input("Digite o cateto da adjacente:"))
h = (ca**2 + co**2) **(1/2)
hi = hypot(co, ca)

print("O valor da hipotenusa é: {:.2f}".format(hi))
#Maneira com o "import"

#print("A hipotenusa é: {:.2f}".format(h))
#Maneira tradicional
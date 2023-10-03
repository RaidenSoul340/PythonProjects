from random import shuffle

e1 = str(input("Primeiro empregado: "))
e2 = str(input("Segundo empregado: "))
e3 = str(input("Terceiro empregado: "))
e4 = str(input("Quarto empregado: "))
e5 = str(input("Quinto empregado: "))
e6 = str(input("Sexto empregado: "))
e7 = str(input("Setimo empregado: "))
e8 = str(input("Oitavo empregado: "))
e9 = str(input("Nono empregado: "))
e10 = str(input("Decimo empregado: "))
lista = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]
shuffle(lista)
print("A ordem escolhida sera")
print(lista)
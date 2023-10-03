soma = 0
cont = 0

for n in range(0,6):
    n = int(input("Digite um número: "))
    if n % 2 ==0:
        soma +=  n
        cont += 1
print("A soma dos valores pares é {}".format(soma))
print("A quantidade de números pares é {}".format(cont))
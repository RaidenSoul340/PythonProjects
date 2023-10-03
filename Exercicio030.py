numero = int(input("Me diga o número que deseja: "))
resultado = numero % 2
if resultado == 0:
    print("O numero {} é PAR!".format(numero))
else:
    print("O numero {} é IMPAR".format(numero))
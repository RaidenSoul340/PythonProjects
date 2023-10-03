frase = str(input("Digite uma frase: ")).strip().upper()
palavra = frase.split()
tj = "".join(palavra)
inverso = ""
for letra in range(len(tj) -1, -1, -1):
    inverso += tj[letra]
print("O inverso de {} é {}".format(tj, inverso))
if inverso == tj:
    print("Se TEM um PALÍDROMO!")
else:
    print("A frase NÃO TEM UM PALÍDROMO")

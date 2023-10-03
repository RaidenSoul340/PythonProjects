resposta = "S"
soma = quant = media = maior = menor = 0
while resposta == "Ss":
    n = int(input("Digite um número: "))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < manor:
            menor = n
    resposta = str(input("Você deseja continua? [S/N]: "))
media = soma / quant
print("Você digitou {} números e a media foi {}".format(quant, media))
print("O maior valor foi {} e o menor foi {}".format(maior, menor))
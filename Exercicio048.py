soma = 0
cont = 0

for c in range(1, 501, 2):
    if c % 3==0: 
        soma += c
        cont += 1
        
print("O total de valores multiplos de 3 são {}".format(cont))
print("A soma de todos os valores multiplos de 3 são {}".format(soma))

    
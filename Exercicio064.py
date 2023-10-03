n = cont = soma = 0
n = int(input("Digite o qualque número avontade [999 para parar!]: "))
while n != 999:
    soma += n
    cont += 1
    n = int(input("Digite o qualque número avontade [999 para parar!]: "))
    
print("A quatidade números repetidos foram {}".format(cont))
print("A soma de todos esses números é {}".format(soma))
print("FIM")
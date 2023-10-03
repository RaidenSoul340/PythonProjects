from time import sleep
#Importação feita para coloca tempo antes da respota

print("#==========Analisador de Valores==========#")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
print("#=========================================#")
print("ANALISANDO...")
sleep(2)
#Comando dado para coloca um tempo de 1,5s antes da resposta

if n1 > n2:
    print("O PRIMEIRO valor é maior")
elif n2 > n1:
    print("O SEGUNDO valor é maior")
else:
    print("Ambos os valores são IGUAIS")

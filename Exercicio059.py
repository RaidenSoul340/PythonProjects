from time import sleep
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
opção = 0
while opção != 5:
    print("""Escolha uma opção!
    [1] Somar
    [2] Multiplicar
    [3] Maior Valor
    [4] Novos Valores
    [5] Encerrar programa""")
    

    opção = int(input("Digite a opção desejada: "))
    
    if opção == 1:
        soma = n1 + n2
        print("A soma entre {} e {} é {}".format(n1, n2, soma))
    
    elif opção == 2:
        Multiplicação = n1 * n2
        print("A Multiplicação de {} x {} é {}".format(n1, n2, Multiplicação))

    elif opção == 3:
        if n1 > n2:
            maior = n1
        else: 
            maior = n2
        print("O número {} é maior que o número {}".format(n1, n2, maior))

    elif opção == 4:
        n1 = int(input("Digite o Primeiro valor: "))
        n2 = int(input("Digite o Segundo valor: "))

    elif opção == 5:
        print("Finalizando...")

    else:
        print("Opção invalida!! Por favor tente novamente")
    print("#==========================#")
    sleep(2)
print("Fim Do Programa Volte Sempre!!")

        
            
#====Estrutura de repetição while====#

#Enquanto não pega a maçã:
    #pega
#pega

#while not apple:
    #passo
#pega

#while no apple:
    #if chão:
        #passo
    #if buraco:
        #pula
    #if moeda:
        #pega:
#pega
#====================================#

#=============Exercicio==============#

#n = 1
#while n != 0:
    #n = int(input("Digite um Valor:"))
#print("FIM")

#r = "S"
#while r == "S":
    #n = int(input("Digite um valor:"))
    #r = str(input("Deseja continuar? [S/N]: ")).upper()
#print("FIM")

n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("A quantidade de números pares são {} e de números impares são {}.".format(par, impar))







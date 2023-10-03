#==========Condição Parte(1)==========#
#se pessoa.esquerda() = if pessoa esquerda(): [Bloco V] ou [Bloco True]
#senão = else [Bloco F] ou [Bloco False]
#=====================================#

#============Exemplo 01============#
#tempo = int(input("Quantos anos tem o seu carro?"))
#if tempo <=3:
    #print("Seu carro é novo")

#else:
    #print("Seu carro é velho")
#print("===FIM===")
#==================================#

#============Exemplo 02============#
#tempo = int(input("Quantos anos tem o seu carro?"))
#print("carro novo"if tempo<=4 else "carro velho")
#print("===FIM===")
#==================================#

#============Exemplo 03============#
#nome = str(input("Qual o seu nome? "))
#if nome == "João":
    #print("Que nome maravilhoso! ;)")
#else:
    #print("Seu nome é tão normal! :p")
#print("Bom Dia, {}".format(nome))
#==================================#

#============Exemplo 04============#
n1 = float(input("Digite a sua primeira nota: "))
n2 = float(input("Digite a sua segunda nota: "))
m = (n1 + n2)/2
print("A sua nota foi {:.1f}".format(m))

if m>=7.0:
    print("A sua nota foi boa, PARABÉNS!!:D!")
else:
    print("A sua nota foi ruim, ESTUDE+ ;-;")

















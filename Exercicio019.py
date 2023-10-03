from random import choice

a1 = str(input("Digite o nome do primeiro aluno: "))
a2 = str(input("Digite o nome do segundo aluno: "))
a3 = str(input("Digite o nome do terceiro aluno: "))
a4 = str(input("Digite o nome do quarto aluno: "))
a5 = str(input("Digite o nome do quinto aluno: "))
a6 = str(input("Digite o nome do sexto aluno: "))
a7 = str(input("Digite o nome do setimo aluno: "))
a8 = str(input("Digte o nome do oitavo aluno: "))
a9 = str(input("Digite o nome do nono aluno: "))
a10 = str(input("Digite o nome do decimo aluno: "))

lista = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
escolhido = choice(lista)
print("O Aluno escolhido foi {}".format(escolhido))
#Programação feita para sortea uma pessoa entre 10
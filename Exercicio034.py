salario = float(input("Digite o seu salario: "))

if salario >=1250:
    supeiro = salario + (salario * 10/100)
    print("Você teve um aumento de 10%. Seu novo salario é: R${:.2f}".format(supeiro))
else:
    inferior = salario + (salario * 15/100)
    print("Você teve um aumento de 15%. Seu novo salario é: R${:.2f}".format(inferior))
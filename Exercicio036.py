vcasa = int(input("Digite o valor da casa que deseja comprar: R$"))
salario = int(input("Digite o valor de seu salário: "))
tempo = int(input("Dgite o tempo de financiamento:"))
#vcasa = valor da casa
prestação = vcasa / (tempo*12)

print("O valor da casa é R${:.2f} o emprestimo sera de R${:.2f} e o tempo que levara parea ser pago sera {} anos".format(vcasa, prestação, tempo))
print("ANALISANDO...")
if prestação >= (salario*0.3):
    print("O seu emprestimo foi NEGADO!")
else:
    print("O seu imprestimo foi ACEITO!")
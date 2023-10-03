from datetime import date
ano_atual = date.today().year

ano = int(input("Qual o ano você nasceu? "))

idade = (ano_atual - ano)

if idade <= 9:
    print("Você tem {} parabéns sua categoria é MIRIM!".format(idade))
elif idade > 9 and idade <= 14:
    print("Você tem {} parabéns sua categoria é INFANTIL!".format(idade))
elif idade > 14 and idade <= 19:
    print("Você tem {} parabéns sua categoria é JUNIOR!".format(idade))
elif idade > 19 and idade <= 25:
    print("Você tem {} parabéns sua categoria é SÊNIOR!".format(idade))
else:
    print("Você tem {} patabéns sua categoria é MASTER!".format(idade))


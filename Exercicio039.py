from datetime import date

ano_atual = date.today().year


print("#========Alistamento Militar========#")
ano = int(input("Em qual ano você nasceu? "))
print("#===================================#")

idade = ano_atual - ano
print("Quem nasceu em {} tem {} de {}".format(ano, idade, ano_atual))

if idade < 18:
    print("Você ira se alistar em {} ano(s)".format(18 - idade))
    print("Você deverá se alistar em {} ".format(ano_atual + (18-idade)))

elif idade == 18:
    print("Você irá se alistar nesse ano de {}".format(ano_atual))

elif idade > 18:
    print("Você deveria ter se alistado há {} anos".format(idade-18))
    print("Seu alistamento foi em {}".format(ano_atual - (idade - 18)))

from datetime import date

ano = int(input("Digite aqui o Ano. Coloque 0 para analisarmos o ano atual: "))

if ano ==0:
    ano = date.today().year 
if (ano% 4==0 and ano% 100) or (ano%400==0):
    print("O ano {} é BISSEXTO!".format(ano))
else:
    print("Esse ano de {} não é BISSEXTO".format(ano))

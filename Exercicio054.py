from datetime import date

ano = date.today().year

contmaior = 0
contmenor = 0

for pessoas in range(1,8):   
    ano_nasceu = int(input("Digite o ano que nasceu: "))
    idade = (ano - ano_nasceu)    
    if idade >= 21:
        contmaior += 1
    else:
        contmenor+= 1
print("Temos {} de maior idade!".format(contmaior))
print("Temos {} de menor idade!".format(contmenor))
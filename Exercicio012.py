n = float(input("Digite o valor do produto R$"))
d = int(input("Digite o desconto %"))
print("O produtor que custava R${}, na promoção com desconto de %{} vai custar R${}".format(n, d, n*d/100))
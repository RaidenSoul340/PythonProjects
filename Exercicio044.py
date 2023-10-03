print("#======LOJAS RAIDEN======#")
preço = float(input("Digite o preço do produto: R$"))
print("#====FORMAS DE PAGAMENTO====#")
print("[1] à vista/cheque")
print("[2] à vista cartão")
print("[3] 2x no cartão")
print("[4] 3x ou mais no cartão")
print("#===========================#")
opção = int(input("Qual o opção deseja para efetua o pagamento: "))
if (opção ==1):
    total = preço - (0.1 * preço)
elif (opção ==2):
    total = preço - (0.05 * preço) 
elif (opção ==3):
    total = preço
    parcela = total/2
    print(f"Sua compra sera parcelada em 2x de R${parcela} SEM JUROS.")
elif (opçao == 4):
    total = (1 + 0.2)*preço
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc:.1f}x de R${parcela:.2f} COM JUROS.')
else:
  total = preço
  print('OPÇÃO INVÁLIDA de pagamento. Tente novamente.')
print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.')
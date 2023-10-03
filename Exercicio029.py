velocidade = float(input("Quantos foi a velocidade que seu carro estava? "))
if velocidade >80:
    print("MULTADO! Você esxedeu a velocidade permitida que era 80km/h")
    multa = (velocidade-80) * 7
    print("Você deve pagar uma multa de R${:.2f}!".format(multa))
print("Tenha um bom dia! Dirija com cuidado")
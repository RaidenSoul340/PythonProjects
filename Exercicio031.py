distancia = float(input("Digite á distancia da sua viagem: "))
print("Vocês esta presta a viajar uma distancia de {}km".format(distancia))
if distancia<= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print("O preço da sua passagem será R${:.2f}".format(preço))



#distancia = float(input("Digite á distancia da sua viagem: "))
#print("Vocês esta presta a viajar uma distancia de {}km".format(distancia))
#preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
#print("O preço da sua passagem será R${:.2f}".format(preço))
from time import sleep

altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso em (KG): "))


imc = peso / (altura**2)

print("O IMC dessa pessoa é de {:.1f}".format(imc))

if imc < 18.5:
    print("Você esta abaixo do peso!")
elif 18.5 <= imc <25:
    print("Você esta com o peso ideal!")
elif 25 <= imc < 30:
    print("Você esta com sobrepeso!")
elif 30 <= imc < 40:
    print("Você esta com obesidade!")
elif imc >= 40:
    print("Você esta com Obesidade mórbia")
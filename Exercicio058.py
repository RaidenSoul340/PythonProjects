from random import randint 

computador = randint(0, 10)

print("Ola eu sou o seu computador :D")
print("Acabei de pensa em número entre 0 a 10 tente adivinha qual é.")
acertou = False
palpite = 0

while not acertou:
    jogador = int(input("Qual o seu palpite? "))
    palpite += 1
    if jogador == computador:
        acertou = True
    
    if jogador < computador:
            print("Mais... Tente novamente!")
    else: 
         if jogador > computador:
            print("Menos... Tente novamente")
print("Parabéns!! O número de tentativas foi {}".format(palpite))



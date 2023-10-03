from random import randint
from time import sleep #time biblioteca pra tempo; sleep usando para dar tempo entre comandos.

computador = randint(0, 5) #ira fazer o computador escolher um número aleatorio entre 0 e 5
print("=--=" * 15)
print("Vou escolher um numero entre 0 e 5. Tenta adivinhar!")
print("=--=" * 15)
jogador = int(input("Em que número o computador pensou? ")) #O jogador vai escolher um número
print("TO PENSADO CARMA LA...")
sleep(3)
if jogador == computador:
    print("PARABÉNS! Você conseguiu me vencer! ;)")
else:
     print("Eu Ganhei EHEHEH! Eu pensei em {} e você disse {}".format(computador, jogador))
     print("Tente de novo!")
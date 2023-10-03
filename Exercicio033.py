#n = int(input("Digite N: "))
#ma = None
#me = None
#for i in range(n):
   #x = float(input("Digite um número: "))
   #ma = ma if ma != None and ma >  x else x
   #me = me if me != None and me < x else x

#print ('O maior valor digitado foi {} e o menor foi {}'.format(ma,me))

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
# Varifica quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verifica quem é maior 
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O mairo valor é {}!".format(maior))
print("O menor valor é {}!".format(menor))
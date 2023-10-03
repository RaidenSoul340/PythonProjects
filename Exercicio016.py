from math import trunc

num = float(input("Digite um número real: "))
print("A parte inteira do número {} é {} ".format(num, trunc(num)))
#Teste usando o "from math import trunc" / chance de erro nula

print("A parte inteira do número {} é {}".format(num, int(num)))
#Teste da maneira do professor / chance de erro nula

print("A parte inteira {} é {:.0f}".format(num, num))
#Teste da maneira rodrigo / chance de erro 10% se tiver 9 depois da ','
from time import sleep

n = int(input("Digite o número de 0 a 10 e descupra a sua multiplicação: "))


for c in range(0, 11):
    m = (n*c)
    print("{} x {} = {}".format(n, c, m))
    
    

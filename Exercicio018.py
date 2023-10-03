from math import radians, sin, cos, tan

num = float(input("Digite o ângulo que você deseja: "))

s = sin(radians(num))
c = cos(radians(num))
t = tan(radians(num))

print("O ângulo de {} tem o Seno de {:.2f}".format(num, sin(num)))
print("O ângulo de {} tem o Coseno de {:.2f}".format(num, cos(num)))
print("O ângulo de {} tem a Tangente de {:.2f}".format(num, tan(num)))
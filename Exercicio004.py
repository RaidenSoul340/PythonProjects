n = input("Digite algo: ")

print("Qual o tipo? {}".format(type(n)))
print("Tem espaço? ", n.isspace())
print("Tem letra? ", n.isalpha())
print("Tem numero? ", n.isnumeric())
print("Tem em numero e letra? ", n.isalpha())
print("Tem Letra minuscula? ", n.islower())
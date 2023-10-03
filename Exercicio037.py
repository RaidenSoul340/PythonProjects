print("#=========Conversor de Bases Numérica=========#")
print("")
print("[1] Binario ")
print("[2] Octal")
print("[3] Hexadecimal")
print("")
print("#=============================================#")

opçao = str(input("Digite o numero da opção desejada: "))
num = int(input("Digite um número inteiro: "))

if opçao == "1":
    print("O número {} na forma Binaria é {}".format(num,format(num, "b")))
elif opçao == "2":
    print("O número {} na forma Octal é {}".format(num, format(num, "o")))
elif opçao == "3":
    print("O número {} na forma Hexadecimal é {}".format(num, format(num, hex(num))))
else:
    print("Você so tem tem 3 opçoes não inventa mais uma não :P!!")
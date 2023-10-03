sexo = str(input("Informa o seu sexo: [M/F] ")).strip().upper()[0] 
while sexo not in "MmFf":
    sexo = str(input("Dados inválidos!!Por favor digite novamente: ")).strip().upper()[0]
print("O seu sexo é {}, o cadastro foi feito com sucesso!".format(sexo))  

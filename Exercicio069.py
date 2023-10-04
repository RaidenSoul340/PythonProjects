print("="*10)
print("CADASTRO")
print("="*10)
total18 = contH = contM20 = 0
while True:
    idade = int(input("Digite a Idade: "))
    sexo = " "
    
    while sexo not in "MmFf":
        sexo = str(input("Qual o sexo? [M/F]: ")).strip().upper()[0]
        
        if idade >= 18:
            total18 += 1
        
        if sexo == "Mm":
            contH += 1

        if sexo == "Ff":
            contM20 += 1
        
        resposta = " "
    while resposta not in "SN":
        resposta = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]

    if resposta == "N":
        break
print(f"O total de pessoas com 18 anos é {total18}.")
print(f"O total de hoemens cadastrados é {contH}.")
print(f"A quantidade mulheres que tem menos de 20 anos é {contM20}")
print("Volte Sempre!! :D")
            

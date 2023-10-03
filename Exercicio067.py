while True:
    n = int(input("Digite o número e descubra a sua tabuada: "))
    print("=" * 20 )    
    if n < 0:
        break
    for m in range(0, 11):
        print(f"{n} x {m} = {n*m}")
    print("=" * 20)
print("Programa Encerrado! Volte Sempre :D")
print("=" *20)

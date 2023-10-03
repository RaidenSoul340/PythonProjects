n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2)/2

print("A soma das notas {:.1f} e {:.1f} da a média de {:.1f}".format(n1, n2, media))
if media >= 5 and media<=6.9:
    print("Você esta de recuperação ;-; estude mais!")
elif media >= 7:
    print("PARABÉNS você passou de ano! Aproveite as ferias")
elif media <= 5:
    print("Você reprovou, estude mais na próxima ;-;")
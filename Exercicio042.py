from time import sleep
l1 = float(input("Primero segmento: "))
l2 = float(input("Segundo segmento: "))
l3 = float(input("Terceiro segmento: "))

print("=--=" * 8)
print("Analisando trinagulo...")
print("=--=" * 8)
sleep(3)

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    
    print("Os segmentos podem forma um TRIANGULO ",end="")
    if l1 ==l2==l3:
        print("EQUILATERO!")
    
    elif l1 != l2 != l3 != l1:
        print("ESCALENO!")
    
    else:
        print("ISÓSCELES")
else:
    print("Não pode forma um TRIANGULO")
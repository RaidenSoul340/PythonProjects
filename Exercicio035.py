from time import sleep
l1 = float(input("Primero segmento: "))
l2 = float(input("Segundo segmento: "))
l3 = float(input("Terceiro segmento: "))

print("=--=" * 8)
print("Analisando trinagulo...")
print("=--=" * 8)
sleep(3)

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    
    print("Os segmentos assim podem forma um TRIANGULO!")
else:
    print("Os segmentos assim NÃO podem forma um TRIANGULO")
#=======Interrompendo Repetições While=======#

#enquanto Verdadeiro:               while True:
    #se bloco                           if block
        #passo                              passo
    #se espaço                          if jump
        #pula                               pula
    #se moeda                           if coin 
        #pega                               pega
    #se trofeu                          if trouf
        #pula                               pula
        #interrompa                         break
#pega                                 pega

#==================Exercicios==================#

n = s = 0
while True: #Isso deixa os comandos infinitos
    n = int(input("Digite um Número: "))
    if n == 999: #Se digitarem 999 ele ira para o programa
        break #Apos digita 999 ira parar o programa
    s += n #soma dos números
#print("A soma vale {}".format(s))
print(f"A soma vale {s}")
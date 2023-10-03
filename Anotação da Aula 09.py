#====================Manipulando Texto====================#
#Fatiamento =>vai fatiar uma palavra de uma frase
#Análise =>vai analasar o comando

#-------------------------Fatiamento-------------------------#
#Lembra: que o fatiamento tem um numero a menos, então quando fot usar o comando adicinar +1 na hora#
#Lembra: "Frase[9:21:2]" esse "2" vai ser a quantidade de letras que ele vai pular e que seram aceitas#
#Lembra: "Frase[:5]" o comando vai começar do começo e vai termina do slot 5 lembrando que isso vai resulta em um slot a menos
#Lembra: Se usar "Frase[15:]" ele vai começa no slot 15 e vai ate o ultimo slot
#---------------------------------------------------------#

#-------------------------Análise-------------------------#
#Lembra: "len[frase]" vai analisar quantos caracteres tem a frase
#Lembra: "frase.count("o") vai conta quantos "o" tem na frase
#Lembra: "frase.count("o",0,13) vai conta quantos "o" tem na frase começando do "0" e ira termina no "13"
#Lembra: "frase.find("deo")" vai procura todos os slot que terminam com o "deo"
#Lembra: '"curso in frase' vai procurar se a palavra curso esta na frase se tiver mais da como resposta "True"
#---------------------------------------------------------#

#-------------------------Transformação-------------------------#
#Lembra: se usar ".replace(1, 2)" ira substituir o 1 pelo 2.
#Lembra: se usar ".upper()" ira deixa todas as letras maiusculas.
#Lembra: se usar o ".lower()" ira deixa todas as letras em minusculas
#Lembra: se usar ".capitalizer" ira deixa todas as letras minusculas menos a primera letra
#Lembra: se usar o ".title" acada espaço ira transforma as letras em maiusculas
#Lembra: se usar ".strip" todos os espaços em branco desnecessarios seram excluidos.
#Lembra: se usar ".rstrip" ira começa a excluir pela direita
#Lembra: se usar ".lstrip" ira começa a excluir pela esquerda
#---------------------------------------------------------#

#-------------------------Divisão-------------------------#
#Lembra: se usar ".split()" dentro de uma frase ira dividir as palavras formando uma lista nova
#---------------------------------------------------------#

#-------------------------Junção-------------------------#
#Lembra: se usar"'-'.join(frase)" ira junta toda a frase separa com o comando a cima
#---------------------------------------------------------#


#-------------------------Exercicio-------------------------#
frase = "Curso em Video Python"
#print(frase[1::2])
print(frase.upper().count("O"))
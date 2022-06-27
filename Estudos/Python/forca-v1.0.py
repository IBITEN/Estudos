nome = list('aviao')
sorte = []
#for para fazer uma lista com a quantidade de letras que tem no nome
for x in nome:
    sorte.append('-')

print('JOGO DA FORCA\
      \nVocê possui 6 tentativas')
#contador para exibir os traços ao invés das letras.
exibir = 0
while exibir < len(sorte):
        if exibir == (len(sorte)-1):
            print(sorte[exibir])
        else:
            print(sorte[exibir], end=' ')
        exibir +=1
#contador para limite maximo de 6 erros.       
tentativas = 6
while tentativas > 0:
    count2 = 0
    letra = input('qual a letra: ').lower()
    #for = caso a pessoa acerte a letra 
    for x in range(0, len(nome)):
        #condicional para inserir a letra correta no index correto.
        if letra == nome[x]:
            sorte[x] = letra
        elif letra not in nome:
            tentativas -=1
            print(f'Você errou, agora possui {tentativas} tentativas')
            break
    #contador para exibir as letra acertadas.
    exibir = 0
    while exibir < len(sorte):
        if exibir == (len(sorte)-1):
            print(sorte[exibir])
        else:
            print(sorte[exibir], end=' ')
        exibir +=1
    #condicional para saber se a pessoa acertou ou atingiu o limite de erros.
    if tentativas == 0:
        print('Que pena,você perdeu.')
        break
    elif sorte == nome:
        print('Você venceu! Parabéns!')
        break

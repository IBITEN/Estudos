linha = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

linha1_1 = []
linha2_1 = []
linha3_1 = []

print('JOGO DA VELHA \n')
for i in linha:
    linha1_1.append('-')
    linha2_1.append('-')
    linha3_1.append('-')

#função para exibir tabela para exemplificar o jogo da velha.
def exibicao1():    
    exibir = 0
    while exibir < len(linha1_1):
        if exibir == (len(linha)-1):
            print(linha[0][exibir])
        else:
            print(linha[0][exibir], end=' |')
        exibir +=1

    exibir = 0
    while exibir < len(linha2_1):
        if exibir == (len(linha)-1):
            print(linha[1][exibir])
        else:
            print(linha[1][exibir], end=' |')
        exibir +=1
   
    exibir = 0
    while exibir < len(linha3_1):
        if exibir == (len(linha)-1):
            print(linha[2][exibir])
        else:
            print(linha[2][exibir], end=' |')
        exibir +=1
exibicao1()

#função para exibir espaços para marcações e o 'X' e 'O'.
def exibicao():
    exibir = 0
    while exibir < len(linha1_1):
        if exibir == (len(linha)-1):
            print(linha1_1[exibir])
        else:
            print(linha1_1[exibir], end=' |')
        exibir +=1

    exibir = 0
    while exibir < len(linha2_1):
        if exibir == (len(linha)-1):
            print(linha2_1[exibir])
        else:
            print(linha2_1[exibir], end=' |')
        exibir +=1
   
    exibir = 0
    while exibir < len(linha3_1):
        if exibir == (len(linha)-1):
            print(linha3_1[exibir])
        else:
            print(linha3_1[exibir], end=' |')
        exibir +=1

#função para inserir 'X' no jogo.
count = 1
def exibirX():
    global count
    count = 1
    posicao = 0
    posicao = int(input('Qual posição do "X"? ')) 
    if posicao in linha[0]:
        if linha1_1[posicao-1] == 'X' or linha1_1[posicao-1] == 'O':
            exibirX()
        else:
            linha1_1[posicao-1] = 'X'
            count = 0
            exibicao()
            vitoriaX()

    if posicao in linha[1]:
        if linha2_1[posicao-4] == 'X' or linha2_1[posicao-4] == 'O':
            exibirX()
        else:
            linha2_1[posicao-4] = 'X'
            count = 0
            exibicao()
            vitoriaX()
        
    if posicao in linha[2]:
        if linha3_1[posicao-7] == 'X' or linha3_1[posicao-7] == 'O':
            exibirX()
        else:
            linha3_1[posicao-7] = 'X'
            count = 0
            exibicao()
            vitoriaX()


#função para inserir 'O' no jogo.
def exibirO():
    global count
    posicao2 = int(input('Qual posição do "O"? '))
    if posicao2 in linha[0]:
        if linha1_1[posicao2-1] == 'X' or linha1_1[posicao2-1] == 'O':
            exibirO()
        else:
            linha1_1[posicao2-1] = 'O'
            count = 1
            exibicao()
            vitoriaO()
   
    if posicao2 in linha[1]:
        if linha2_1[posicao2-4] == 'X' or linha2_1[posicao2-4] == 'O':
            exibirO()
        else:
            linha2_1[posicao2-4] = 'O'
            count = 1
            exibicao()
            vitoriaO()

    if posicao2 in linha[2]:
        if linha3_1[posicao2-7] == 'X' or linha3_1[posicao2-7] == 'O':
            exibirO()
        else:
            linha3_1[posicao2-7] = 'O'
            count = 1
            exibicao()
            vitoriaO()
        
#função para testar vitória de 'X'.
ganhar = 0      
def vitoriaX():
    
    global ganhar
    ganhar = 0
    if linha1_1[0] == 'X' and linha1_1[1] == 'X' and linha1_1[2] == 'X':
        print('"X" venceu')
        ganhar = 1
    elif linha2_1[0] == 'X' and linha2_1[1] == 'X' and linha2_1[2] == 'X':
        print('"X" venceu')
        ganhar = 1
    elif linha3_1[0] == 'X' and linha3_1[1] == 'X' and linha3_1[2] == 'X':
        print('"X" venceu')
        ganhar = 1
    elif linha1_1[0] == 'X' and linha2_1[0] == 'X' and linha3_1[0] == 'X':
        print('"X" venceu')
        ganhar = 1
    elif linha1_1[1] == 'X' and linha2_1[1] == 'X' and linha3_1[1] == 'X':
        print('"X" venceu')
        ganhar = 1
    elif linha1_1[2] == 'X' and linha2_1[2] == 'X' and linha3_1[2] == 'X':
        print('"X" venceu')
        ganhar = 1
    elif linha1_1[0] == 'X' and linha2_1[1] == 'X' and linha3_1[2] == 'X':
        print('"X" venceu')
        ganhar = 1
    elif linha1_1[2] == 'X' and linha2_1[1] == 'X' and linha3_1[0] == 'X':
        print('"X" venceu')
        ganhar = 1

#função para testar vitória de 'O'.
def vitoriaO():
    global ganhar
    ganhar = 0
    if linha1_1[0] == 'O' and linha1_1[1] == 'O' and linha1_1[2] == 'O':
        print('"O" venceu')
        ganhar = 1
    elif linha2_1[0] == 'O' and linha2_1[1] == 'O' and linha2_1[2] == 'O':
        print('"O" venceu')
        ganhar = 1
    elif linha3_1[0] == 'O' and linha3_1[1] == 'O' and linha3_1[2] == 'O':
        print('"O" venceu')
        ganhar = 1
    elif linha1_1[0] == 'O' and linha2_1[0] == 'O' and linha3_1[0] == 'O':
        print('"O" venceu')
        ganhar = 1
    elif linha1_1[1] == 'O' and linha2_1[1] == 'O' and linha3_1[1] == 'O':
        print('"O" venceu')
        ganhar = 1
    elif linha1_1[2] == 'O' and linha2_1[2] == 'O' and linha3_1[2] == 'O':
        print('"O" venceu')
        ganhar = 1
    elif linha1_1[0] == 'O' and linha2_1[1] == 'O' and linha3_1[2] == 'O':
        print('"O" venceu')
        ganhar = 1
    elif linha1_1[2] == 'O' and linha2_1[1] == 'O' and linha3_1[0] == 'O':
        print('"O" venceu')
        ganhar = 1


print('\n')
exibicao()

while ganhar == 0:
    if count == 1:
        exibirX()
    else:
        exibirO()


    







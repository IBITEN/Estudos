canais = int(input('canais: '))

lista = []
for count in range(0, canais):
    lista.append(input('registre: ').split(';'))

x = float(input('Bonus p/premium: '))
y = float(input('Bonus p/normal: '))

bonus = []
for count in range(0, canais):
    seguidores = lista[count][1]
    seguidores = int(seguidores)
    quant = seguidores/1000
    quant = int(quant)
    if lista[count][3] == 'não':
        valor = quant*y
        bonus.append(valor)
    elif lista[count][3] == 'sim':
        valor = quant*x
        bonus.append(valor)

valores = []
for count in range(0, canais):
    monetizacao = lista[count][2]
    monetizacao = float(monetizacao)
    monetizacao = monetizacao + bonus[count]
    valores.append(monetizacao)  

print('-----\nBÔNUS\n-----')

for count in range(0, canais):
    print(f'{lista[count][0]}: R$ {valores[count]:.2f}')

    
         
        


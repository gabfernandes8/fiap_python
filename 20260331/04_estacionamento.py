# exercicio 4
precoHora = 5.00
precoMax = 35.00

titulo = 'Estacionamento'
print(f'{titulo:^30}')
tempoPermanencia = int(input('Qual foi o período de permanência (horas)? '))

precoTotal = tempoPermanencia * precoHora

if precoTotal > precoMax:
    precoTotal = precoMax

print(f'O valor final é de R$ {precoTotal:.2f}')

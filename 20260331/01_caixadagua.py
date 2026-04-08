# exercicio 01
titulo = "Caixa D'Água"
print(f'{titulo:^30}')
bloco = int(input('Digite o bloco que mora (1-4): '))

#1ª opção - verificar se é par
if bloco % 2 == 0: #é par
    print('Caixa A')
else:
    print('Caixa B')

#2ª opção - com tupla
if bloco in (2,4): #é par
    print('Caixa A')
else:
    print('Caixa B')

#3ª opção - com OR
if bloco == 2 or bloco == 4:
    print('Caixa A')
else:
    print('Caixa B')
#####
# objetivo: arquivo usado para aprender decisões
# autor: Gabriela Fernandes Cavalcanti
# data:31/03/2026
#####

titulo = 'Maioridade'
print(f'{titulo: ^30}')
idade = int(input('Idade: '))

if idade >= 18: #sim, true, 1
    print('Maior de idade')
else:
    print('Menor de idade')

print('Obrigado por participar da pesquisa.')
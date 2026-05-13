'''
objetivo: arquivo para armazenar os códigos dos exercicios propostos
autor: Gabriela Fernandes Cavalcanti
data: 12/05/2026
'''

import random
import statistics
from statistics import mean

minhaLista = ['café', 'água', 'adoçante', 'leite', 'baunilha', 'café', 'canela', 'chantilly', 'whey', 'pimenta', 'gengibre']

# Desafio 1: descobrir se tem chantilly e gengibre na lista
# if 'chantilly' and 'gengibre' in minhaLista:
#     print('o café será zoado')
# else:
#     print('vai ser bom')

# if 'chantilly' in minhaLista and 'gengibre' in minhaLista:
#     print('o café será zoado')
# else:
#     print('vai ser bom')

###############################################

'''
1. Solicite 10 números inteiros ao usuário e armazene os números pares em uma lista, 
e os números ímpares em outra lista. Exiba as duas listas ao usuário.
'''

# titulo = '### Pares e Impares ###'
# print(f'\n{titulo:^30}')
#
# #cria duas listas vazias ao mesmo tempo
# pares, impares = [], []
#
# #vai repetir e pedir um numero ao usuário 10 vezes
# for i in range(10):
#     n = int(input(f'digite o {i+1}º número: '))
#     #cálculo para ver se o numero é par ou não
#     if n % 2 == 0:
#         pares.append(n)
#     else:
#         impares.append(n)
#
# print(pares)
# print(impares)

###############################################

'''
2. Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba: 
a. A média aritmética dos números armazenados na lista.
b. O somatório dos números pares armazenados na lista.
'''

# titulo = '### Média Aritmética e Soma dos Pares ###'
# print(f'{titulo:^30}')
#
# #cria a lista
# numeros = []
#
# for i in range(10):
#     n = int(input(f'digite o {i+1} número: '))
#     #inclui o numero recebido na lista
#     numeros.append(n)
#
# #sum é funcao nativa
# media = sum(numeros)/len(numeros)
#
# # #jeito 1
# # #define a variável
# # somaPares = 0
# # for n in numeros:
# #     if n % 2 == 0:
# #         #soma o valor
# #         somaPares += n
#
# #jeito 2
# somaPares = sum(n for n in numeros if n % 2 == 0
# )
#
# print(f"\nMédia: {media:.2f}")
# print(f"Soma dos pares: {somaPares}")

###############################################

'''
3. Preencha uma lista com 20 números inteiros aleatórios sorteados entre 1 e 50 e exiba: 
a. a lista com todos os itens armazenados. 
b. o somatório de todos os números contidos na lista. 
c. o maior número da lista. 
d. o menor número da lista.
'''

# titulo = '### Números Aleatórios ###'
# print(f'{titulo:^30}')
#
# #cria lista
# numeros = []
#
# #jeito 1
# for i in range(20):
#     #usa o random pra gerar os numeros aleatorios de 1 a 50 e armazena na variavel num
#     num = random.randint(1, 50)
#     #inclui na lista
#     numeros.append(num)
#
# # jeito 2
# # numeros = [random.randint(1, 50) for i in range(20)]
#
# print(f'a. Números Armazenados: {numeros}')
# print(f'b. Somatória de todos os números: {sum(numeros)}')
# print(f'c. Maior número: {max(numeros)}')
# print(f'd. Menor número: {min(numeros)}')

###############################################

'''
4. Solicite os nomes e as idades de 10 pessoas. 
Armazene os nomes em uma lista e as idades em outra lista. 
Na sequência, exiba os nomes de todas as pessoas que possuem idade maior ou igual a 18 anos.
'''

# titulo = '### Nomes e Idades ###'
# print(f'{titulo:^30}')
#
# nomes, idades = [], []
#
# for i in range(10):
#     nome = input(f'Digite o {i+1}º nome: ')
#     idade = int(input(f'Digite a idade: '))
#     nomes.append(nome)
#     idades.append(idade)
#
# print(f'\nLista de Nomes: {nomes}')
# print(f'Lista de Idades: {idades}')
#
# print(f'\n# Lista de Maior #')
# for i in range(len(idades)):
#     if idades[i] >= 18:
#         print(f'Nome: {nomes[i]}'
#               f'\nIdade: {idades[i]}')
#         print('')

###############################################

'''
5. Preencha a lista com 10 números aleatórios. 
Na sequência, solicite um número ao usuário e informe quantas vezes esse número aparece na lista.
'''

# titulo = '### Números Aleatórios 2 ###'
# print(f'{titulo:^30}')
#
# numeros = [random.randint(1,10) for i in range(10)]
# numUser = int(input('Digite um número de 1 a 10: '))
#
# #jeito 1
# #cria variavel pra servir de contador e inicializa
# # contador = 0
# # for i in numeros:
# #     if i == numUser:
# #         contador += 1
#
# #jeito 2: usando função nativa do python (.count())
# contador = numeros.count(numUser)
#
# print(f'Números: {numeros}')
# print(f'O número {numUser} aparece {contador} vez(es) na lista.')

###############################################

'''
6. Solicite uma quantidade indeterminada de notas de alunos (até que seja informada uma nota menor que zero). 
Após a entrada de dados, exiba: 
a. A quantidade de notas que foram informadas. 
b. Todas as notas na ordem em que foram informadas. 
c. A média aritmética de todas as notas. 
d. A quantidade de notas acima da média aritmética calculada.
'''

# titulo = '### Notas ###'
# print(f'{titulo:^30}')
#
#cria a lista
# notas = []
#
#loop pedindo a nota pro usuário, até que seja digitado um número menor que zero
# while True:
#     nota = float(input('Digite a nota: '))
#
#     if nota < 0:
#         break
#     elif nota > 10:
#         print(f'Nota inválida!')
#     else:
#         notas.append(nota)
#
#calcula a média aritmética
# media = sum(notas)/len(notas)
#
# inicia a variavel
# contador = 0
#
#criando um laço para fazer a contagem de notas acima da média calculada
# for nota in notas:
#     if nota > media:
#         contador += 1
#
# print('')
# print(f'# Resumo #')
# print(f'a. Qtd de notas inseridas: {len(notas)}')
# print(f'b. Notas: {notas}')
# print(f'c. Média: {media:.1f}')
# print(f'd. Qtd notas acima da média: {contador}')


###############################################
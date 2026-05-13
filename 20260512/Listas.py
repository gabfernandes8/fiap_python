'''
objetivo: aprendendo manipulação de listas
autor: Gabriela Fernandes Cavalcanti
data: 12/05/2026
'''

print('Listas')
#lista usa colchete
minhaLista = ['café', 'água', 'adoçante']

print(f'primeiro elemento {minhaLista[0]}')

## indice positivo
# o mesmo racional do range, tem que somar 1 no final pq eh intervalo aberto
print(f'parte a lista {minhaLista[1:2+1]}')

# a representação de ir ate o fim da lista, pode ser feita com : apenas
print(f'parte a lista {minhaLista[0:]}')

## indice negativo
print(f'parte a lista {minhaLista[-2:]}')

#invertido
print(f'parte a lista {minhaLista[2::-1]}')

###########################

## slicing em frases
print('\nSlicing em frases')
frase = 'o mundo é horrível'

#transforma a frase em lista de palavras
palavras = frase.split()
print(palavras)
# invertendo a frase
print(f'frase inversa: {palavras[::-1]}')

# Slicing em palavra
palavra = 'gabriela'
# inverte a palavra
print(f'a palavra {palavra} inversa é {palavra[::-1]}')

#############################

## operações em listas
minhaLista = ['café', 'água', 'adoçante', 'café', 'café', 'canela', 'chantilly']
print('')
print('')
print('')
print('')
print(minhaLista)
print(f'tamanho da lista: {len(minhaLista)}')

#listas são mutáveis
#substituir um valor
print('')
print('mudando valor na lista')
minhaLista[3] = 'leite'
print(minhaLista)

# acrescentar valor no final
print('')
print(f'acrescentando um valor na lista')
minhaLista.append('whey')
print(minhaLista)

# acrescentar valor em uma determinada posição
print('')
print(f'acrescentando um valor em uma determinada posição')
minhaLista.insert(4, 'baunilha')
print(minhaLista)

#### eliminar itens
print('')
print(f'eliminando um valor do final')
minhaLista.pop()
print(minhaLista)

print('')
print(f'eliminando um elemento pelo indice')
minhaLista.pop(5)
print(minhaLista)

print('')
print(f'eliminando um elemento pelo valor do elemento')
minhaLista.remove('chantilly')
print(minhaLista)

# limpa a lista
print('')
print(f'limpando a lista')
minhaLista.clear()
print(minhaLista)

# apagar a lista
print('')
del minhaLista
#print(minhaLista)

#######################################

minhaLista = ['café', 'água', 'adoçante', 'leite', 'baunilha', 'café', 'canela', 'chantilly', 'whey']
pequenaLista = ['pimenta', 'gengibre']

# concatenar uma lista
print('\n## Concatenando lista ##')
# cria uma nova lista a partir de duas
cafePerfeito = minhaLista + pequenaLista
print(f'lista concatenada: {cafePerfeito}')

# estender uma lista
print('\n## Estentendo uma lista ##')
print(minhaLista)
print(pequenaLista)

# a extensão modifica uma das listas necessariamente
minhaLista.extend(pequenaLista)
print(minhaLista)

# varrer uma lista (toda coleção é um elemento interavel)
print('\n## Varrendo lista ##')
print('pelos itens')
for item in minhaLista:
    print(item)

# tb encontra o código assim
# for i in range(len(minhaLista)): # indice = i
#     print(minhaLista[i])

# encontrar um elemento na lista
print('\n## Encontrando elemento na lista ##')
if 'whey' in minhaLista:
    print('o café será proteico')
if 'gelo' in minhaLista:
    print('o café será gelado')

# descobrir a posicao do elemento da lista
print('\n## Desocbrindo posição do elemento na lista ##')
print(f'o chantilly está na posição {minhaLista.index("chantilly")}')

# ordenar a lista
print('\n\n## Estudo do sort e do sorted ##')
print('SORTED()') #nativo do python
print(f'Original > {minhaLista}')
print(f'Ordenada > {sorted(minhaLista)}')
print(f'Depois da ordenação > {minhaLista}') # volta ao original


print('\nSORT()')
print(f'Original > {minhaLista}')
minhaLista.sort()
print(f'Ordenada > {sorted(minhaLista)}')
print(f'Depois da ordenação > {minhaLista}') # volta ao original


#listas com tipos de dados diferentes não é possivel ordenar facilmente
listaHeterogenea = ['Kátia', 45, True, ['Hagrid', 'Cacau']]
print(listaHeterogenea)




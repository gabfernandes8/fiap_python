'''
objetivo: aprendendo estrutura de decisão em python
data: 07/04/2026
autora: Gabriela Fernandes Cavalcanti
'''

import random


# programa exemplo: dia da semana
# v1: tradicional
titulo = ("Dia da Semana")
print(f"{titulo:^30}")

n = int(input("Escolha um numero de 1 a 7"))

if n == 1:
    print(f"Domingo")
else:
    if n == 2:
        print(f"Segunda")
    else:
        if n == 3:
            print("Terça")
        else:
            if n == 4:
                print("Quarta")
            else:
                print("cabou")

##################################################

#v2: elif
n = int(input("Escolha um numero de 1 a 7"))
if n == 5:
    print("Sexta")
elif n == 6:
    print("Sábado")
elif n == 7:
    print("Domingo")

##################################################

#v3: case
# n = int(input("Escolha um numero de 1 a 7"))
# geração de número aleatório
n = random.randint(1, 7)
match n:
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 1 | 7: #equivale ao or
        print("Fim de semana")
    case _: #equivale ao else
        print("Nº inválido")


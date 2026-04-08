'''
objetivo: arquivo para armazenar os exercícios de estrutura de decisão em python
data: 07/04/2026
autora: Gabriela Fernandes Cavalcanti
'''

import random

# 1: dada uma letra, determinar se é vogal ou não
print("##### Letrinhas #####")
letra = input("Digite uma letra: ").lower() #trasnforma tudo em minúsculo

match letra:
    case "a" | "e" | "i" | "o" | "u":
        print("É vogal")
    case _:
        print("É consoante")

########################################################################################

# 2: solicitar ao usuário dois números e ele deve escolher qual operação fazer
print("")
print("##### Calculadorinha #####")
n1 = random.randint(1, 100)
print(f"Primeiro número gerado: {n1}")
n2 = random.randint(1, 100)
print(f"Segundo número gerado: {n2}")

print("")
operador = int(input("Qual operação deseja efetuar:\n"
                 "1: Soma\n"
                 "2: Subtrair\n"
                 "3: Multiplicar\n"
                 "4: Dividir\n"))

if operador == 1:
    print(n1 + n2)
elif operador == 2:
    print(n1 - n2)
elif operador == 3:
    print(n1 * n2)
elif operador == 4:
    print(n1 / n2)
else:
    print("Operação inválida.")
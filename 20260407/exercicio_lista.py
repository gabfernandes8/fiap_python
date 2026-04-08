'''
objetivo: arquivo para armazenar os exercícios da lista ;de estrutura de decisão em python
data: 07/04/2026
autora: Gabriela Fernandes Cavalcanti
'''

# 1. Faça um algoritmo que solicita ao usuário as notas de três provas.
# Calcule a média aritmética e informe se o aluno foi Aprovado ou Reprovado
# (o aluno é considerado aprovado com a média igual ou superior a 6).

print("#### Média Aritmética ####")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1+n2+n3)/3
print("")
print(f"A sua média é {round(media,2)}")

if media >= 6:
    print("Aprovado!")
else:
    print("Reprovado.")

##############################################################################################

# 2. Faça um algoritmo que solicita ao usuário um valor inteiro e exibe uma
#    mensagem informando se o número é par ou ímpar.

print("#### Par ou Ímpar ####")
num = int(input("Digite um número inteiro: "))
print("")

match num % 2:
    case 0:
        print("O número é par.")
    case _:
        print("O número é ímpar.")

##############################################################################################

# 3. Faça um algoritmo que solicita ao usuário um número inteiro e exiba este número na tela.
# Se o número for negativo, antes de ser exibido, ele deve ser transformado no equivalente positivo.

print("#### Conversor de Negativos ####")
num = int(input("Digite um número inteiro: "))

original = num

if num < 0:
    num = num * -1

print(f"O número processado é: {num}")

##############################################################################################

# 4. Faça um algoritmo que solicita ao usuário uma letra e exiba uma mensagem informando se é
#    uma vogal ou uma consoante.

print("##### Letrinhas #####")
letra = input("Digite uma letra: ").lower() #trasnforma tudo em minúsculo

match letra:
    case "a" | "e" | "i" | "o" | "u":
        print("É vogal")
    case _:
        print("É consoante")

##############################################################################################

# 5. Faça um algoritmo que solicita um número inteiro e exibe uma mensagem indicando se ele é
#    positivo, negativo ou zero.

print("#### +, - ou 0 ####")
num = int(input("Digite um número inteiro: "))

if num > 0:
    print(f"O número {num} é positivo.")
elif num < 0:
    print(f"O número {num} é negativo.")
elif num == 0:
    print(f"O número é zero.")

##############################################################################################

# 6. Faça um algoritmo que solicita ao usuário dois números inteiros. O primeiro é o valor
# das horas e o segundo dos minutos. Verifique se a hora é válida ou inválida e exiba uma
# mensagem correspondente
# (São válidas as horas entre 00:00 e 23:59).

print("#### Horários ####")
horas = int(input("Digite o valor das horas (0-23): "))
minutos = int(input("Digite o valor dos minutos (0-59): "))
print("")

if (horas >= 0 and horas <= 23) and (minutos >= 0 and minutos <= 59):
    print(f"Horário: {horas:02d}:{minutos:02d}")
else:
    print("Horário inválido.")

##############################################################################################

# 7. Faça um algoritmo que solicite dois números ao usuário e exiba apenas o maior deles.
#    Caso eles sejam iguais exiba a mensagem “Números Iguais”.

print("#### 2 Números ####")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
print("")

if n1 > n2:
    print(f"O maior número é {n1}")
elif n1 < n2:
    print(f"O maior número é {n2}")
else:
    print("Números iguais.")

##############################################################################################

# 8. Faça um algoritmo que solicita ao usuário três números e exibe na tela apenas o menor deles,
#    ou uma mensagem informando que os números são iguais.

print("#### 3 Números ####")
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))
print("")

if n1 == n2 == n3:
    print("Números iguais")
else:
    resultado = min(n1, n2, n3)
    print(f"O menor número é: {resultado}")

##############################################################################################

# 9. Faça um algoritmo que solicita ao usuário três valores correspondentes aos lados de um triângulo.
# Informe se o triângulo é equilátero (possui 3 lados iguais), isósceles (possui dois lados iguais) ou
# escaleno (não possui lados iguais).

print("#### Tipos de Triângulos ####")
l1 = int(input("Digite o tamanho do lado 1: "))
l2 = int(input("Digite o tamanho do lado 2: "))
l3 = int(input("Digite o tamanho do lado 3: "))
print("")

if l1 == l2 == l3:
    print("O triângulo é equilátero.")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")

##############################################################################################
# 10. Faça um algoritmo que solicite o salário fixo e o valor das vendas efetuadas pelo vendedor
#     de uma empresa. Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até
#     R$ 1.500,00 mais 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário total.

print("#### Salário Total ####")
salarioFixo = float(input("Digite o salario fixo: "))
valorVendas = float(input("Digite o valor das vendas: "))
print("")

if valorVendas <= 1500:
    comissao = valorVendas * 0.03
else:
    comissao = valorVendas * 0.05

salarioTotal = salarioFixo + comissao

print(f"O salário total é de R${salarioTotal:.2f}")
########################################################
# objetivo: lista de exercícios em python
# data: 17/03/2026
# autor: Gabriela Fernandes Cavalcanti
# versão: 1.0
########################################################

# 1 - saudação
# nome = input("Digite o seu nome: ")
# print("Olá,", nome, "!")
# ################################################
#
# 2 - valores
# soma
# n1 = int(input("Informe o primeiro número: "))
# n2 = int(input("Informe o segundo número: "))
#
# soma = n1 + n2
# multiplicacao = n1 * n2
#
# print(nome, ", a soma de", n1, "e", n2, "é", soma, "e a multiplicação entre eles é", multiplicacao)
# #################################################
#
# 3 - média aritmética
# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# nota3 = float(input("Digite a terceira nota: "))
#
# media = round((nota1 + nota2 + nota3) / 3,1)
#
# print(nome, ", a sua média é", media)
#
# 4 - temperaturas em F
# print("**************************")
# print("Conversor de Temperaturas")
# print("**************************")
# tempC = int(input("Informe a temperatura em Celsius: "))
# tempF = (tempC * 1.8) + 32
# print("A temperatura", tempC, "em Fahrenheit é", tempF)
#
# 5 - imc
# print("**************************")
# print("Calculadora de IMC")
# print("**************************")
#
# peso = float(input("Informe o seu peso: "))
# altura = float(input("Informe a sua altura: "))
# imc = round(peso / (altura * altura))
#
# print(nome, ", seu IMC é", imc)
#
# 6 - triangulo
# print("**************************")
# print("Triângulo")
# print("**************************")
#
# base = int(input("Informe o valor da base: "))
# altura = int(input("Informe o valor da altura: "))
#
# area = base * altura / 2
#
# print("A área do seu triângulo é", area)

# 7 - desconto 10%
# preco = float(input("Informe o preço do produto: "))
# desconto = preco * 0.10
# preco_final = preco - desconto
#
# print(f"O preço com desconto é: R$ ${preco_final:.2f}")

# 8 - concessionária
salarioBase = 2500.00
nomeVendedor = input("Informe o nome do vendedor: ")
qtCarrosVendidos = int(input("Quantidade de carros vendidos: "))
valorVendas = float(input("Valor total das vendas: "))
comissao = qtCarrosVendidos * 200.00
comissaoPercentual = valorVendas * 0.02

salarioFinal = salarioBase + comissao + comissaoPercentual

print(f"O vendedor {nomeVendedor} receberá o salário de R$ {salarioFinal:.2f}")
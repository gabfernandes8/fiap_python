####
# objetivo: arquivo de exercicios de algoritmos sequenciais
# data: 24/03/2026
# autores: Ana Paula, Arthur Bezerra, Gabriel Tucci, Gabriela Fernandes,
#          Guilherme Buosi, Juan Ferreira, Lívia Santos, Pedro Davi, Pedro Samugim
####

# # 1 - Ana Paula Macedo Batista - RM573979
# preco = float(input("Digite o valor do produto: "))
# desconto = preco * 0.12
# preco_final = preco - desconto
#
# print("Valor com desconto:", preco_final)

#############################

# # 2 - Ana Paula Macedo Batista - RM573979
# segundos = int(input("Digite o tempo em segundos: "))
#
# # Divisão de inteiros sem resto (//)
# horas = segundos // 3600
#
# # Resto da divisão (%)
# resto = segundos % 3600
# minutos = resto // 60
# seg = resto % 60
# #
# print(f"{horas} hora(s), {minutos} minuto(s) e {seg} segundo(s)")
#
# #############################
#
# # 3 - Gabriel Oliveira Tucci -
# anel_chip = 0.40
# anel_alimento = 0.35
#
# custo_por_frango = anel_chip + (2 * anel_alimento)
#
# n = int(input("Digite o número de frangos: "))
#
# gasto_total = n * custo_por_frango
#
# print(f"Gasto total: R$ {gasto_total:.2f}")
#
# # #############################
#
# # 4 - Gabriela Fernandes Cavalcanti - RM568972
# valorReal = int(input("Informe o valor em reais: "))
# valorDolar = valorReal * 5.23
# print(f"R$ {valorReal} em dolár é ${valorDolar:.2f}")
#
# # ##############################
#
# # # 5 - Guilherme do Nascimento Buosi - RM 571661
# # 1. Leitura dos dados
# votos_brancos = int(input("Digite o número de votos brancos: "))
# votos_nulos = int(input("Digite o número de votos nulos: "))
# votos_validos = int(input("Digite o número de votos válidos: "))
#
# # 2. Cálculo do total de votos
# total_votos = votos_brancos + votos_nulos + votos_validos
#
# # 3. Cálculo dos percentuais
# if total_votos > 0:
#     percentual_brancos = (votos_brancos / total_votos) * 100
#     percentual_nulos = (votos_nulos / total_votos) * 100
#     percentual_validos = (votos_validos / total_votos) * 100
#
#     print(f"Resultado da Eleição:")
#     print(f"Votos Brancos: {round(percentual_brancos, 2)}% ({votos_brancos} votos)")
#     print(f"Votos Nulos: {round(percentual_nulos, 2)}% ({votos_nulos} votos)")
#     print(f"Votos Válidos: {round(percentual_validos, 2)}% ({votos_validos} votos)")
# else:
#     print("Erro: Nenhum voto foi registrado na eleição.")
#
# # ##############################
#
# # 6 - Pedro Samugim Verillo - RM568920
# raio = float(input('Digite o raio do círculo em centímetros: '))
# area = 3.1415 * raio**2
# print('A área do círculo é' ,(round (area, 2)) , 'cm')
#
# ##############################
#
# # 7 - Pedro Davi Silva Conceicao - RM 573644
# custo_fabrica = float(input("Digite o custo de fábrica do carro: R$ "))
# distribuidor = custo_fabrica * 0.28
# impostos = custo_fabrica * 0.45
# custo_consumidor = custo_fabrica + distribuidor + impostos
#
# print(f"\nCusto de fábrica:   R$ {custo_fabrica:.2f}")
# print(f"Distribuidor (28%): R$ {distribuidor:.2f}")
# print(f"Impostos (45%):     R$ {impostos:.2f}")
# print(f"Custo ao consumidor: R$ {custo_consumidor:.2f}")
#
# ##############################
#
# # 8 - JUAN FERREIRA DOS SANTOS SANTANA - RM573855
# sal = float(input("Insira o salario do funcionario: "))
# sal_aumentado = sal * 0.25 + sal
# print(f"Seu novo salario e {sal_aumentado}")
#
# ##############################
#
# # 9 - Arthur Bezerra - RM570967
# primeiro = 780000 * 0.46
# segundo = 780000 * 0.32
# terceiro = 780000 * 0.22
#
# print("1º Ganhador: R$", primeiro)
# print("2º Ganhador: R$", segundo, )
# print("3º Ganhador: R$", terceiro)
#
# ##############################
#
# # 10 - Arthur Bezerra - RM570967
# dias = int(input("Digite a quantidade de dias trabalhados: "))
# bruto = 80 * dias
# sal_liq = bruto - (bruto * 0.08)
#
# print("Salário bruto é R$", bruto)
# print("Salário líquido é de R$", sal_liq)
#
# # ##############################
#
# # 11 - LIVIA SANTOS OLIVEIRA - RM573963
# # Entrada de dados (quantidades vendidas)
# qtd_paes = int(input("Digite a quantidade de pães franceses vendidos: "))
# qtd_broas = int(input("Digite a quantidade de broas vendidas: "))
#
# # Definição dos preços unitários
# PRECO_PAO = 0.38
# PRECO_BROA = 4.50
#
# # Cálculos de arrecadação
# total_paes = qtd_paes * PRECO_PAO
# total_broas = qtd_broas * PRECO_BROA
# total_arrecadado = total_paes + total_broas
#
# # Cálculo da poupança (10%)
# valor_poupanca = total_arrecadado * 0.10
#
# # Exibição dos resultados formatados
# print("-" * 30)
# print(f"Total arrecadado: R$ {total_arrecadado:.2f}")
# print(f"Valor a ser guardado na poupança (10%): R$ {valor_poupanca:.2f}")
# print("-" * 30)
#
# #############################
#
# # # 12 - Pedro Samugim Verillo - RM568920
# comp = float(input('Digite o comprimento da cozinha em metros: '))
# larg = float(input('Digite a largura da cozinha em metros: '))
# altu = float(input('Digite a altura da cozinha em metros: '))
#
# area_cozinha = comp * larg * altu
# qtd_caixas = (round(area_cozinha / 1.5, 0))
#
# print("A área total das paredes é: ", area_cozinha, " m²")
# print("A quantidade de caixas necessárias é: ", qtd_caixas, "caixas")
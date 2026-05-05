'''
objetivo: aprendendo estrutura de repetição em python
data: 14/04/2026
autora: Gabriela Fernandes Cavalcanti
'''

titulo = "Estrutura While"
print("")
print(f"#### {titulo} ####")

'''
    while é muito parecido com o if
a diferença é que ele funciona com a parte do true
o comportamento dele é repetir o mesmo trecho do código
enquanto a condição (comparção) for verdadeira
'''

i = 1
numero = 3
#
# while i <= 10:
#     #i += 1 --> cuidado onde fazer o encremento do i, o resultado pode não ser o esperado
#     tabuada = numero * i
#     print(f"{numero} x {i} = {tabuada}")
#     i += 1  # equivale a i = i + 1

#     print("")

# while i <= 10:
#     tabuada = numero * i
#     print(f"{numero} x {i} = {tabuada}")
#     i += 1 #equivale a i = i + 1
#     print("")
#
#     resposta = input(f"Deseja calcular a próxima tabuada? (s/n)\n").lower()
#     # while resposta == "s":
#     #     numero += 1
#     # else:
#     #     print("aaa")

# 1
# while resposta == "s":
#     i = 1
#     while i <= 10:
#         print(f"{numero} x {i} = {numero * i}")
#         i += 1
#
#     print("")
#     resposta = input("Quer calcular a próxima tabuada?: ").lower()[0]
#     numero += 1
#
# print("")
# print("Volte sempre!")

# 2 - caracter de scape
# while True:
#     i = 1
#     while i <= 10:
#         tabuada = numero * i
#         print(f"{numero} x {i} = {tabuada}")
#         i += 1
#
#     resposta = input(f"Fim da tabuada do {numero}. Aperte enter para continuar ou entre com C").upper()
#     if resposta == "c":
#         break
#     numero += 1

# 3 - um único while
numero = int(input("Insira um número da tabuada: "))
i = 1
continuar = "s"

while i <= 10 and continuar != "n":
    tabuada = numero * i
    print(f"{numero} x {i} = {tabuada}")
    i += 1

    if i >= 10:
        continuar = input("Se deseja parar, digite 'n' ").lower()
        i = 1
        numero += 1
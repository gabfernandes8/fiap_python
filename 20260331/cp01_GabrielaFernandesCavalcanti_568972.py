# # Gabriela Fernandes Cavalcanti - RM568972
# # exercicio 02
# titulo1 = "Compra com Subtotal"
# print(f'{titulo1:^30}')
#
# precoArroz = 22.90
# precoFeijao = 7.50
# precoOleo = 6.80
#
# qtArroz = int(input("Quantos pacotes de arroz foram comprados?: "))
# qtFeijao = int(input("Quantos pacotes de feijão foram comprados?: "))
# qtOleo = int(input("Quantas garrafas de óleo de soja foram compradas?: "))
#
# totalArroz = qtArroz * precoArroz
# totalFeijao = qtFeijao * precoFeijao
# totalOleo = qtOleo * precoOleo
# valorTotal = totalArroz + totalFeijao + totalOleo
#
# print('')
# print("#### Resumo da Compra ####")
# print(f'Total Arroz: {round(totalArroz,2)}')
# print(f'Total Feijao: {round(totalFeijao,2)}')
# print(f'Total Oleo: {round(totalOleo,2)}')
# print(f'Valor Total da Compra: {round(valorTotal,2)}')


# exercicio 03
titulo2 = "Horas Estudadas por Dia"
print(f'{titulo2:^30}')

dom = int(input("Quantas horas estudou no domingo?: "))
seg = int(input("Quantas horas estudou na segunda?: "))
ter = int(input("Quantas horas estudou na terça?: "))
qua = int(input("Quantas horas estudou na quarta?: "))
qui = int(input("Quantas horas estudou na quinta?: "))
sex = int(input("Quantas horas estudou na sexta?: "))
sab = int(input("Quantas horas estudou no sábado?: "))

totalHorasSemana = dom + seg + ter + qua + qui + sex + sab
mediaDia = totalHorasSemana / 7
totalHorasMes = totalHorasSemana * 4
totalHorasAno = totalHorasMes * 12
totalMinutosSemana = totalHorasSemana * 60

print('')
print("#### Resumo Semanal ####")
print(f'Horas totais estudadas na semana: {totalHorasSemana}')
print(f'Média por dia: {round(mediaDia)}')
print(f'Horas totais no mês: {totalHorasMes}')
print(f'Horas totais no ano: {totalHorasAno}')
print(f'Total semanal em minutos: {totalMinutosSemana}')

########################################################
# objetivo: cores?
# data: 17/03/2026
# autor: Gabriela Fernandes Cavalcanti
# versão: 1.0
########################################################

nome = "Gabriela"
idade = 19
temperatura = 35.58756

vermelho = '\033[1;31m'
verde = '\033[1;32m'
reset = '\033[0;0m'

if temperatura >= 39:
    print(f"Paciente: {nome}\nIdade: {idade}\nTemperatura: {vermelho}{temperatura:.2f}{reset}")
else:
    print(f"Paciente: {nome}\nIdade: {idade}\nTemperatura: {verde}{temperatura:.2f}{reset}")

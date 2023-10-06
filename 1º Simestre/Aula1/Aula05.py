# # DADOS SOBRE CADASTRO FUNCIONARIO
# Variaveis
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salario: "))
porcentagem = float(input("Digite porcentagem de aumento: "))
filhos = int(input("Quantos filhos voce tem?" ))

#Calculos
acrescimo = (salario * porcentagem) / 100           # aumento porcentagem
acrescimo2 = filhos * 150                           # filhos
acrescimo3 = (salario + acrescimo) / 3              # ferias | 1/3 do salario.
totalSalario = (salario + acrescimo) + acrescimo2   # Soma de tudo

#print
print(f"Seu nome é: {nome}. \nSua idade é: {idade}. \nSeu salário é: R$ {salario} \nCom acrescimo de %{porcentagem}: R$ {acrescimo} \nAcrescimo de {filhos} filhos: R$ {acrescimo2} \nAcrescimo de: R$ {acrescimo3} \nTotal: R$ {totalSalario}")

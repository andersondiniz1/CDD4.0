# Declaração da variavel
idade = int(input("Digite sua idade: "))
mes = int(input("Digite mês que nasceu: "))
mesatual = int(input("Digite mês atual: "))
anoatual = int(input("Digite ano atual: "))

# Calculo + Condição
ano = anoatual - idade

if mesatual <= mes:
    ano -= 1

if idade >= 18:
    print(f"Sua idade é {idade} é o ano que você nasceu é {ano}, você é maior de idade")
else:
    print(f"Sua idade é {idade} é o ano que você nasceu é {ano}, você é menor de idade")
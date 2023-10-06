# Declaração da variavel de repetição + repetição do codigo caso usuario queira
condicao = "y"
while condicao in "yY":
    n = float(input("Digite um numero: "))

    # Condição: Repetição caso numero digitado for 0 + dizer se é positivo ou negativo
    while n == 0:
        n = float(input("Erro: Digite a primeira maior ou menor que 0: "))
    else:
        if n > 0:
            print(f"O numero {n} é positivo")
        else:
            print(f"O numero {n} é negativo")
    condicao = input("Deseja fazer novamente? (y/n) ")
else:
    print("Encerrando programa")
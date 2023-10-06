# variaveis + repetição
cont = "y"
while cont in "yY":
    # variaveis + repetição
    n = float(input("Digite um numero: "))
    while n == 0:
        n = float(input("Digite um numero diferente de 0: "))
    # Condição
    if n > 10:
        print(f" O numero {n} é MAIOR que 10")
    elif n == 10:
        print(f" O numero {n} é IGUAL a 10")
    else:
        print(f" O numero {n} é MENOR que 10")
    # Codição para repetição
    cont = input("Deseja realizar o teste novamente? (y/n)")
# variaveis + repetição sé valor é y ou  Y
cont = "y"
while cont in "yY":
    # variaveis + repetição sé valor é 0
    base = float(input("Digite o valor da base do triangulo: \n"))
    while base == 0:
            base = float(input("Digite o valor da base do triangulo diferente de 0: \n"))
    altura = float(input("Digite o valor da altura do triangulo: \n"))
    while altura == 0:
            altura = float(input("Digite o valor da altura do triangulo diferente de 0: \n"))

    # Calculo da area
    area = (base * altura) / 2

    # Resultado + Codição para repetição do codigo
    print(f"\nValor da area do triangulo é {area}\n")
    cont = input("Deseja realizar o calculo novamente? (y/n) \n")

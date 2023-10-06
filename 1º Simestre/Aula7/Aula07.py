# variaveis + repetição sé valor é y ou  Y
cond = "y"
while cond == "y" or cond == "Y": # ou: while cond in "yY":
    # variaveis + repetição sé valor é 0 ou maior que 20
    soma = 0
    notas = int(input("Digite quantas notas serão: "))
    while notas <= 0 or notas > 20:
        notas = int(input("Digite quandos notas serão, maior que 0 ou menor que 20: "))

    # Repetição de soma pelo valor de "notas" e armazenamento das somas na variavel "soma"
    for i in range(1, notas + 1, 1):
        n = float(input(f"Digite o valor da {i}º nota: "))
        # Condição sé nota digitada for maior que 0 ou menor que 10, vai pedir para repetir
        while n < 0 or n > 10:
             n = float(input(f"Digite o valor da {i}º nota, entre 0 e 10: "))
        soma += n

    # Calculo da média
    media = soma / notas

    # Resultado + condição de repetição
    print(f"\n Sua média é {media} \n")
    cond = input("Deseja realizar a média novamente? (y/n) \n")


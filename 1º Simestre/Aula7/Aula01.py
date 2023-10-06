# Declaração da variavel de condição de repetir o codigo/calculo
condicao = "y"

# Condição: Repetição do calculo caso usuario decida
while condicao in "yY":
    # Declaração das variaveis notas
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    # Condição: Caso digite notas diferente do padrão de 0 a 10
    while 0 > nota1 > 10:
        nota1 = float(input("Digite a primeira nota novamente de 0 a 10: "))
    while 0 > nota2 > 10:
        nota2 = float(input("Digite a segunda novamente de 0 a 10: "))

    # Declaração da variavel média + Calculo da média
    media = (nota1 + nota2) / 2

    # Condição: aprovado, recuperação ou reprovado.
    if 7 <= media <= 10:
        print(f"Você foi aprovado, sua média é : {media:.2f}")
    elif 7 >= media >= 4:
        print(f"Você está de recuperação, sua média é : {media:.2f}")
    else:
        print(f"Você foi reprovado, sua média é : {media:.2f}")

    condicao = input("desejá realizar um outro calcula (y/n)? ")
else:
    print("Encerrando programa.")

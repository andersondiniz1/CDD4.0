# # Variaveis
# n1 = int(input("1º Numero: "))
# n2 = int(input("2º Numero: "))

# # Estrutura logica
# if n1 > n2:
#     print(f"- Ordem crescente: {n2}, {n1}.")
# else:
#     print(f"- Ordem crescente: {n1}, {n2}.")

############################### python /workspaces/CDD4.0/Aula01.py ###############################


# # Variaveis notas
# nota1 = float(input("Digite a promeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# nota3 = float(input("Digite a terceira nota: "))

# Calculo da media
## media = ((nota1 + nota2) + nota3) / 3

## Condição sé passou ou não
## if media >= 7 and :
#     print(f"- Voce passou, sua média é: {media:.2f}")    # :2f para não dar numero decimal enorme
# else:
#     print(f"- Voce reprovou, sua média é: {media:.2f}")  # :2f para não dar numero decimal enorme

############################### ou ###############################

# # Condição sé passou ou não
# # :2f para não dar numero decimal enorme
# if nota1 < 11 or nota2 < 11 or nota3 < 11 or nota1 > 0 or nota2 > 0 or nota3 > 0:
#     media = ((nota1 + nota2) + nota3) / 3
#     if media < 7:
#         if media < 4:
#             print(f"- Voce reprovou, sua média é: {media:.2f}")
#         else:
#             print(f"- Voce ficou de recuperação, sua média é: {media:.2f}")
#     else:
#         print(f"- Voce passou, sua média é: {media:.2f}")
# else:
#     print("Notas invalidas!")

############################### ou ###############################


# invalido = nota1 or nota2 or nota3 > 10 or nota1 or nota2 or nota3 < 0
# if invalido:
#     print("Notas invalidas!")
# else:
#     media = ((nota1 + nota2) + nota3) / 3
#     if media < 7:
#         if media < 4:
#             print(f"- Voce reprovou, sua média é: {media:.2f}")
#         else:
#             print(f"- Voce ficou de recuperação, sua média é: {media:.2f}")
#     else:
#        print(f"- Voce passou, sua média é: {media:.2f}")


############################### python /workspaces/CDD4.0/Aula01.py ###############################

# # Variaveis time
# time1 = input("Digite nome do primeiro time: ")
# gols1 = int(input(f"Digite a quantidade de gols do time {time1}: "))
# time2 = input("Digite nome do segundo time: ")
# gols2 = int(input(f"Digite a quantidade de gols do time {time2}: "))
#
# # Placar
# print("================ PLACAR ================")
# print(f"[{time1} - {gols1}]            [{time2} - {gols2}]")
# print("========================================")
#
# # # Condição de vitoria
# if gols1 == gols2:
#     print(f"Jogo empatado entre {time1} e {time2}")
# elif gols1 > gols2:
#     print(f"Time {time1} venceu a partida!")
# else:
#     print(f"Time {time2} venceu a partida!")

############################### ou ###############################

# # Condição de vitoria
# if gols1 != gols2:
#     if gols1 > gols2:
#         print(f"Time {time1} venceu a partida!")
#     else:
#         print(f"Time {time2} venceu a partida!")
# else:
#     print(f"Jogo empatado entre {time1} e {time2}")

############################### python /workspaces/CDD4.0/Aula01.py ###############################

# # Variaveis
# g = 5.80
# e = 4.90

# # Input do cliente
# print(f"Preço litro de gasolina é: R${g} | Preço litro de etanol é: R${e}")
# tipo = input(f"Digite o tipo de combustivel 'G' para gasolina é 'E' para etanol: ")

# # Condição
# if tipo == "g" or tipo == "e" or tipo == "G" or tipo == "E":
#     if tipo == "g" or "G":
#         litro = int(input(f"Digite a quantidade em litros de gasolina que deseja: "))
#         preco = g * litro
#         print(f"Gasolina R${preco}")
#     elif tipo == "e" or "E":
#         litro = int(input(f"Digite a quantidade em litros de etanol que deseja: "))
#         preco = e * litro
#         print(f"Etanol R${preco}")
#     else:
#         print("Invalido!")
# else:
#     tipo = input(f"Letra invalida, Digite o tipo de combustivel 'G' para gasolina é 'E' para etanol: ")

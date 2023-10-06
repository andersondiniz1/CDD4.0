# # Variaveis / Input do cliente
# h1 = int(input("Digite primeira hora: "))
# m1 = int(input("Digite primeiro minuto: "))
#
# h2 = int(input("Digite segunda hora: "))
# m2 = int(input("Digite segundo minuto: "))
#
# hora_temporaria = 0
#
# minutos = m1 + m2
#
# # Condição
# if minutos >= 60:
#     hora_temporaria = 1
#     minutos = minutos - 60
#
# if h1 > 12:
#     h1 = h1 - 12
# if h2 > 12:
#     h2 = h2 - 12
#
# # Variaveis2
# hora = h1 + h2 + hora_temporaria
#
# # Condição2
# if hora < 10 and minutos < 10:
#     print(f"final 0{hora}:0{minutos}")
# if hora < 10 and minutos > 10:
#     print(f"final 0{hora}:{minutos}")
# if minutos < 10 and hora > 10:
#     print(f"final {hora}:0{minutos}")
# if hora > 10 and minutos > 10:
#     print(f"final {hora}:{minutos}")

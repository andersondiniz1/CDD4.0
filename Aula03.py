# # saber sé o numero é par ou impar
# # Variaveis / Input do cliente
# numero = int(input("Digite um numero inteiro: "))
# 
# # Condição
# if numero != 0:
#     if numero % 2 == 0:  # se o resto da divisão de 2 for igual a zero.
#         print(f"O numero {numero} é par.")
#     else:
#         print(f"O numero {numero} é impar.")
# else:
#     print("Numero digitado é zero, não funciona.")

############################### python /workspaces/CDD4.0/Aula01.py ###############################

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

############################### python /workspaces/CDD4.0/Aula01.py ###############################

# numero = int(input("Digite numero entre 1 e 12: "))
# if numero < 1 and numero > 12:
#     numero = int(input("Erro, somente digite numero entre 1 e 12: "))
# 
# if numero == 1:
#     print("Janeiro")
# elif numero == 2:
#     print("Fevereiro")
# elif numero == 3:
#     print("Março")
# elif numero == 4:
#     print("Abril")
# elif numero == 5:
#     print("Maio")
# elif numero == 6:
#     print("Junho")
# elif numero == 7:
#     print("Julho")
# elif numero == 8:
#     print("Agosto")
# elif numero == 9:
#     print("Setembro")
# elif numero == 10:
#     print("Outrubro")
# elif numero == 11:
#     print("Novembro")
# elif numero == 12:
#     print("Dezembro")
# else:
#     print("Numero não é entre 1 é 12, erro.")
#     numero = int(input("Erro, somente digite numero entre 1 e 12: "))

############################### python /workspaces/CDD4.0/Aula01.py ###############################

# declarando variavel; enquanto for menor que dez; vai encrementar + 1
# for (x = 1; x < 10; x++)

# em puthon, x é a variavel. inicio = valor da variavel no inicio.
# for x in range(inicio, fim, passo)

# for a in range(1, 11, 1):
#     print(f"Numero {a}")
# for b in range(1, 11, 1):
#     print(b, end=" ")

# for c in range(100,0,-1):
#     print(c, end=" ")

# for d in range(101):
#     if d % 2 == 0:          # ou    if d % 2 != 0:
#         print(" ")
#     else:
#         print(d, end=" é impar")

# numero_final = 0
# for e in range(1, 11):
#     numero = int(input("Digite o numero: "))
#     numero_final = numero_final + numero
# media_final = numero_final / 10
# print(f"Sua média é: {media_final:.2f} é soma dos números é: {numero_final}") # ou print(numero_final/(n)) para a média

# nome = input("Digite o seu nome: ")
# for f in range(10):
#     print(f"Seu nome é: {nome}")

# numero = int(input("Digite o numero: "))
# for f in range(11):
#     multi = numero * f
#     print(f"Tabuada de multiplicação por {f}: {multi}")
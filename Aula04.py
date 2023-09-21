# # 1 até 10 até 1
# for f in range(1, 11, 2):
#     print(f, end=" ")
# for f in range(8, 0, -2):
#     print(f, end=" ")

# for f in range(1, 11, 1):
#     if f % 2 == 1:
#         print(f, end=" ")
# for f in range(9, 0, -1):
#     if f % 2 == 0:
#         print(f, end=" ")

# for f in range(100, 111, 1):
#     print(f, end=" ")

# numero = int(input("Digite numero: "))
# for numero in range(1, numero + 1, 1):
#     print(numero, end=" ")

# contadorneg = 0
# contador = 0
# somaneg = 0
# soma = 0
# for n in range(1, 11, 1):
#     numero = int(input(f"Digite numero {n}: "))
#     if numero > 0:
#         soma = soma + numero
#         #contador = contador + 1
#         print(f"Numero é positivo")
#     if numero < 0:
#         contadorneg = contadorneg + 1
#         somaneg = somaneg + numero
#         print(f"Numero é negativo")
# contador = 10 - contadorneg
# print(f"Existem {contadorneg} numeros negativos e {contador} positivos, soma é: {soma} e negativa {somaneg}")

# contador = 0
# contador2 = 0
# for n in range(1, 11, 1):
#     numero = int(input(f"Digite numero {n}: "))
#     if 10 <= numero <= 20:
#         print(f"Esta entre 10 e 20")
#         contador += 1
# contador2 = 10 - contador
# print(f" {contador} numeros estão no intervalo de 10 e 20 é {contador2} estão fora.")

for n in range(1, 11, 1):
    numero = float(input(f"Digite numero {n}: "))
    soma += numero
media = soma / (n - 1)
print(f"Media é: {media:.2f}")


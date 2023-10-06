# Variaveis notas
nota1 = float(input("Digite a promeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calculo da media
## media = ((nota1 + nota2) + nota3) / 3

## Condição sé passou ou não
## if media >= 7 and :
#     print(f"- Voce passou, sua média é: {media:.2f}")    # :2f para não dar numero decimal enorme
# else:
#     print(f"- Voce reprovou, sua média é: {media:.2f}")  # :2f para não dar numero decimal enorme

# # Condição sé passou ou não
# # :2f para não dar numero decimal enorme
# if (nota1 <= 10 or nota2 <= 10 or nota3 <= 10) or (nota1 >= 0 or nota2 >= 0 or nota3 >= 0):
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


invalido = nota1 > 10 or nota2 > 10 or nota3 > 10 or nota1 < 0.0 or nota2 < 0.0 or nota3 < 0.0
if invalido:
    print("Notas invalidas!")
else:
    media = ((nota1 + nota2) + nota3) / 3
    if media < 7:
        if media < 4:
            print(f"- Voce reprovou, sua média é: {media:.2f}")
        else:
            print(f"- Voce ficou de recuperação, sua média é: {media:.2f}")
    else:
       print(f"- Voce passou, sua média é: {media:.2f}")

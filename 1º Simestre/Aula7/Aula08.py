n1 = float(input("Digite 1º numero: "))
n2 = float(input("Digite 2º numero: "))
resultado = 0
if n1 > n2:
    resultado = n1 - n2
    print(f"\n Resultado da subtração de {n1:.2f} - {n2:.2f} = {resultado:.2f}")
elif n1 == n2:
    print(f"\n Resultado é {resultado:.2f}, numeros {n1:.2f} e {n2:.2f} são iguais")
else:
    resultado = n2 - n1
    print(f"\n Resultado da subtração de {n2:.2f} - {n1:.2f} = {resultado:.2f}")


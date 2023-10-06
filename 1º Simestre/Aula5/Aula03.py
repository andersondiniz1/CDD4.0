val1 = int(input(f"Digite valor 1: "))
val2 = int(input(f"Digite valor 2: "))
cont = 1
divi = 0
while val2 == 0:
    val2 = int(input(f"Diferente de zero, Digite valor 2: "))
    if cont >= 4:
        break
    cont += 1
else:
    divi = val1 / val2
    print(f" Divisão é: {divi:.2f}")
print("Programa finalizado")




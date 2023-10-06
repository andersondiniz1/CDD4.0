n1 = float(input("Digite o 1º numero: "))
n2 = float(input("Digite o 2º numero: "))
n3 = float(input("Digite o 3º numero: "))

if n1 > n2 and n1 > n3:
    print(f"1º Numero {n1} é maior")
elif n2 > n1 and n2 > n3:
    print(f"2º Numero {n2} é maior")
else:
    print(f"3º Numero {n3} é maior")

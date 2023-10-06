a = int(input(f"Digite a quatidade de notas: "))
n = 0
soma = 0
media = 0
numero = 0

while n <= a:
    numero = float(input(f"Digite numero {n}: "))
    soma = soma + numero
    n = n + 1
media = soma / a
print(f"Media é: {media:.2f}")
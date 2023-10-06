# Variaveis
g = 5.80
e = 4.90

# Input do cliente
print(f"Preço litro de gasolina é: R${g} | Preço litro de etanol é: R${e}")
tipo = input(f"Digite o tipo de combustivel 'G' para gasolina é 'E' para etanol: ")

# Condição
if tipo == "g" or tipo == "e" or tipo == "G" or tipo == "E":
    if tipo == "g" or "G":
        litro = int(input(f"Digite a quantidade em litros de gasolina que deseja: "))
        preco = g * litro
        print(f"Gasolina R${preco}")
    elif tipo == "e" or "E":
        litro = int(input(f"Digite a quantidade em litros de etanol que deseja: "))
        preco = e * litro
        print(f"Etanol R${preco}")
    else:
        print("Invalido!")
else:
    tipo = input(f"Letra invalida, Digite o tipo de combustivel 'G' para gasolina é 'E' para etanol: ")





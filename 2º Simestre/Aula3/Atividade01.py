from biblioteca import empresa

nome = input("Digite o produto: ")
quantidade = int(input("Digite a quantidade no estoque: "))
valor = int(input("Digite o valor unitario: "))

resultado = empresa(nome, quantidade, valor)

print(f"Valor total do meu estoque de {resultado[0]} é: R${resultado[1]:.2f}")
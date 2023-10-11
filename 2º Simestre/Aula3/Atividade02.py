from biblioteca import argumento

resposta = input("A resposta esta certa? (sim, não ou 0) \n")

var = argumento(resposta)
print(f"Resultado é: {var}")
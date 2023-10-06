senha = input(f"Digite a senha: ")
senha_padrão = "A1"
cont = 3

while senha != senha_padrão:
    senha = input(f"Incorreta, falta {cont} tentativas, digite a senha: ")
    if cont <= 0 and senha != senha_padrão:
        print("Errou 3 vezes, senha bloqueada")
        break
    cont -= 1
else:
    print(f"Senha correta")

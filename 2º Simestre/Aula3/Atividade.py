# Importar funções da biblioteca
from biblioteca import soma, multiplicar, dividir, subtrair

numero1 = 0
numero2 = 0

# Menu
verificador = "s"
while verificador == "s" or verificador == "s":
    # Tela de menu principal

    escolha = input(f"\n\n=================\n"
                    f"1º numero: {numero1}\n"
                    f"2º numero: {numero2}\n"
                    f"=================\n"
                    f" 1 - somar\n"
                    f" 2 - multiplicar\n"
                    f" 3 - dividir\n"
                    f" 4 - subtrair\n"
                    f" n - Trocar numeros\n"
                    f" s - sair do programa\n"
                    f"=================\n"
                    f"Escolha uma opção: \n")
    while escolha not in "1234sSnN":
        escolha = input("Erro - Opção errada, tente novamente: \n")

    if escolha == "1":
        soma(numero1, numero2)

    elif escolha == "2":
        multiplicar(numero1, numero2)

    elif escolha == "3":
        dividir(numero1, numero2)

    elif escolha == "4":
        subtrair(numero1, numero2)

    elif escolha in "nN":
        numero1 = float(input("\nDigite 1º numero: "))
        numero2 = float(input("Digite 2º numero: "))
        print("Numeros substituidos com sucesso!\n")

    elif escolha in "sS":
        print("\n Encerrando programa...")
        verificador = "n"

    else:
        print("Opção errada, tente novamente...")
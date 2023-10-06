
while True:
    n = int(input(f"\nDigite um mumero: "))
    suce = n + 1
    ante = n - 1

    print("\n====== MENU ======\n"
          "1 - Para sucessor.\n"
          "2 - Para antecessor.\n"
          "3 - Sair do programa.\n"
          "================== \n")
    cond = input("Digite o numero correspondente:")

    if cond == "1":
        print(f"\n Sucessor é {suce}.")
        break
    elif cond == "2":
        print(f"\nAntecessor é {ante}.")
        break
    elif cond == "3":
        print(f"\nEncerranddo programa")
        break
    else:
        rep = input("\nNumero invalido, tente novamente")




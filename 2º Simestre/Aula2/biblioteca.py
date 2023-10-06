# Funções
def soma(n1, n2):
    reservado1 = n1 + n2
    print(f"\nResultado da soma entre {n1} e {n2} é: {reservado1}")

def multiplicar(n1, n2):
    reservado2 = n1 * n2
    print(f"\nResultado da multiplicação entre {n1} e {n2} é: {reservado2}")

def dividir(n1, n2):
    reservado3 = n1 / n2
    print(f"\nResultado da divisão entre {n1} e {n2} é: {reservado3}")

def subtrair(n1, n2):
    reservado4 = n1 - n2
    print(f"\nResultado da subtração entre {n1} e {n2} é: {reservado4}")

def piramide(n1):
    for x in range(1, n1 + 1):
        print(str(x) * x)

def piramide2(n1):
    for i in range(1, n1 + 1):
        for y in range(1, i + 1):
            print(y, end="")
        print("\n")

def cont_vogal(texto):
    cont = 0
    for x in texto:
        if x in "aeiouAEIOU":
            cont += 1
    print(f"Total de volgais no texto é: {cont}")

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

def empresa(nome, quantidade, valor):

    total_estoque = quantidade * valor
    return nome, total_estoque

def argumento(resposta):

    if resposta in "SIMsim":
        verificador = "P"
        return verificador
    elif resposta in "NÃONAOnãonao":
        verificador = "N"
        return verificador 
    elif resposta in "0":
        verificador = "Z"
        return verificador

def adicao(*numeros):

    soma = 0
    for x in numeros:
        soma += x
    return soma

def reverso(texto):

    cont = 0
    for x in texto:
        if x not in " ":
            cont += 1
    print(cont)

    for i in range(len(texto)-1, -1, -1):
        print(texto[i], end="")

def verificador(A):
    B = []
    for x in A:
        if x not in B:
            B.append(x)
    return B
            
        

    





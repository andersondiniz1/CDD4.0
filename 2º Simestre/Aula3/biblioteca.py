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



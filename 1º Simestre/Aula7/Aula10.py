idade = int(input("Digite sua idade: "))
meses = int(input("Digite qual mes voce nasceu: "))
dias = int(input("Digite qual dia voce nasceu: "))

quantidade = (idade * 365) + (meses * 30) + dias
print(quantidade)
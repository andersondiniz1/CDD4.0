quantidade = int(input("Quantos alunos tem na sala? "))
alunos = [""] * quantidade
for x in range(0, quantidade, 1):
    alunos[x] = input(f"Digite o {x + 1}º nome: ")
for n in range(0, quantidade, 1):
    print(f" O {n + 1}º aluno é: {alunos[n]}.")

cond = 0
nome = input("Digite um  nome: ")
for i in range(quantidade):
    if alunos[i] == nome:
        print(f"{alunos[i]} está na {i + 1}º posição.")
        cond = 1

if cond == 0:
    print(f"O nome: {nome}. Não encontrado")






soma = 0
notas = [0] * 5

for x in range(5):
    notas[x] = float(input(f"Digite a {x + 1}º nota: "))

for v in range(5):
    soma += notas[v]

media = soma / 5

print(f"\nMedia geral da sala: {media}\n")

for c in range(5):
    if notas[c] >= media:
        print(f"O {c + 1}º aluno foi aprovado")
    else:
        print(f"O {c + 1}º aluno foi reprovado")
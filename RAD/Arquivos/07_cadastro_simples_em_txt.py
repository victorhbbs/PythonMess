nome = input("Escreva o nome do aluno: ")
nota = float(input("Digite a nota do aluno: "))

with open("alunos.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"{nome};{nota}\n")

print("aluno cadastrado com sucesso!")
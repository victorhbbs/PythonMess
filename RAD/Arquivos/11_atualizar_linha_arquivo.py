ARQUIVO = "alunos.txt"

nome_buscado = input("Digite o nome do aluno que deseja atualizar: ")
nova_nota = float(input("Digite a nova nota: "))

with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

novas_linhas = []
encontrou = False

for linha in linhas:
    dados = linha.strip().split(";")

    nome = dados[0]
    nota = dados[1]

    if nome.lower() == nome_buscado.lower():
        novas_linhas.append(f"{nome};{nota}\n")
        encontrou = True
    else:
        novas_linhas.append(linha)

with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
    arquivo.writelines(novas_linhas)

if encontrou:
    print("Nota atualizada com sucesso.")
else:
    print("Aluno não encontrado.")
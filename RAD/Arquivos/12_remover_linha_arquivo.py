ARQUIVO = "alunos.txt"

nome_remover = input("Digite o nome do aluno que deseja remover: ")

with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

novas_linhas = []
removeu = False

for linha in linhas:
    dados = linha.strip().split(";")

    nome = dados[0]

    if nome.lower() == nome_remover.lower():
        removeu = True
    else:
        novas_linhas.append(linha)

with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
    arquivo.writelines(novas_linhas)

if removeu:
    print("Aluno removido com sucesso.")
else:
    print("Aluno não encontrado.")
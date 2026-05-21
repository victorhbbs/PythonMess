import os

ARQUIVO = "alunos_arq.txt"

def cadastrar_alunos():
    nome = input("Digite o nome do aluno que deseja cadastrar: ")
    nota = float(input("Digite a nota do aluno que deseja cadastrar: "))

    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome};{nota}\n")

    print("Aluno cadastrado com sucesso.")

def listar_alunos():
    if not os.path.exists(ARQUIVO):
        print("Nenhum aluno encontrado.")
        return
    
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")

            nome = dados[0]
            nota = dados[1]

            situacao = "Aprovado" if nota >= 7 else "Reprovado"

            print(f"Aluno encontrado: {nome} | Nota: {nota} | Situação: {situacao}")

def buscar_aluno():
    if not os.path.exists(ARQUIVO):
        print("Nenhum aluno encontrado.")
        return
    
    nome_busca = input("Digite o nome do aluno que deseja procurar: ")
    
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")

            nome = dados[0]
            nota = dados[1]

            situacao = "Aprovado" if nota >= 7 else "Reprovado"

            if nome.lower() == nome_busca.lower:
                print(f"Nome: {nome} | Nota: {nota} | Situação: {situacao}")

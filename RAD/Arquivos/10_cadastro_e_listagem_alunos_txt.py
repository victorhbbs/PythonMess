import os

ARQUIVO = "alunos.txt"

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))

    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome};{nota}\n")

    print("Aluno cadastrado com sucesso.")

def listar_alunos():
    if not os.path.exists(ARQUIVO):
        print("Nenhum aluno encontrado.")
        return
    
    print("\nLista de alunos: ")

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")

            nome = dados[0]
            nota = float(dados[1])

            situacao = "Aprovado" if nota >= 7 else "Reprovado"

            print(f"Aluno: {nome} | Nota: {nota} | Situação: {situacao}")

def exibir_menu():
    print("\n=====MENU=====")
    print("1 - Cadastrar aluno")
    print("2 - Listar aluno")
    print("0 - Sair")

while True:
    exibir_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()

    elif opcao == "2":
        listar_alunos()

    elif opcao == "0":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida.")

    
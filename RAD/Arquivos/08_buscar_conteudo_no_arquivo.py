nome_buscado = input("Digite o nome do aluno que deseja buscar: ")

encontrou = False

with open("alunos.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        dados = linha.strip().split(";")

        nome = dados[0]
        nota = float(dados[1])

        if nome.lower() == nome_buscado.lower():
            print(f"Aluno encontrado: {nome} | Nota: {nota}")
            encontrou = True

if not encontrou:
    print("Aluno não encontrado.")


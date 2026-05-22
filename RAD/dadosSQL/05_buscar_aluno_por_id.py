import sqlite3

conexao = sqlite3.connect("escola.db")
cursor = conexao.cursor()

id_aluno = 1

cursor.execute("SELECT * FROM alunos where id = ?", (id_aluno,))

aluno = cursor.fetchone()

if aluno:
    print(f"ID: {aluno[0]}")
    print(f"Nome: {aluno[1]}")
    print(f"Nota: {aluno[2]}")
else:
    print("Aluno não encontrado!")

conexao.close()
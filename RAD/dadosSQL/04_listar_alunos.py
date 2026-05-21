import sqlite3

conexao = sqlite3.connect("escola.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM alunos")

alunos = cursor.fetchall()

for aluno in alunos:
    id_aluno = aluno[0]
    nome = aluno[1]
    nota = aluno[2]

    print(f"ID: {id_aluno} | Nome: {nome} | Nota: {nota}")

conexao.close()
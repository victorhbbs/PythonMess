import sqlite3

conexao = sqlite3.connect("escola.db")
cursor = conexao.cursor()

nome = "Victor"
nota = 8.5

cursor.execute(
    "INSERT INTO alunos (nome, nota) VALUES (?, ?)",
    (nome, nota)
)

conexao.commit()
conexao.close()

print("Aluno inserido com sucesso.")
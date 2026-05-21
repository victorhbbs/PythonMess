import sqlite3

conexao = sqlite3.connect("escola.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        nota REAL NOT NULL           
    )
""")

conexao.commit()
conexao.close()

print("Tabela alunos criada com sucesso.")
import sqlite3

conexao = sqlite3.connect("escola.db")

print("Banco de dados criado/conectado com sucesso.")

conexao.close()

print("Conexão encerrada.")
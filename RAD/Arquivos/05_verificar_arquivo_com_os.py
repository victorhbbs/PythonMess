import os

nome_arquivo = "mensagem2.txt"

if os.path.exists(nome_arquivo):
    print("O arquivo existe.")
    print(f"Caminho absoluto: {os.path.abspath(nome_arquivo)}")
    print(f"Tamanho do arquivo: {os.path.getsize(nome_arquivo)} bytes")
else:
    print("O arquivo não existe.")
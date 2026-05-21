import os

nome_pasta = "dados"
nome_arquivo = "alunos.txt"

os.makedirs(nome_pasta, exist_ok=True)

caminho_arquivo = os.path.join(nome_pasta, nome_arquivo)

with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write("Victor\n")
    arquivo.write("Ana\n")
    arquivo.write("Carlos\n")

print("Arquivo criado dentro da pasta dados.")
print(f"Caminho do arquivo: {os.path.abspath(caminho_arquivo)}")
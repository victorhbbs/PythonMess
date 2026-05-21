with open("mensagem2.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())
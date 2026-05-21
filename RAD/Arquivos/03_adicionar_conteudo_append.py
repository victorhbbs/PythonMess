with open("mensagem2.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("essa linha foi adicionada depois\n")
    arquivo.write("essa tbm")

print("novas linhas adicionadas com sucesso.")
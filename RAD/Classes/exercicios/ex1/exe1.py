class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Meu nome é {self.nome} e tenho {self.idade} anos.")

pessoa = Pessoa("Victor", 20)

pessoa.apresentar()
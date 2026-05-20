class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calc_total(self):
        return self.preco * self.quantidade
    
produtos = [
    Produto("Carregador", 2.90, 20),
    Produto("Capa de Telefone", 14.99, 12),
    Produto("Fone de Ouvido", 20.99, 8)
]

total_estoque = 0

for produto in produtos:
    total_estoque
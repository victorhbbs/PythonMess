from dataclasses import dataclass

@dataclass
class Produto:
    nome: str
    preco: float
    quantidade: int

    def __post_init__(self):
        if self.preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        
        if self.quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        
    def calcular_total(self):
        return self.preco * self.quantidade
    
try:
    produto = Produto("Notebook", 3500.00, 2)
    print(produto)
    print(f"Total: R$ {produto.calcular_total():.2f}")

    produto_invalido = Produto("Mouse", -50.00, 1)

except ValueError as erro:
    print(f"Erro ao criar produto: {erro}")
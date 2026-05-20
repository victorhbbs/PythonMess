from dataclasses import dataclass

@dataclass
class Produto:
    nome: str
    preco: float
    quantidade: int

    def calcular_total(self):
        return self.preco * self.quantidade
    
produto1 = Produto("Teclado", 150.00, 2)
produto2 = Produto("Mouse", 80.00, 3)

print(produto1)
print(produto2)

print(f"Total do produto 1: R$ {produto1.calcular_total():.2f}")
print(f"Total do produto 2: R$ {produto2.calcular_total():.2f}")
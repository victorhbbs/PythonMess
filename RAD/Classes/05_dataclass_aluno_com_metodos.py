from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    nota1: float
    nota2: float

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2
    
    def situacao(self):
        media = self.calcular_media()

        if media >= 7:
            return "Aprovado"
        elif media >= 5:
            return "Recuperação"
        else:
            return "Reprovado"
        
    def exibir_boletim(self):
        print(f"Aluno: {self.nome}")
        print(f"Nota 1: {self.nota1}")
        print(f"Nota 2: {self.nota2}")
        print(f"Média: {self.calcular_media():.2f}")
        print(f"Situação: {self.situacao()}")

aluno = Aluno("Victor", 8.0, 6.5)

aluno.exibir_boletim()
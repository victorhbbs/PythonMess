class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def esta_aprovado(self):
        return self.nota >= 7
    
    def exibir_dados(self):
        situacao = "Aprovado" if self.esta_aprovado() else "Reprovado"
        print(f"Aluno: {self.nome} | Nota: {self.nota} | Situação: {situacao}")

alunos = [
    Aluno("Victor", 8.5),
    Aluno("Ana", 6.0),
    Aluno("Carlos", 9.0),
    Aluno("Marina", 5.5)
]

print("Todos os alunos:")
for aluno in alunos:
    aluno.exibir_dados()

print("\nAlunos aprovados:")
for aluno in alunos:
    if aluno.esta_aprovado():
        aluno.exibir_dados()
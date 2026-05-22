import os
import sqlite3
import tkinter as tk
from tkinter import messagebox
from dataclasses import dataclass

BANCO = "estudantes.db"
ARQUIVO_RELATORIO = "relatorio_alunos.txt"

@dataclass
class Aluno:
    nome: str
    nota: float

    def situacao(self):
        if self.nota >= 7:
            return "Aprovado"
        return "Reprovado"
    
def conectar():
    return sqlite3.connect(BANCO)

def criar_tabela():
    conexao = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                nota REAL NOT NULL           
            )
        """)

        conexao.commit

    except sqlite3.Error as erro:
        messagebox.showerror("Erro", f"Erro ao criar tabela: {erro}")

    finally:
        if conexao:
            conexao.close()

def cadastrar_aluno():
    conexao = None

    try:
        nome = entrada_nome.get()
        nota = float(entrada_nota.get())

        if nome.strip() == "":
            messagebox.showwarning("Atenção", "Digite o nome do aluno.")
            return 
        
        aluno = Aluno(nome, nota)

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO alunos (nome, nota) VALUES (?, ?)",
            (aluno.nome, aluno.nota)
        )

        conexao.commit()

        messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso.")

        entrada_nome.delete(0, tk.END)
        entrada_nota.delete(0, tk.END)

        listar_alunos()

    except ValueError:
        messagebox.showerror("Erro", "A nota precisa ser um número.")

    except sqlite3.Error as erro:
        if conexao:
            conexao.rollback()

        messagebox.showerror("Erro", f"Erro no banco de dados: {erro}")

    finally:
        if conexao:
            conexao.close()

def listar_alunos():
    conexao = None

    try:
        lista_alunos.delete(0, tk.END)

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT id, nome, nota FROM alunos")
        alunos = cursor.fetchall()

        if not alunos:
            lista_alunos.insert(tk.END, "Nenhum aluno cadastrado.")
            return
        
        for aluno in alunos:
            id_aluno = aluno[0]
            nome = aluno[1]
            nota = aluno[2]

            objeto_aluno = Aluno(nome, nota)

            texto = (
                f"ID: {id_aluno} | "
                f"Nome: {objeto_aluno.nome} | "
                f"Nota: {objeto_aluno.nota} | "
                f"Situação: {objeto_aluno.situacao()}"
            )

            lista_alunos.insert(tk.END, texto)

    except sqlite3.Error as erro:
        messagebox.showerror("Erro", f"Erro ao listar alunos: {erro}")

    finally:
        if conexao:
            conexao.close()

def gerar_relatorio():
    conexao = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT nome, nota FROM alunos")
        alunos = cursor.fetchall()

        with open(ARQUIVO_RELATORIO, "w", encoding="utf-8") as arquivo:
            arquivo.write("RELATÓRIO DE ALUNOS\n")
            arquivo.write("===================\n\n")

            for aluno in alunos:
                nome = aluno[0]
                nota = aluno[1]

                objeto_aluno = Aluno(nome, nota)

                arquivo.write(
                    f"Nome: {objeto_aluno.nome} | "
                    f"Nota: {objeto_aluno.nota} | "
                    f"Situação: {objeto_aluno.situacao()}\n"
                )

        caminho = os.path.abspath(ARQUIVO_RELATORIO)

        messagebox.showinfo(
            "Relatório",
            f"Relatório gerado com sucesso:\n{caminho}"
        )

    except sqlite3.Error as erro:
        messagebox.showerror("Erro", f"Erro no banco de dados: {erro}")

    except OSError as erro:
        messagebox.showerror("Erro", f"Erro ao criar arquivo: {erro}")

    finally:
        if conexao:
            conexao.close()

criar_tabela()

janela = tk.Tk()
janela.title("Cadastro de Alunos")
janela.geometry("600x400")

frame_formulario = tk.Frame(janela)
frame_formulario.pack(pady=10)

label_nome = tk.Label(frame_formulario, text="Nome:")
label_nome.grid(row=0, column=0, padx=5, pady=5)

entrada_nome = tk.Entry(frame_formulario)
entrada_nome.grid(row=0, column=1, padx=5, pady=5)

label_nota = tk.Label(frame_formulario, text="Nota:")
label_nota.grid(row=1, column=0, padx=5, pady=5)

entrada_nota = tk.Entry(frame_formulario)
entrada_nota.grid(row=1, column=1, padx=5, pady=5)

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

botao_cadastrar = tk.Button(
    frame_botoes,
    text="Cadastrar",
    command=cadastrar_aluno
)

botao_cadastrar.grid(row=0, column=0, padx=5)

botao_listar = tk.Button(
    frame_botoes,
    text="Listar",
    command=listar_alunos
)

botao_listar.grid(row=0, column=1, padx=5)

botao_relatorio = tk.Button(
    frame_botoes,
    text="Gerar Relatório TXT",
    command=gerar_relatorio
)

botao_relatorio.grid(row=0, column=2, padx=5)

lista_alunos = tk.Listbox(janela, width=80, height=12)
lista_alunos.pack(pady=10)

listar_alunos()

janela.mainloop()
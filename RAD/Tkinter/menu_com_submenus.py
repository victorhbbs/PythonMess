import subprocess
import sys
from pathlib import Path
import tkinter as tk


class ExemploMenu:
    def __init__(self):
        self.janela = tk.Tk()

        self.janela.title("Menu")
        self.janela.geometry("300x200")
        self.janela.config(bg="white")

        menubar = tk.Menu(self.janela)

        filemenu = tk.Menu(
            menubar,
            tearoff=0
        )

        filemenu.add_command(label="Novo")
        filemenu.add_command(label="Abrir")
        filemenu.add_command(label="Fechar")
        filemenu.add_separator()
        filemenu.add_command(
            label="Sair",
            command=self.sair
        )

        menubar.add_cascade(
            label="Arquivo",
            menu=filemenu
        )

        menu_ajuda = tk.Menu(
            menubar,
            tearoff=0
        )

        menu_ajuda.add_command(
            label="Abrir exemplo de Pack",
            command=self.abrir_exemplo_pack
        )

        menu_ajuda.add_command(
            label="Abrir exemplo de Widgets",
            command=self.abrir_exemplo_widgets
        )

        menu_ajuda.add_command(
            label="Sobre",
            command=self.sobre
        )

        menubar.add_cascade(
            label="Ajuda",
            menu=menu_ajuda
        )

        self.janela.config(menu=menubar)

        self.janela.mainloop()

    def sair(self):
        self.janela.destroy()

    def sobre(self):
        segunda_janela = tk.Toplevel(self.janela)
        segunda_janela.title("Sobre")
        segunda_janela.geometry("200x200")

        label = tk.Label(
            segunda_janela,
            text="Exemplo de menu com Tkinter"
        )

        label.pack(
            padx=20,
            pady=20
        )

    def abrir_exemplo_pack(self):
        self.abrir_arquivo_python("04_pack_fill_expand.py")

    def abrir_exemplo_widgets(self):
        self.abrir_arquivo_python("01_widgets_label_button_entry.py")

    def abrir_arquivo_python(self, nome_arquivo):
        pasta_atual = Path(__file__).parent
        caminho_arquivo = pasta_atual / nome_arquivo

        subprocess.Popen([
            sys.executable,
            str(caminho_arquivo)
        ])


if __name__ == "__main__":
    ExemploMenu()
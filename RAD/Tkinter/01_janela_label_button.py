import tkinter as tk

def clicar():
    label.config(text="Você clicou no botão!")

janela = tk.Tk()
janela.title("Primeira Janela")
janela.geometry("300x200")

label = tk.Label(
    janela,
    text="Olá, Tkinter!",
    font=("Arial", 14)
)

label.pack(pady=20)

botao = tk.Button(
    janela,
    text="Clique aqui!",
    command=clicar
)

botao.pack()

janela.mainloop()
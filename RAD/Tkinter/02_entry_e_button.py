import tkinter as tk

def mostrar_nome():
    nome = entrada_nome.get()
    label_resultado.config(text=f"Olá, {nome}!")

janela = tk.Tk()
janela.title("Exemplo com Entry")
janela.geometry("300x200")

label_nome = tk.Label(janela, text="Digite seu nome:")
label_nome.pack(pady=5)

entrada_nome = tk.Entry(janela)
entrada_nome.pack(pady=5)

botao = tk.Button(
    janela,
    text="Enviar",
    command=mostrar_nome
)

botao.pack(pady=5)

label_resultado = tk.Label(janela, text="")
label_resultado.pack(pady=10)

janela.mainloop()
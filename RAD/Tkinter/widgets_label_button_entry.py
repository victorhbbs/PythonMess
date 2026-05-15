import tkinter as tk


janela = tk.Tk()
janela.title("Exemplo de Widgets Básicos")

label = tk.Label(
    text="Brincando com Tkinter",
    fg="#0000FF",
    bg="#00FFFF",
    width=40,
    height=4
)

botao = tk.Button(
    text="Botão",
    width=25,
    height=5
)

entry = tk.Entry()

label.pack()
botao.pack()
entry.pack()

entry.insert(0, "Raphael")

nome = entry.get()

label2 = tk.Label(
    text=nome,
    fg="#0000FF",
    bg="#E0FFFF",
    width=40,
    height=4
)

label2.pack()

janela.mainloop()
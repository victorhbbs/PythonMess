import tkinter as tk


janela = tk.Tk()
janela.title("Exemplo de Pack com Fill e Expand")

frame1 = tk.Frame(
    master=janela,
    width=200,
    height=100,
    bg="red"
)

frame1.pack(
    fill=tk.BOTH,
    side=tk.LEFT,
    expand=True
)

frame2 = tk.Frame(
    master=janela,
    width=100,
    bg="green"
)

frame2.pack(
    fill=tk.BOTH,
    side=tk.LEFT,
    expand=True
)

frame3 = tk.Frame(
    master=janela,
    width=50,
    bg="blue"
)

frame3.pack(
    fill=tk.BOTH,
    side=tk.LEFT,
    expand=True
)

janela.mainloop()
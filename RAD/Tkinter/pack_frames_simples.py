import tkinter as tk


janela = tk.Tk()
janela.title("Exemplo de Pack com Frames")

frame_a = tk.Frame(master=janela)
frame_b = tk.Frame(master=janela)

label_a = tk.Label(master=frame_a, text="Frame A")
label_a.pack()

label_b = tk.Label(master=frame_b, text="Frame B")
label_b.pack()

frame_a.pack()
frame_b.pack()

janela.mainloop()
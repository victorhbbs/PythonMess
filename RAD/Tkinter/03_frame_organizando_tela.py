import tkinter as tk

janela = tk.Tk()
janela.title("Exemplo com Frame")
janela.geometry("300x200")

frame_titulo = tk.Frame(janela)
frame_titulo.pack(pady=10)

frame_formulario = tk.Frame(janela)
frame_formulario.pack(pady=10)

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

label_titulo = tk.Label(
    frame_titulo,
    text="Cadastro de Aluno",
    font=("Arial", 16)
)

label_titulo.pack()

label_nome = tk.Label(frame_formulario, text="Nome:")
label_nome.pack()

entrada_nome = tk.Entry(frame_formulario)
entrada_nome.pack()

botao_salvar = tk.Button(frame_botoes, text="Salvar")
botao_salvar.pack(side=tk.LEFT, padx=5)

botao_salvar = tk.Button(frame_botoes, text="Cancelar")
botao_salvar.pack(side=tk.LEFT, padx=5)

janela.mainloop()
import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root

        self.root.title("Exemplo de Placeholder com Entry")

        self.texto_padrao = "Digite o seu nome aqui"

        self.entrada = tk.Entry(
            root,
            fg="gray",
            width=30
        )

        self.entrada.insert(0, self.texto_padrao)
        self.entrada.pack(pady=2)

        self.entrada.bind("<FocusIn>", self.limpar)
        self.entrada.bind("<FocusOut>", self.restaurar)

    def limpar(self, event):
        if self.entrada.get() == self.texto_padrao:
            self.entrada.delete(0, tk.END)
            self.entrada.config(fg="black")

    def restaurar(self, event):
        if not self.entrada.get():
            self.entrada.insert(0, self.texto_padrao)
            self.entrada.config(fg="gray")


root = tk.Tk()
App(root)
root.mainloop()
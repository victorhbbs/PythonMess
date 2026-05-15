import tkinter as tk


class GradeApp:
    def __init__(self, root):
        self.root = root

        self.root.title("Exemplo de Grid")

        self.root.columnconfigure(0, minsize=250)
        self.root.rowconfigure([0, 1], minsize=100)

        self.label1 = tk.Label(
            self.root,
            text="A",
            bg="red",
            fg="white"
        )

        self.label1.grid(
            row=0,
            column=0,
            sticky="ne"
        )

        self.label2 = tk.Label(
            self.root,
            text="B",
            bg="blue",
            fg="white"
        )

        self.label2.grid(
            row=1,
            column=0,
            sticky="sw"
        )


root = tk.Tk()
GradeApp(root)
root.mainloop()
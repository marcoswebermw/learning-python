import tkinter as tk
from tkinter import ttk

janela = tk.Tk()

ttk.Label(janela, text="Novo Label").grid(column=0, row=0)

janela.mainloop()
import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Janela Principal")

painel = ttk.LabelFrame(janela, text=" Painel de Componentes ")
painel.grid(column=0, row=0)

# Os componentes são adicionados no painel e não na janela.
valorNome = tk.StringVar()
lb1 = ttk.Label(painel, text="Nome:")
txt1 = tk.Entry(painel, width=15, textvariable=valorNome)

lb1.grid(column=0, row=0)
txt1.grid(column=0, row=1)

txt1.focus()

janela.mainloop()
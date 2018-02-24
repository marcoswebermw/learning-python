import tkinter as tk
from tkinter import ttk

cor = ["RED", "GREEN", "BLUE"]

janela = tk.Tk()

valor_escolhido = tk.IntVar()
valor_escolhido.set(-1) # Valor qualquer

def escolher():
    val = valor_escolhido.get()
    if val == 0: janela.configure(background=cor[val])
    elif val == 1: janela.configure(background=cor[val])
    elif val == 2: janela.configure(background=cor[val])

for coluna in range(3):
    rb_atual = tk.Radiobutton(janela, text=cor[coluna], variable=valor_escolhido, value=coluna, command=escolher)
    rb_atual.grid(column=1, row=coluna, sticky=tk.W)


janela.mainloop()
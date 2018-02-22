import tkinter as tk
from tkinter import ttk

VERMELHO = "RED"
VERDE = "GREEN"
AZUL = "BLUE"

janela = tk.Tk()

valor_escolhido = tk.IntVar()

def escolher():
    val = valor_escolhido.get()
    if val == 1: janela.configure(background=VERMELHO)
    elif val == 2: janela.configure(background=VERDE)
    elif val == 3: janela.configure(background=AZUL)

rb_1 = tk.Radiobutton(janela, text=VERMELHO, variable=valor_escolhido, value=1, command=escolher)
rb_1.grid(column=0, row=1, sticky=tk.W, columnspan=3)

rb_2 = tk.Radiobutton(janela, text=VERDE, variable=valor_escolhido, value=2, command=escolher)
rb_2.grid(column=0, row=2, sticky=tk.W, columnspan=3)

rb_3 = tk.Radiobutton(janela, text=AZUL, variable=valor_escolhido, value=3, command=escolher)
rb_3.grid(column=0, row=3, sticky=tk.W, columnspan=3)

rb_1.focus()

janela.mainloop()
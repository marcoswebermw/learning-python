import tkinter as tk
from tkinter import scrolledtext

janela = tk.Tk()
largura = 30
altura = 4

sct = scrolledtext.ScrolledText(janela, width=largura, height=altura, wrap=tk.WORD)
sct.grid(column=0, columnspan=3)
sct.focus()
janela.mainloop()

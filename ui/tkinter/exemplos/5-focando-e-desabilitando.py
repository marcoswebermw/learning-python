import tkinter as tk 
from tkinter import ttk

# Janela
janela = tk.Tk()
janela.title('Focando e desabilitando')

# Textbox
texto_variavel = tk.StringVar()
texto = ttk.Entry(janela, width=15, textvariable=texto_variavel)
texto.grid(column=0, row=0)

# Evento do Botao
def clicar():
    botao.configure(state="disabled")
    botao.configure(text="Estou desabilitado")

# Botao
botao = ttk.Button(janela, text="Estou habilitado", command=clicar)
botao.grid(column=1, row=0)

texto.focus()

janela.mainloop()
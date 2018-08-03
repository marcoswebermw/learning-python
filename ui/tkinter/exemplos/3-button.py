import tkinter as tk
from tkinter import ttk

# Janela principal
janela = tk.Tk()
janela.title('Botões')

# Label
rotulo_1 = ttk.Label(janela, text="Rótulo")
rotulo_1.grid(column=0, row=0)

# Evento do clique do botão
def clicar():
    botao_1.configure(text="Eu fui clicado!")
    rotulo_1.configure(foreground='blue')
    rotulo_1.configure(text='Fiquei azul')

# Button
botao_1 = ttk.Button(janela, text="Clique aqui!", command=clicar)
botao_1.grid(column=1, row=0)

janela.mainloop()
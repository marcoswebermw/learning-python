import tkinter as tk 
from tkinter import ttk

# Janela
janela = tk.Tk()
janela.title('Caixa de texto')

# Label
rotulo_1 = ttk.Label(janela, text="Nome:")
rotulo_1.grid(column=0, row=0)

# Texto
texto_variavel = tk.StringVar()
texto_1 = ttk.Entry(janela, width=15, textvariable=texto_variavel)
texto_1.grid(column=0, row=1)

# Evento do Botao
def clicar():
    botao_1.configure(text='Olá ' + texto_1.get())
    rotulo_1.configure(foreground='blue')

# Botao
botao_1 = ttk.Button(janela, text="Clique aqui", command=clicar)
botao_1.grid(column=1, row=1)


janela.mainloop()
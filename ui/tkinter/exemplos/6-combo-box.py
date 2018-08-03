import tkinter as tk 
from tkinter import ttk

# Janela
janela = tk.Tk()
janela.title('Combo box')

# ComboBox
texto_variavel = tk.StringVar()
combo = ttk.Combobox(janela, width=15, textvariable=texto_variavel, state='readonly')
combo['values'] = (1,2,5,10,20)
combo.current(0)
combo.grid(column=0, row=0)

# Evento do Botao
def clicar():
    botao.configure(text="O valor do combo é: " + combo.get())

# Botao
botao = ttk.Button(janela, text='Clique me', command=clicar)
botao.grid(column=1, row=0)

combo.focus()
janela.mainloop()

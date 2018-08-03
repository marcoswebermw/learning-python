import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Janela Principal")
janela.configure(background="BLUE")

painel = ttk.LabelFrame(janela, text=" Painel de Componentes ")
painel.grid(column=0, row=0, padx=5, pady=5)

# Os componentes são adicionados no painel e não na janela.
valorNome = tk.StringVar()
lb1 = ttk.Label(painel, text="Nome:")
txt1 = tk.Entry(painel, width=15, textvariable=valorNome)
btn1 = ttk.Button(painel, text="Clique aqui!")

# Pegando os componentes filhos do painel
pos = 0
for c in painel.winfo_children():
    c.grid_configure(sticky="NW", row=pos, columnspan=1, padx=15, pady=3)
    pos += 1
    

txt1.focus()
janela.mainloop()
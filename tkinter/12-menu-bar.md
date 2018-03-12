## Menu bar
  
O Tkinter nos permite criar `barras de menus` que podem ser adicionadas à janela da aplicação. E dentro dessas barras de menu podemos adicionar `menus`. Dentro dos menus também podemos adicionar `itens`.
  
### Exemplo
  
```py
import tkinter as tk
from tkinter import Menu

janela = tk.Tk()

# Método para sair da aplicação.
def _sair():
    janela.quit()
    janela.destroy()
    exit()

# Criando barra de menu e adicionando-a à janela.
barra_menu = Menu(janela) # Barra de menu.
janela.config(menu=barra_menu)

# Criando menus.
# O tearoff serve para remover a linha tracejada que
# aparece por padrão.
menu_arquivo = Menu(barra_menu, tearoff=0)
menu_ajuda = Menu(barra_menu, tearoff=0)

# Adicionando itens aos menus.
menu_arquivo.add_command(label="Novo") # Item.
menu_arquivo.add_separator() # Separador de itens.
menu_arquivo.add_command(label="Sair", command=_sair) # Item.
menu_ajuda.add_command(label="Sobre") # Item

# Adicionando o menus na barra de menus.
barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo) # Menu.
barra_menu.add_cascade(label="Ajuda", menu=menu_ajuda) # Menu.

janela.mainloop()
```
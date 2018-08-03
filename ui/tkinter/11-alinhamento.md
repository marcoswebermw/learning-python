## Alinhamento de componentes
  
O tkinter através do método grid nos permite definir algumas opções de alinhamento dos elementos na tela.  
  
### columnspan e rowspan 
  
Esses dois são responsáveis por expandir o número de colunas ou linhas que um elemnto pode ocupar. O padrão é que um elemento esteja disposto em uma linha e uma coluna.  
  
### column e row
  
Define a coluna e a linha que o componente vai ficar.  
  
### padx e pady
  
Define o preenchimento(espaços) lateral que um componente deve ter em relação aos outros.  
  
### sticky
  
O sticky pode substituir ou acompanhar os `column` e `row`. Na verdade ele força que um elemento seja posicionado em determinado local do seu componente pai.  
  
Ele pode posicionar os elementos no norte, sul, leste ou oeste dentro do seu componente pai.
  
Existem duas formas de se fazer:
  
* Com `tk.N`, `tk.S`, `tk.W`, `tk.E`
  
* Com `N`, `S`, `W`, `E`
  
> Os ultimos podem ser combinados como em: `NE`, `NW`, `SE`, `SW`,etc.  
  
### grid_configure
  
O `grid_configure()` permite que possamos definir as mesmas propriedades que foram definidas em `grid`.  
  
### winfo_children
  
Permite obter todos os filhos de um determinado componente.  
  
### Exemplo
  
```py
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
```


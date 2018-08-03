## Combo box

É criado passando como parâmetros o contexto(janela), a largura do combo, uma variável para armazenar o texto digitado no combo(se estiver habilitado com state), e opcionalmente o parâmetro `state` que indicará se é possível ou não escrever na caixa do combo.  
  
Os valores são passados através de uma tupla na chave `values` do combo.  

O método `current` indica a linha do combo que começará selecionada. O primeiro índice é o "0".   
  
O método `get()` também retorna o valor selecionado.  
   
  
```py
# ComboBox
texto_variavel = tk.StringVar()
combo = ttk.Combobox(janela, width=15, textvariable=texto_variavel, state='readonly')
combo['values'] = (1,2,5,10,20)
combo.current(0)
combo.grid(column=0, row=0)
```  
  
### Código completo

```py
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

```  
  
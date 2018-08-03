## CheckButton
  
O checkbutton é uma caixa que pode estar selecionada ou não.  
   
O primeiro parâmetro de seu construtor é o contexto de execução, que será nossa janela.  
  
O `text` é o rótulo para descrição do checkbutton.  
  
O parâmetro `variable` recebe uma variável que armazenará, através de um inteiro(`tk.IntVar()`), o estado do checkbutton. O  `0` para não selecionado e `1` para selecionado.  
  
E finalmente o `state` indica o estado do checkbox. Que pode ser `active`, `disabled` ou `normal`.  
  
Os métodos `select()` e `deselect()` executam a ação de selecionar e deselecionar o checkbutton, respectivamente .  
    
### Código completo

```py
import tkinter as tk
from tkinter import ttk


janela = tk.Tk()
estado = tk.IntVar()
cb_1 = tk.Checkbutton(janela, text='CheckButton 1', variable=estado, state='normal')
print('CHECKBUTTON NÃO SELECIONADO: {}'.format(estado.get()))
cb_1.select()
print('CHECKBUTTON SELECIONADO: {}'.format(estado.get()))
cb_1.grid(column=0, row=0, sticky=tk.W) # tk.W -> Posicionado no Oeste(West).

estado2 = tk.IntVar()
cb_2 = tk.Checkbutton(janela, text='CheckButton 2', variable=estado2, state='disabled')
cb_2.grid(column=1, row=0)

estado3 = tk.IntVar()
cb_3 = tk.Checkbutton(janela, text='CheckButton 3', variable=estado3, state='active')
cb_3.grid(column=0, row=1)

def marcar_desmarcar():
    if estado2.get():
        estado2.set(0)
    else:
        estado2.set(1)

bt_1 = tk.Button(janela, text='Marcar Checkbutton 2', command=marcar_desmarcar)
bt_1.grid(column=1, row=1)



janela.mainloop()
```  


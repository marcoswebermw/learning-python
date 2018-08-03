## Label
  
Criando um label passando o contexto(janela), um texto, e depois um grid de posicionamento.  
  
`ttk.Label(janela, text="Novo Label").grid(column=0, row=0)`   
  
> O `grid` indica em que coluna e linha da janela o label ficará posicionado.  
  
### Código completo
  
```py
import tkinter as tk
from tkinter import ttk

janela = tk.Tk()

rotulo = ttk.Label(janela, text="Novo Label")

rotulo.grid(column=0, row=0)

janela.mainloop()
```  
  
  

## Scrolled Text
  
Equivalente a um `TextArea` com barras de rolagens em outras linguagens.  
  
Recebe um contexto, largura, altura e o `wrap` que indica como o texto vai se comportar.  

O padrão do `wrap` é `tk.CHAR` que deixa o texto quebrar no canto e continuar na linha debaixo. O `tk.WORD` obriga o texto todo a ir para a outra linha, não permitindo quebras.    
  
```py
import tkinter as tk
from tkinter import scrolledtext

janela = tk.Tk()
largura = 30
altura = 4

sct = scrolledtext.ScrolledText(janela, width=largura, height=altura, wrap=tk.WORD)
sct.grid(column=0, columnspan=3)
sct.focus()
janela.mainloop()
```
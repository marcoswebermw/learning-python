### Importando e Instanciando
  
Para usarmos a `tkinter` precisamos importá-la e depois criar uma instância dela.  
  
```py
import tkinter as tk

janela = tk.Tk()
```
  
### Colocando título
  
```py
janela.title("Usando Tkinter");
```
  
### Redimensionando
    
```py
janela.resizable(False, False)
```
  
O primeiro parâmetro de `resizable()` determina se o eixo `X` será redimensionável ou não. O segundo parâmetros se refere ao eixo `Y`.   
  
### Event Loop
  
O `event loop` é um loop infinito que fica rodando esperando que algum evento ocorra para dispará-lo.  Só termina quando invocada alguma função para terminá-lo ou quando a janela é fechada. Quando ele inicia, a janela é mostrada na tela.  
  
```py
janela.mainloop()
```  
  
### Exemplo Básico de GUI
  
```py
import tkinter as tk

janela = tk.Tk()
  
janela.title("Janelas com Tkinter")

janela.resizable(False,False)

janela.mainloop()
```  
  
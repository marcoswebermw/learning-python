### Tkinter
  
É uma biblioteca que permite a criação de ambientes gráficos em Python.  
  
Já vem embarcado com biblioteca padrão do Python.  
  
### Verificar Tkinter no shell
  
Para verificar se o módulo tkinter está realmente instalado use o comando:  
  
`python -m tkinter`  
  
Ou  
  
`python3 -m tkinter`  
  
### Verificar Tkinter no REPL(Read–eval–print loop) do Python
  
```py
import tkinter as tk

tk._test()
```  
  
### Instalando Tkinter  
  
Caso tenha algum problema e a Tkinter não esteja instalada use o camando abaixo para baixar no Linux a versão para python 3 da biblioteca.  
  
`sudo apt install python3-tk`   
  
  
### Extensão Ttk
    
Para usar o label, buttons e outros widgets precisamos importar também uma extensão chamada `ttk` que vem dentro do pacote do tkinter. Ela dá um melhor look and feel para aplicações tkinter.    
  
`from tkinter import ttk`  
  

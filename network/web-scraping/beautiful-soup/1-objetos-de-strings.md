## Objetos BeautifulSoup através de strings
  
Strings podem ser passadas para serem transformadas em objetos do Beautiful Soup e assim serem trabalhadas.  
   
> Objetos do Beautiful Soup, no código, geralmente são atribuidos começando com o nome `soup` como em `soup_alguma_nome`.  

```py
from bs4 import BeautifulSoup

minha_string = ´<h1>Olá Mundo!</h1>´
soup = BeautifulSoup(minha_string)

# Objeto agora é reconhecido como html(em forma de uma arvore de tags).
# A saída pode variar dependendo do parser usado.
print(soup)
```  
  

### Trabalhando com Parsers
  
Também é possível trabalhar com `xml` ao invéz de `html`. Isso é possível porque o Beautiful Soup através da classe `TreeBuilder` tem um parser que consegue trabalhar criando árvores tanto para `html` como também `xml`.   
  
Porém o padrão é o `html`. Por isso temos que indicar explicitamente no construtor do Beautiful Soup que queremos trabalhar com `xml`.  
  
O construtor pode receber um argumento chamado `features` que define o tipo de parser ou arquivo que será usado. Esse argumento pode ser uma `string` ou uma `lista de strings`. É recomendado sempre especificar o parser usado.  
  
Abaixo uma lista de parsers que poderm ser usados:    
  
| Parser | TreeBuilder | Features |
| --- | --- | --- |
| lxml | LXMLTreeBuilder | ['lxml','html','fast','permissive'] |
| html5lib | HTML5TreeBuilder | ['html','html5lib','permissive','strict','html5'] |
| html.parser | HTMLParserTreeBuilder | ['html','strict','html.parser'] |
| lxml | LXMLTreeBuilderForXML | ['xml','lxml','permissive','fast'] |
  
> Pode ocorrer uma exceção caso o parser não esteja instalado no sistema operacional. É necessário instalá-lo.  
  
### Instalando alguns parsers
  
```sh
pip3 install parse-helper html5lib
```
  
### Exemplos de uso dos parsers
  
* 'html'
  
```py
from bs4 import BeautifulSoup

minha_string = "<p>Meu Html</p>"
soup = BeautifulSoup(minha_string, 'html')
print(soup)
```   
   
* Features='xml'  
  
```py
from bs4 import BeautifulSoup

minha_string = "<p>Meu XML</p>"
soup = BeautifulSoup(minha_string, features='xml')
print(soup)
```  
  
* 'xml'

```py
from bs4 import BeautifulSoup

minha_string = "<p>Meu XML</p>"
soup = BeautifulSoup(minha_string, 'xml')
print(soup)
```  
  
* 'lxml'  

```py
from bs4 import BeautifulSoup

minha_string = "<p>Meu XML</p>"
soup = BeautifulSoup(minha_string, 'lxml')
print(soup)
```  
  
* 'html5lib'  

```py
from bs4 import BeautifulSoup

minha_string = "<p>Meu HTML5</p>"
soup = BeautifulSoup(minha_string, 'html5lib')
print(soup)
```  
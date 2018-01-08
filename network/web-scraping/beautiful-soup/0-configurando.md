### Configurando o ambiente
  
```sh
# Instalando
sudo pip3 install virtualenv  

# Criando ambiente
virutalenv -p python3.5 ambiente-beautiful-soup  

# Ativando ambiente
source ./ambiente-beautiful-soup/bin/activate  

# Desativando ambiente
deactivate  
```  
  
### Instalando Beautiful Soup no ambiente criado
  
```sh
pip3 install beautifulsoup4
```
  
### Testando o Beautiful Soup
  
Abra um interpretador python e tente importar o módulo, se tudo der certo, nada será exibido.  
  
```sh
python

from bs4 import BeautifulSoup
```  

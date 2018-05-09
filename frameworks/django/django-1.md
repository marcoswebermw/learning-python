# Configurando
  
## Criando o ambiente virtual e instalando o Django via pip.
  
```sh
# Criando ambiente virtual.
venv django -p python3.5

source django/bin/activate

# Instalando o Django.
pip install django

# Testando o Django.
python

import django

django.get_version()

# Outra forma de testar o Django.
python

import django

django.VERSION

# Testando a versão pelo shell
python -m django --version
```
  
## Criando um projeto
  
Será necessário criar uma estrutura de diretórios com vários arquivos de configurações para um projeto Django. Isso pode ser feito da seguinte maneira:
  
```sh
django-admin startproject novo_site
```
  
* Estrutura criada:
  
```sh
novo_site/
    manage.py
    novo_site/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```
  
- `novo_site/` - O diretório raiz para o projeto. Pode ter seu nome mudado.
  
- `manage.py` - Utilitário que faz a interação com o projeto Django.
  
- `novo_site/novo_site/` - Este segundo `novo_site` representa o pacote python do projeto e, que será usado para importar algum recurso.
  
- Agora os arquivos internos dentro do pacote `novo_site/novo_site/`:
  
    - `__init__.py` - Arquivo vazio que indica que este diretório é um pacote.  
    - `settings.py` - Configurações deste projeto.  
    - `urls.py` - As declarações das URLs deste projeto.  
    - `wsgi.py` - Relativos a servidores compatíveis com WSGI.  
  

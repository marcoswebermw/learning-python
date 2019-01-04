# Flask
  
É um microframework web minimalista(é o desenvolvedor que toma as decisões). Ele só fornece o núcleo, mas permite que sejam adicionadas extensões ao framework.  
  
## Depêndencias do Flask
  
Flask depende do motor(linguagem) de templete `Jinja` e o toolkit WSGI `Werkzeug`. Além desses, na instalação do Flask também são instaladas as ferramentas:  

- `MarkupSafe` contra injeção de dependências;  
- `ItsDangerous` garante integridade de cookies;  
- `Click` framework que permite a criação de aplicações de linha de comando.  
  
## Exemplo

Exemplo da aplicação simples, `hello.py`, retirada da documentação.  

```py
from flask import Flask
# Instanciando uma aplicação WSGI com `Flask(__name__)`.
# O primeiro argumento é o nome do módulo da aplicação.
# Aqui foi usado o `__name__` pois não sabemos se aplicação,
# está sendo executada daqui ou importada.
# Isto é um macete muito usado.
app = Flask(__name__)

# Decorator que indica a url que irá disparar essa função.
# O resultado será retornado para o navegador.
@app.route('/')
def hello_world():
    return 'Hello, World!'
```  

## Comandos

flask --help
flask routes
flask run
flask shell

## Outros para aprender
  
tinymongo
pymongo
blueprint
factories
sqlalchemy
flask-admin
wsgi
templates
wtforms
flask_simplelogin
jinja2
pytest-flask

## Referências
  
[Docs Flask](http://flask.pocoo.org/docs/1.0/);  
[Docs Flask Installation](http://flask.pocoo.org/docs/1.0/installation/#installation);  
# Cookies
  
Para pegar todos os cookies que um cliente transmite, use o atributo `cookies` que é um dicionário do objeto `request`.  

O objeto response através de `make_response()` permite o armazenamento de cookies pelo método `set_cookie()`.  

## Exemplos da documentação
  
- Lendo cookies

```py
from flask import request

@app.route('/')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.
```  

- Armazenando cookies  

```py
from flask import make_response

@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp
```  

## Referências
  
[Docs Flask Quick Start](http://flask.pocoo.org/docs/1.0/quickstart/#cookies);  

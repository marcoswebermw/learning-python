# Redirecionamento e Erros  

Redirecionamentos são feitos com a função `redirect()`. E uma requisição pode ser abortada antecipadamente com a função `abort()` que retornará um código indicando o erro.  

Exemplos da documentação  

Será feito um redirecionamento para uma página que não pode ser acessada por causa do código http de erro `401` que significa acesso negado. Essa é uma página de erro simples, preta e branca.  

```py
from flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()
```  

Para customizar a tela de erro use o decorator `errorhandler()`.  

```py
from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
```  

> Mais informações sobre como manipular erros acesse [Error Handling](http://flask.pocoo.org/docs/1.0/errorhandling/#error-handlers).  

## Referências  

[Docs Flask](http://flask.pocoo.org/docs/1.0/quickstart/#redirects-and-errors);  

[Error Handling](http://flask.pocoo.org/docs/1.0/errorhandling/#error-handlers);  

# Message Flashing  

O Flask nos trás um sistema de mensagens, que nos permite enviar informações para o usuário de forma simples. Não podem ser muito grandes, pois o browser ou servidor podem ter um limite para o tamanho de cookies.  

As mensagens flashing colocam uma informação(mensagem) no fim de uma requisição. Essa informação pode ser acessada na requisição seguinte(e somente nela).  

Para enviar uma mensagem use a função `flash` e para obté-las use `get_flashed_messages()`.  

## Exemplo da Documentação  

```py
# Arquivo python.
from flask import Flask, flash, redirect, render_template, \
     request, url_for

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)
```  

```html
<!-- layout.html -->
<!doctype html>
<title>My Application</title>
{% with messages = get_flashed_messages() %}
  {% if messages %}
    <ul class=flashes>
    {% for message in messages %}
      <li>{{ message }}</li>
    {% endfor %}
    </ul>
  {% endif %}
{% endwith %}
{% block body %}{% endblock %}
```  

```html
<!-- index.html -->
{% extends "layout.html" %}
{% block body %}
  <h1>Overview</h1>
  <p>Do you want to <a href="{{ url_for('login') }}">log in?</a>
{% endblock %}
```  

```html
<!-- login.html -->
{% extends "layout.html" %}
{% block body %}
  <h1>Login</h1>
  {% if error %}
    <p class=error><strong>Error:</strong> {{ error }}
  {% endif %}
  <form method=post>
    <dl>
      <dt>Username:
      <dd><input type=text name=username value="{{
          request.form.username }}">
      <dt>Password:
      <dd><input type=password name=password>
    </dl>
    <p><input type=submit value=Login>
  </form>
{% endblock %}
```  

## Referências  

[Docs Flask Message-Flashing](flask.pocoo.org/docs/1.0/quickstart/#message-flashing);  

[Docs Flask Message Flashings](http://flask.pocoo.org/docs/1.0/patterns/flashing/#message-flashing-pattern);  

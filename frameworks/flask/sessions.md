# Sessions  

O objeto `session` permite que sejam armazenadas informações do usuário em uma requisição. Essas informações podem ser levadas de uma requisição para a outra. A session trabalha com cookies só que de forma segura.  

É necessário ter uma chave secreta para trabalhar com session.  

A função `escape()` trata dos possíveis problemas de caracteres que podem acontecer de dados vindos de urls. Ele converte os caracteres `&`, `<`, `>`, `'`, `"` em string seguras para serem usadas no html. É usado quando não há um template engine(Jinja) em uso.  

## Exemplo da Documentação  

```py
from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
```  

## Gerando chaves secretas  

```sh
$ python -c 'import os; print(os.urandom(16))'
# b'_5#y2L"F4Q8z\n\xec]/'
```  

## Referências  

[Docs Flask Quick Start](flask.pocoo.org/docs/1.0/quickstart/#sessions);  

[Docs Flask API](http://flask.pocoo.org/docs/1.0/api/#sessions);  

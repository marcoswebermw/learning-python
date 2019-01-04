# Trabalhando com URLs
  
## Rotas
  
Rotas podem ser definidas através do decorator `app.route('rota')`. E logo em seguida é definida uma função ligada a esta rota. Ou seja, toda vez que a rota for chamada, a função será executada.  
  
Temos que ter cuidado quando usarmos rotas porque para o `Flask` a rota ´/teste/´ é diferente de `/teste` sem a barra final.


```py
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/bye')
    return '<html><body><strong>Bye!</strong></body></html>'
```
  
# Variáveis na Url
  
É possível passar variáveis na url. E estas variáveis possuem tipos. O padrão é ´string´, e portanto, é opcional especificá-la.  

Tipos:  

- string(padrão) -> Texto sem barra;
- int -> Inteiros positivos;
- float -> Números de ponto flutuante positivos;
- path -> Funciona como string, mas aceita barras;
- uuid -> Strings uuid.
  
```py
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath
```
  
## Url_for()
  
A função `url_for()` nos permite obter uma url de forma mais segura do que se digitarmos na mão. Sempre é retornado o caminho absoluto.  

Ela recebe como primeiro argumento uma função, que está relacionada com uma rota. E em seguida recebe quantos parâmetros nomeados forem necessários na formação das variáveis passadas pela url. Variáveis desconhecidas são anexadas e tratadas como query parameters.  

Além disso quando a usamos, ela limita o número de alterações que teríamos que fazer no código caso precisassemos alterar uma url.  

Ela trata do escaping de caracteres especiais e o uso de unicode de forma transparente. Simplifica o trabalho quando especificarmos o caminho do nosso código fora diretório root mas queremos tratar como se estivesse dentro dele.  

O Flask fornece uma função chamada `test_request_context()` que simula requisições mesmo quando estamos no shell do python. Ela será útil para mostrar o uso do `url_for()`.  

```py
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

with app.test_request_context():
    print(url_for('index'))  # /
    print(url_for('login'))  # /login
    print(url_for('login', next='/'))  # /login?next=/
    print(url_for('profile', username='John Doe')) # /user/John%20Doe

```
  
## Métodos HTTP
  
Uma rota por padrão no Flask só responde ao método `GET`. Para manipular outros métodos é necessário passar argumentos para o decorator `route()`. Com o `GET` presente, consequentemente também temos o `HEAD` e o `OPTIONS`.  

```py
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
```
  
## Arquivos Estáticos
  
Arquivos estáticos como arquivos do Javascript ou Css podem ser encontrados pelo Flask em um diretório chamado `/static` que deve ser colocado dentro do pacote de sua aplicação ou no caso de módulos, deve ficar em um diretório vizinho ao diretório da aplicação que o Flask o encontrará.  

Gerando urls para arquivos estáticos:
  
```py
url_for('static', filename='style.css') # static/style.css
```


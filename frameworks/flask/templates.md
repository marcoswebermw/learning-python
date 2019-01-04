## Templates
  
Flask oferece uso de templates no Python através do motor de templates `Jinja2` por padrão. Isto porque é muito trabalhoso manter código python que gera html, além de exigir muita atenção quanto a segurança da aplicação. O Jinja faz essas coisas automaticamente.  

O Flask procura os templates dentro de um diretório chamado `templates/`. Se nossa aplicação for um módulo, o diretório `templates` deve estar ao lado(mesmo nível) do nosso módulo. Se for um pacote, o diretório `templates` deve estar dentro do pacote.  

Um template poderá ser renderizado pelo método `render_template`, que recebe como parametros o nome do template, e as variáveis (parâmetros nomeados) que desejar passar para ele.  

Exemplo da documentação:
  
```py
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```
  
Dentro do template podemos passar váriaveis e usar estruturas condicionais, repetição, etc. Ele é muito útil para montar uma página através de herança de outras partes da página já construídas como o cabeçalho e rodapé.  

Exemplo de um template(documentação):
  
```html
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}
```
  
> É possível acessar dentro de um template objetos como: `request`, `session` , `g objects` e `get_flashed_messages()`.  

## Referências
  
[Docs Flask](http://flask.pocoo.org/docs/1.0/quickstart/#rendering-templates);

## Request
  
O request é um objeto que permite a recuperação de informações a cerca da requisição. Ele é importado através do comando `from flask import request`.
  
Para descobrir o método http que fez a requisição é só usar o atributo `request.method`. Se quisermos acessar os dados transmitidos por um formulário usamos o atributo `request.form['name']` passando a chave que indica o campo que queremos acessar o valor.
  
Se passarmos uma chave que não existe na tentativa de buscar um campo de um formulário será lançado um `KeyError` que poderá ser capturado, ou, se não for, será mostrada um página com o erro http `HTTP 400 - Bad Request`.
  
Parametros da url(query strings) como em: https://www.teste.com/?chave=valor podem ser obtidos através do método get do atributo `args`. Talvez seja melhor usá-lo em conjunto com a captura de `KeyError`, pois o parametro pode vir com campos inexistentes. Ele é usado da seguinte forma: `searchword = request.args.get('key', '')`.
  
## Exemplo de uso(Documentação)
  
```py
from flask import request

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
```
  
## Referências
  
[Docs Flask Request](http://flask.pocoo.org/docs/1.0/api/#flask.Request);  

[Docs Flask](http://flask.pocoo.org/docs/1.0/quickstart/#quickstart);  

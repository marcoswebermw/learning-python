# Deferred Request Callbacks Pattern
  
O Flask cria e passa objetos do tipo `response` em um nível abaixo de alguns métodos de callback. O que permite que esses métodos façam modificações no objeto response.  

Quando a manipulação de `request` começa, o objeto `response` ainda não foi criado. Ele é criado por uma view ou um componente do sistema.  

O Flask oferece alguns métodos para trabalharmos com callback durante as requisições. Eles estão acessíveis através de decorators.  

## before_request
  
O método `before_request` permite o registro de uma função para que ela execute sempre antes de `todas` as requisições. Ela não recebe argumentos. E se não retornar valor, será tratada como retorno de uma view.  

```py
@app.before_request
def callback_antes_do_request():
    print('Executado antes do request ser processado.')
```
  
## after_request
  
O método `after_request` faz o registro de uma função para ser executada depois de `todas` as requisições feitas. Essa função recebe como parâmetro um objeto da classe `response_class` e retorna também um objeto da mesma classe.  

Esse objeto response pode ser manipulado. Ele tem alguns métodos como o `response.get_data(as_text=True)` que pega os dados passados na requisição e os trata como strings.  

> Pode não ser executada no fim da requisição caso ocorra alguma exceção não manipulada.  

```py
@app.after_request
def callback_depois_do_request(response):
    # Imprime os dados da requisição.
    print( response.get_data(as_text=True) )
    # Retorna o objeto response.
    return response
```
  
## after_this_request
  
Ela executa depois que a função da view associada a ela é executada. Ela só executa para esta função.  

```py
@app.route('/')
def index():
    @after_this_request
    def add_header(response):
        response.headers['X-Foo'] = 'Parachute'
        return response
    return 'Hello World!'

@app.route('/')
def index():
    @after_this_request
    def imprimir(response):
        print('Executa depois desta requisição')
        return response
    return 'Retorna para response'
```
  
# Referências
  
[Docs Deferred Request Callbacks](http://flask.pocoo.org/docs/1.0/patterns/deferredcallbacks/);  

[Docs before_request](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.before_request);  

[Docs after_request](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.after_request);  

[Docs after_this_request](http://flask.pocoo.org/docs/1.0/api/#flask.after_this_request);  
[Python-Flask:-running-code-before-and-after-every-request](https://instructobit.com/tutorial/111/Python-Flask:-running-code-before-and-after-every-request);  
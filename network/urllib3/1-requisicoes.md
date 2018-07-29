# Requisições
  
A requisição pode receber algumas informações de cabeçalho, método http, e outro parâmetros.  

## Cabeçalhos Http
  
No argumento `headers` da requisição é possível passar informações de cabeçalho http por meio de um dicionário.  

```py
import urllib3

http = urllib3.PoolManager()

r = http.request('GET', 'http://httpbin.org/headers', headers={'X-Something': 'value'})

json.loads(r.data.decode('utf-8'))['headers'] # {'X-Something': 'value', ...}

```
  
## Query Parameters
  
Requisições do tipo `GET`, `HEAD` e `DELETE`, recebem parâmetros através do argumento `fields` do `request()`.  


```py
import urllib3

http = urllib3.PoolManager()

r = http.request('GET', 'http://httpbin.org/get', fields={'argumento': 'valor'})

json.loads(r.data.decode('utf-8'))['args'] # {'argumento': 'valor', ...}

```  

Para as requisições do tipo `POST` e `PUT` é preciso encodar os parâmetros na `url`.  

```py
import urllib3
from urllib.parse import urlencode

http = urllib3.PoolManager()

encoded_args = urlencode({'argumento': 'valor'})
url = 'http://httpbin.org/post?' + encoded_args

r = http.request('POST', url)
json.loads(r.data.decode('utf-8'))['args'] #{'argumento': 'valor'}

```  
  
**Dados do Formulário**
  
Para os dados que são enviados por formulários através do `POST` e `PUT` o `request` já faz o encode automatico através de dicionário no argumento `fields`.  

```py
import urllib3

http = urllib3.PoolManager()

r = http.request('POST', 'http://httpbin.org/post',fields={'campo': 'valor'})

json.loads(r.data.decode('utf-8'))['form'] # {'campo': 'valor'}

```  
  
  
> Exemplos tirados da documentação.
  

## Referências
  
[Docs urllib3](http://urllib3.readthedocs.io/en/latest/user-guide.html);  


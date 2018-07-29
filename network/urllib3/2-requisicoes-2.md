# Requisições
  
## JSON
  
É possível enviar um JSON encodado em uma requisição através do parâmetro `body` e definindo o `Content-Type:` no cabeçalho da requisição.  
  
```py
import urllib3
import json

http = urllib3.PoolManager()

dados = {'atributo': 'valor'}
dados_encodados = json.dumps(dados).encode('utf-8')

r = http.request('POST', 'http://httpbin.org/post', body=dados_encodados, headers={'Content-Type': 'application/json'})

json.loads(r.data.decode('utf-8'))['json'] # {'atributo': 'valor'}

```  

## Arquivos e dados binários
  
**Arquivos**
  
Para fazer upload de arquivos usando o enconde `multipart/form-data` é preciso passar uma tupla para o argumento `fields`. A tupla deve conter o `nome do arquivo` e os `dados`. Também é possível(não obrigatório) passar o tipo MIME explicitamente como terceiro elemento da tupla.  
  
```py
import urllib3
import json

http = urllib3.PoolManager()

with open('exemplo.txt') as arquivo:
    dados_arquivo = arquivo.read()
    r = http.request('POST', 'http://httpbin.org/post', 
        fields={'filefield': ('exemplo.txt', dados_arquivo, 'text/plain'),
        })

json.loads(r.data.decode('utf-8'))['files'] # {'filefield': '...'}
```
  
**Dados Binários**
  
Para enviarmos dados binários brutos só precisamos passá-lo pelo argumento `body`. E é boa prática também passar o `Content-Type` no cabeçalho.  

```py
import urllib3
import json

http = urllib3.PoolManager()

with open('exemplo.jpg', 'rb') as arquivo:
    dados_binarios = arquivo.read()
    r = http.request(
        'POST',
        'http://httpbin.org/post',
        body=dados_binarios,
        headers={'Content-Type': 'image/jpeg'})
        
json.loads(r.data.decode('utf-8'))['data']

```
  
> Exemplos tirados da documentação.
  

## Referências
  
[Docs urllib3](http://urllib3.readthedocs.io/en/latest/user-guide.html);  


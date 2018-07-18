# Urllib3
  
O módulo `urllib3` acompanha o python e nos permite trabalhar com o protocolo http e manipular urls.  

Ele tem características que ajudam os desenvolvedores como um pool para gerenciamento de todos os detalhes de conexões(`PoolManager`) e é thread safety.  

Ele basicamente funciona através do método `request` que faz requisições e retorna um objeto `HTTPResponse`. Este objeto provê os atributos `status`, `data` e `headers`.  

## Instalação
  
```py
pip install urllib3
```
  
> * Instalação caso necessário.  

## Uso
  
```py
import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'http://httpbin.org/robots.txt')

print(r.status)
print(r.data)
print(r.headers)
```  

## JSON
  
A resposta pode ser pega em formato JSON decodifindo e deserializando o atributo `data`:  

```py
import json

r = http.request('GET', 'http://httpbin.org/ip')

json.loads(r.data.decode('utf-8'))
#{'origin': '127.0.0.1'}

```
  
## Referências

[Docs](http://urllib3.readthedocs.io/en/latest/index.html)
  

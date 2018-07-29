# Timeout

A `urllib3` permite definir timeouts que indicam quanto tempo uma requisição continua executando até ser abortada.  

Ela é definida por um valor float passado como parâmetro de `request`.  

```py
import urllib3

http = urllib3.PoolManager()

http.request('GET', 'http://httpbin.org/delay/4', timeout=5.0)

```
  
## Classe Timeout
  
O uso de uma instância dessa classe permite um controle maior e específico sobre o tempos limite de conexão e leitura.  

```py
http.request('GET', 'http://httpbin.org/delay/3', timeout=urllib3.Timeout(connect=1.0))

http.request('GET', 'http://httpbin.org/delay/3', timeout=urllib3.Timeout(connect=1.0, read=2.0))
```
  
> Exemplos tirados da documenteção.  
  
    
## Configurações globais
  
Ao invés de colocar as regras de timeout individualmente, é possível fazê-lo de forma global através do `PoolManager()`. Ele praticamente aceita todas as regras que o request suporta.  

Mas essas regras globais podem ser sobrescritas pelos métodos `request`.  

```py
http = urllib3.PoolManager(timeout=3.0)

http = urllib3.PoolManager(timeout=urllib3.Timeout(connect=1.0, read=2.0))
```

## Referências
  
[Docs urllib3](http://urllib3.readthedocs.io/en/latest/user-guide.html);  

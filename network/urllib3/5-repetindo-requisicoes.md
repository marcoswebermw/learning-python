# Repetindo e redirecionando requisições

A `urllib3` pode automaticamente repetir requisições idempotentes(que recebem sempre a mesma entrada e retornam a mesma saída).  

O padrão é que a `urllib3` repita uma solicitação 3 vezes e siga até 3 redirecionamentos. É possível mudar este padrão através de parâmetros do método `request()`.  


```py
import urllib3
r = urllib3.PoolManager()
# Tentativas de solicitação através do `retries`
r.request('GET', 'http://httpbin.org/ip', retries=5)

# Desabilitando todos redirecionamentos lógicos e tentativas de requisição.
r.request('GET', 'http://httpbin.org/redirect/1', retries=False)

# Desabilitando somente redirecionamentos e mantendo tentativas de requisição.
r.request('GET', 'http://httpbin.org/redirect/1', redirect=False)
```
  
## Classe Retry
  
O uso de uma instância dessa classe permite um controle maior sobre solicitações e redirecionamentos.  

```py
# 2 tentativas e 3 redirecionamentos.
r.request('GET', 'http://httpbin.org/redirect/3', retries=urllib3.Retry(2, redirect=3))
```
  
## Desabilitando Exceções
  
Para evitar muitas exceções de redirecionamento e apenas mostrar o erro `http 302`.  

```py
resp = r.request('GET', 'http://httpbin.org/redirect/3', retries=urllib3.Retry(2, redirect=3, raise_on_redirect=False))

resp.status # 302
```
  
> Lista de exceções: [Exceções urllib3](http://urllib3.readthedocs.io/en/latest/reference/index.html#module-urllib3.exceptions)  
  

> Exemplos baseados na documentação.
  
## Configurações globais
  
Ao invés de colocar as regras de requisição e redirecionamento individualmente, é possível fazê-lo de forma global através do `PoolManager()`. Ele praticamente aceita todas as regras que o request suporta.  

Mas essas regras globais podem ser sobrescritas pelos métodos `request`.  

```py
resp = urllib3.PoolManager(retries=False)
```

## Referências
  
[Docs urllib3](http://urllib3.readthedocs.io/en/latest/user-guide.html);  

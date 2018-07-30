# Stream
  
O stream é usado quando existe uma grande quantidade de dados para serem transportados pela rede. Se usarmos a forma convencional, baixando uma responta inteira de uma vez, provavelmente irá sobrecarregar os recursos da máquina como a memória. Sem falar na lentidão no uso desta prática.  

Usando a técnica de stream, vamos passando os dados em pedaços menores do servidor para o cliente, ganhando desempenho.  

Para usarmos streams com a `urllib3` temos que fazer uso do argumento de `urllib3.request()` chamado `preload_content=False` que indica que usaremos stream. E no final usamos o método `urllib3.release_conn()` para liberar a conexão para voltar ao pool de conexões.  

```py
import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'http://httpbin.org/bytes/1024', preload_content=False)

# Pegando 32 bytes por vez.
tamanho_total = 0
for pedaco in r.stream(32):
    print(pedaco)
    tamanho_total = tamanho_total + 32
    print('\nTransmitidos {} bytes.\n'.format(tamanho_total))
r.release_conn()
```  

> O método `read()` pode ser uma alternativa ao método `stream()`.  

## Referências
  
[Docs Urllib3](http://urllib3.readthedocs.io/en/latest/advanced-usage.html);  

[Docs Urllib3 Referências](http://urllib3.readthedocs.io/en/latest/reference/)
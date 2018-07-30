# Pool
  
A `urllib3` nos fornece 2 tipos de pools para trabalharmos. O `PoolManager` que é o que mais usamos e o `HTTPConnectPool`. Abaixo são listadas as características de cada um:  

**PoolManager:**  

- Multithread -> Aceita várias conexões para um ou mais hosts;  

- O Padrão é suportar 10 conexões máximas mas pode ser alterado;  
- Gerencia automaticamente o pool de conexões para cada host.  

- Pode aumentar ou diminuir as conexões com o host dependendo da situação de forma automatica;  

- Pode fazer várias requisições para vários hosts diferentes. Tem alto desempenho.  

- Pode floodar um host(e ser bloqueado) por causa da quantidade de threads fazendo requisições para este host simultaneamente, fazendo com que sistemas anticrawler pensem ser um ataque.  

- Maior número de conexões aumentam também o consumo nos socketes e aumenta o consumo de memória.  


**HTTPConnectionPool:**  

- É single thread.  

- Mantém um pool de conexões individuais;  

- São usadas em requisições individuais e depois retornam ao pool.  

- O limite máximo indica quantas conexões ele vai manter e gravar no pool. Conexões além poderão ser criadas mas não serão salvas e retornadas ao pool. O padrão é uma conexão para reuso;
  
- Se `block=True` o limite máximo de conexões será respeitado. Evita floodar um site com várias requisições;  

- É mais lenta que o PoolManager se usada com o limite padrão de conexões.  

- Recebe um host e não urls;  

## Exemplos
  
```py
import urllib3
http = urllib3.PoolManager(maxsize=10, block=True)
http2 = urllib3.HTTPConnectionPool('google.com', maxsize=10, block=True)
```  

> Exemplo baseado na docomentação.


## Referências
  
[Docs Urllib3](http://urllib3.readthedocs.io/en/latest/advanced-usage.html);  
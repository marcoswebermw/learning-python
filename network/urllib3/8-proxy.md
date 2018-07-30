# Proxy
  
Nesse caso os proxies são úteis quando não queremos que um determinado site seja acessado diretamente por nosso ip. Com o proxy todo o tráfego passa antes por ele e depois vai ao destinatário chegando com ip do proxy e não o nosso.  
  
Com a urllib3 o uso de proxies é feito através da classe `ProxyManager` que recebe como principal parâmetro o ip do proxy que será usado. O seu funcionamento é quase igual a um `PoolManager`.  

```py
import urllib3

proxy = urllib3.ProxyManager('https://91.211.189.106:8080')
req = proxy.request('GET', 'https://httpbin.org/ip')
print(req.data)
```  

> Proxies free podem ser encontrados em: 
[free-proxy-list](https://free-proxy-list.net). Dê preferência para os do tipo `elite proxy`.  

## Referências
  
[Docs Urllib3](http://urllib3.readthedocs.io/en/latest/advanced-usage.html);  
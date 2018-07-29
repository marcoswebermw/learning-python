# Verificação de certificados
  
Apesar de ser uma boa prática, o `urllib3` não faz a verificação de certificados `SSL` em requisições `https` por padrão. Para fazer isso é preciso instalar o pacote `certifi`:

`pip install certifi`  

No `PoolManager()` é possível fazer essa verificação. O parâmetro `cert_reqs='CERT_REQUIRED'` indica a verificação dos certificados. Já o `ca_certs=certifi.where()` indica que os certificados serão obtidos automaticamente.  

Para colocar certificados do próprio sistema operacional use o `ca_certs` com o caminho para os certificados.  
  
Serão lançadas exceções `SSLError` caso a verificação falhe.  

```py
import certifi
import urllib3
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
```
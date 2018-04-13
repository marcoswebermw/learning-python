# Executando no servidor
  
A equipe do Django fornece um servidor web feito em python para uso em desenvolvimento. Fica mais fácil testar aplicações django nele. Ele não deve ser usado em produção.
  
```py
python manage.py runserver
```
  
Acima estamos interagindo com o projeto através do `manage.py` e executando o comando `runserver` que inicia o servidor web de desenvolvimento no endereço `http://127.0.0.1:8080`.
  
## Trocando a porta do servidor
  
A porta do servidor pode ser trocada na chamada do servidor.
  
```py
python manage.py runserver 8080
```
  
## Trocando o endereço IP do servidor
  
O servidor pode ser executado com outro IP. Para isso passe-o juntamento com sua porta durante a chamado do servidor.
  
```py
python manage.py runserver 0.0.0.0:8080
```
  
> O endereço `0.0.0.0` indica todos os endereços públicos da rede. Este endereço também pode ser usado em sua forma de atalho, que é `0:8000`.
  
> O servidor não precisa ser reiniciado em alterações de código. Somente será necessário quando ocorrerem ações como a adição de arquivos.
  
## Referências
  
[Docs Django](https://docs.djangoproject.com/pt-br/2.0/intro/tutorial01/)  
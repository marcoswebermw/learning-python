# Logging com python

* O módulo logging faz parte da biblioteca padrão do python.  
* Permite o rastreamento dos eventos que ocorrem durante a execução do software.  
* Pode enviar logs tanto para o console como também para um arquivo.  

--------------------------------

### Usando o comando print no lugar do logging temos:  
  * Difícil discriminar entre o que é debug do que só é saída normal do programa.
  * Difícil desabilitar todos os prints quando for preciso.
  * Difícil de removê-los quando terminar o debug.  

### Usando o logging:

```py
import logging

class Teste():
	def __init__(self, mensagem):
		logging.debug('A mensagem é {}'.format(mensagem))
```


### Níveis de logging

* O logging tem vários níveis.
* Eles definem o nível de detalhamento das saídas dos logs.
* O nível padrão é o `logging.WARNING`.
* O que nós geralmente usamos é o `logging.DEBUG` através do método `logging.debug()`.
* Os níveis são `constantes`. Cada constante tem um valor associado.
* O nível com valor mais alto é o `CRITICAL` com valor `50`.
* O nível mais baixo é o NOTSET quem tem valor `0`.

---------------------------------------------------

| Nível | Valor | Função | Uso |
| --------- | --------- | --------- | --------- |
| *NOTSET* | 0 | ? | ? |
| *DEBUG* |10|logging.debug()|Mostrar informações detalhadas, e diagnosticar problemas.|
| *INFO* |20|logging.info()|Confirma se tudo funciona como esperado.|
| *WARNING* |30|logging.warning()|Indica que aconteceu ou acontecerá algo inesperado.|
| *ERROR* |40|logging.error()|Indica um problema mais grave.|
| *CRITICAL* |50|logging.critical()|Indica um erro gravíssimo. O programa pode ficar incapz de rodar.|


* Para definir os níveis usa-se:

```py
logging.basicConfig(level=logging.DEBUG)

```

### Mandando o log para um arquivo

```py
logging.basicConfig(filename="arquivo.log", level=logging.DEBUG)
```

### Usando LogRecord Attributes

* Pode-se usar mais atributos em `logging.basicConfig()`. 

* Acesse a lista completa aqui https://docs.python.org/3/library/logging.html#logrecord-attributes

### Exemplos:

```py
logging.basicConfig(filename="arquivo.log", level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")
```

---------------------------------------------------

|Atributo|Função|
| --------- | --------- | 
| *%(asctime)s* |Registro do timestamp no horário que o log foi gerado.|
| *%(levelname)s* |Nível do logging.|
| *%(funcName)s* |Nome da função.|
| *%(message)s* |Mensagem a ser exibida.|



### Links de referências:

* https://docs.python.org/3/howto/logging.html
* https://www.digitalocean.com/community/tutorials/how-to-use-logging-in-python-3
* https://docs.python.org/3/library/logging.html#logrecord-attributes

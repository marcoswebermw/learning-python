# TimeIt
  
O `timeit` é um módulo que serve para medir o tempo de execução de um determinado código em Python.  
  
Com ele podemos verificar o desempenho de trechos de código e determinar qual a melhor opção para determinada situação.  

O timeit pode ser executado tanto na linha de comando quanto no próprio código python.  

## `Timer(stmt='pass',setup='pass',timer=<timerfunction>)`
  
Classe para temporizar pequenas quantidades de código. Seu construtor recebe três parâmetros opcionais.  

- O primeiro parâmetro `stmt` define a sentença ou declaração que será executada. Pode ser uma função.  

- O segundo parâmetro `setup` é usado quando queremos usar funções que nós definimos. Ele contém a declaração de import.   

- O terceiro parâmetro `timer` é uma função de timer mas que depende da plataforma. Este parâmetro não sei como usar e não uso.  

A classe `Timer()` tem alguns métodos. Os dois principais são:  

* `timeit(number=1000000)` - Executa a expressão de ´setup´ uma vez, e depois executa a expressão ´principal' um determinado número de vezes, retornando o tempo em segundos, representado como float que ela levou para executar. O número padrão de repetições é 1000000.  

* `repeat()` - É uma espécie de atalho para o método `timeit()`. O `repeat()` executa o método `timeit()` um número de vezes e retorna uma lista com os tempos das execuções feitas.  

Podemos, passar ou não, parâmetros para o método `repeat()`. O primeiro parâmetro determina a quantidade de vezes que o teste será feito(vezes que o timeit() será chamado). O segundo indica o número de execuções(repetições da expressão).  

O padrão, sem parâmetros, é que o repeat execute 3 baterias de 1.000.000 de execuções cada, e no final retorne uma lista de tempos.  

> Para melhorar o desempenho, por padrão, o `timeit` desliga o `garbage collection`. Para ligá-lo use como o parâmetro `setup` o valor `'gc.enable()'`.  

## Exemplo
  
```py
from timeit import Timer

sentenca = '[x for x in range(1,10)]'

t = Timer(sentenca)
print('Sem Garbage Collection')
print( t.timeit() )

t = Timer(sentenca, 'gc.enable()')
print('Com Garbage Collection')
print( t.timeit() )
```

## Referências
  
* [PythonHelp](https://pythonhelp.wordpress.com/2011/09/13/medindo-tempo-de-execucao-de-programas-python/)  

* [Docs Python](https://docs.python.org/3.0/library/timeit.html)  
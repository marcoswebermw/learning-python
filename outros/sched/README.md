# Sched
  
`Sched` é um agendador de tarefas. Funciona como o `cron` nos Unix ou `agendador de tarefas` no Windows. A vantagem é que ele pode ser rodado direto de um script Python independente de plataforma. Ele permite ser usado em ambiente multi-thread de forma segura.  

O `sched` disponibiliza a classe `sched.scheduler` que oferece alguns métodos e atributos para permitir que suas instâncias agendem tarefas.  

Cada evento agendado é colocado em uma fila com prioridade. Quando for executado ou cancelado sai da mesma.

## Classe `sched.scheduler(timefunc=time.monotonic, delayfunc=time.sleep)`

A classe `scheduler` recebe duas funções **opcionais**(à partir da versão 3.3) como argumento: `timefunc` e `delayfunc`.  

Essas funções servem para indicar que funções externas serão usadas para se trabalhar com o tempo.

* `timefunc`

A `timefunc` retorna um número que representa o tempo. Ela recebe por padrão `time.monotonic` que indica que será usado um valor que represente a data.  

Esse valor vem sendo somado à partir de uma data no passado. É útil para se fazer calculos com datas e horas. Depois é só converter para um formato legível, caso necessário.  

Se `time.monotonic` não estiver disponível será usada `time.time` em seu lugar. Essa última usa um valor em segundos.  
* `delayfunc`
  
É uma função que será responsável pelo gerenciamento do delay no agendamento. Por padrão é usado a função built-in `time.sleep` como função padrão de delay.  

## Referências
  
* [Docs Python](https://docs.python.org/3/library/sched.html)  
* [bip.weizmann](https://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/sched/index.html)  
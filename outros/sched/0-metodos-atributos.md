# Métodos e Atributos de `Scheduler`
  
Às instâncias de `sched.scheduler` tem acesso aos seguintes métodos e atributos para tratar do agendamento de tarefas:  

* `scheduler.enterabs(time, priority, action, argument=(), kwargs={})`
  
Serve para agendar um novo evento com horário absoluto(exato) para ser executado.  

O parâmetro `time` define quando o evento será executado. Tem que ser compatível com `timefunc`.
  
O segundo parâmetro define a prioridade. Um valor menor tem prioridade mais alta. Quem tem prioridade mais alta executa primeiro.  

O terceiro parâmetro, `action` é uma função que representa o que vai ser executado quando o tempo do agendamento for atingido. Ela pode receber ou não argumentos. Estes argumentos podem estar em forma de listas(*argument) ou dicionários(**kwargs).  

Retorna um ID para possível cancelamento do evento.  

* `scheduler.enter(delay, priority, action, argument=(), kwargs={})`
  
Serve para agendar um novo evento com horário relativo(delay) para ser executado. Os seus parâmetros funcionam de forma parecida com `entertabs`. Em geral ele é mais usado do que o `entertabs`.  

* `scheduler.cancel(event_id)`
  
Remove um evento da fila. Uma `ValueError` será lançada se o evento não existir.  

* `scheduler.empty()`
  
Irá retornar `True` se a fila de eventos estiver vazia.
  
* `scheduler.run(blocking=True)`
  
Roda todos os eventos agendados. Se `blocking=False` Tentará rodar todos os eventos assim que possível, se existirem.  
  
* `scheduler.queue`

Atributo que retorna uma lista de eventos, na fila, que estão prontos para serem executados. Eles estão dispostos por ordem de prioridade. O retorno do tipo `named tuple`.

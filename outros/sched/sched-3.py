# Overlap
# Os eventos rodam por padrão em uma mesma thread.
# Quando um evento demora muito para ser executado,
# o evento seguinte é adiado e executado imediatamente
# após o fim do primeiro. Nenhum evento é perdido.

import sched
import time

agendador = sched.scheduler(time.time, time.sleep)


def evento_longo(nome):
	print('\nInício do Evento :', time.time(), nome)
	time.sleep(2)
	print('Fim do Evento:', time.time(), nome)


print('Tempo Inicial:', time.time())
agendador.enter(2, 1, evento_longo, ('Primeiro', ))
agendador.enter(3, 1, evento_longo, ('Segundo', ))

agendador.run()

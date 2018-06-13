import sched

agendador = sched.scheduler()

def mostraMsg():
    print('\nOlá Mundo!')
    agendador.enter(delay=3, priority=0, action=mostraMsg)

mostraMsg()

try:
    agendador.run(blocking=True)
except KeyboardInterrupt:
    print('\nAgendamento Interrompido.')




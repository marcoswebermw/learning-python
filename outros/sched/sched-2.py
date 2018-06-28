import sched
import time

tempo = time.time
retardo = time.sleep

agendador = sched.scheduler(tempo, retardo)

def mostrar_msg(msg):
    print("Tempo: {} - Mensagem: {}".format(tempo(), msg) )

print('Tempo Inicial:', tempo())
agendador.enter(2, 1, mostrar_msg, ('Abacaxi',))
agendador.enter(3, 1, mostrar_msg, ('Maçã',))

agendador.run()
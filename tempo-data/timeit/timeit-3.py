# Com função
import timeit

def criaLista(x, y):
    lista = [x for x in range(x,y+1)]

# Parâmetro 1: chama a função.
# Parâmetro 2: importa a função deste módulo.
t = timeit.Timer('criaLista(1,10)', 'from __main__ import criaLista')

print( t.timeit() )
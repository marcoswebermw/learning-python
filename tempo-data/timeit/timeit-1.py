# Com timeit()
from timeit import Timer

sentenca = '[x for x in range(1,10)]'

t = Timer(sentenca)
print('Sem Garbage Collection')
print( t.timeit() )

t = Timer(sentenca, 'gc.enable()')
print('Com Garbage Collection')
print( t.timeit() )


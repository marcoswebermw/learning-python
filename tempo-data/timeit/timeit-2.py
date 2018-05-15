# Com repeat()
from timeit import Timer

sentenca = '[x for x in range(1,10)]'
t = Timer(sentenca)

print('Repete: [x for x in range(1,10)] 1000000 em 3 Baterias:\n')
print( t.repeat() )

print('\nRepete: [x for x in range(1,10)] 1000000 em 2 Baterias:\n')
print( t.repeat(2, 1000000) ) # Repete o timeit 1000000 vezes em 2 baterias.

print('\nRepete: [x for x in range(1,10)] 1000000 em 1 Bateria:\n')
print( t.repeat(1, 1000000) ) # Repete o timeit 1000000 vezes em 1 bateria.
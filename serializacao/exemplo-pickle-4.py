import pickle

lista = ['Olá Mundo!', 100, 'ABACAXI']
serializado = pickle.dumps(lista)
print(serializado)
print('\nTipo serializado: {}'.format(type(serializado))) # <class 'bytes'>

deserializado = pickle.loads(serializado)
print('\nDeserializado: {}'.format(deserializado))
print('\nTipo deserializado: {}'.format(type(deserializado))) # <class 'list'>
# _*_ coding:utf-8 _*_

class Pai(object):
        pass

class Filha(Pai):
        pass

class Neta(Filha):
        pass

# Verifica se 'Pai' é subclasse de 'Filha'
print("'Pai' é subclasse de 'Filha': %s" %issubclass(Pai, Filha))

# Verifica se 'Filha' é subclasse de 'Pai'
print("'Filha' é subclasse de 'Pai': %s" %issubclass(Filha, Pai))

# Verifica se 'Filha' é subclasse de 'Neta'
print("'Filha' é subclasse de 'Neta': %s" %issubclass(Filha, Neta))

# Verifica se 'Neta' é subclasse de 'Filha'
print("'Neta' é subclasse de 'Filha': %s" %issubclass(Neta, Filha))

# Verifica se 'Pai' é subclasse de 'Neta'
print("'Pai' é subclasse de 'Neta': %s" %issubclass(Pai, Neta))

# Verifica se 'Neta' é subclasse de 'Pai'
print("'Neta' é subclasse de 'Pai': %s" %issubclass(Neta, Pai))

print("\n")

print("\nQuem é a superclasse de Pai: ")
print(Pai.__bases__)
print("\nQuem é a superclasse de Filha: ")
print(Filha.__bases__)
print("\nQuem é a superclasse de Neta: ")
print(Neta.__bases__)

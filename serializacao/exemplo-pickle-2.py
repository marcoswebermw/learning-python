import pickle

# Essa classe tem que ser criada novamente aqui.
# Essa classe foi criada no 'exemplo-pickle-1.py'
# Ela tem que ser vazia aqui.
# Se ela não for criada o Pickle não funciona.
class Pessoa(object):
    pass

arq = open('pessoa.pkl', 'rb')
obj = pickle.load(arq)
arq.close()

print('Nome: {}\n Cor: {}\n Profissão: {}'.format(
    obj.nome, obj.cor, obj.profissao))
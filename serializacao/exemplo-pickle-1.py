# Exemplo pickle.dump()
import pickle

class Pessoa(object):
    def __init__(self):
        self.nome = 'Hulk'
        self.cor = 'Verde'
        self.profissao = 'Super-herói'

obj = Pessoa()

arq = open('pessoa.pkl', 'wb')
pickle.dump(obj, arq)
arq.close()



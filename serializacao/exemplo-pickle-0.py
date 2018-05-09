import pickle

lista = ['Olá Mundo!', 100, 'ABACAXI']
# O arquivo tem que ser salvo em binário.
# O dump recebe o objeto e o arquivo onde irá gravá-lo.
pickle.dump(lista, open('lista.pkl','wb'))

deserializando = pickle.load(open('lista.pkl','rb'))
print(deserializando)

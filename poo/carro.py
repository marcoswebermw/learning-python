class Carro:
        def __init__(self, nome, ano):
                print('INICIANDO CLASSE...')
                self.__nome = nome
                self.__ano = ano

        def obter_nome(self):
                return self.__nome

        def obter_ano(self):
                return self.__ano

carro = Carro('Ferrari', 2016)
print(carro.obter_nome())
print(carro.obter_ano())

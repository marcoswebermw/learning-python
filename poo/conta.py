# _*_ coding:utf-8 _*_
"""
PYTHON SÓ TEM DOIS MODOS DE ENCAPSULAMENTO: PUBLIC(PADRÃO) E PRIVATE(EX.: __atributoPrivado = 0).
ATRIBUTOS E MÉTODOS PRIVADOS COMEÇAM COM "__" UNDERSCORE NA FRENTE DO NOME.

EXISTEM MÉTODOS ESPECIAIS:
__init__ -> MÉTODO CONSTRUTOR.
__add__ -> MÉTODO QUE RECEBE O SELF E OUTRO OBJETO DE MESMA CLASSE E FAZ A SOMA DE ALGUM ATRIBUTO EM COMUM DIRETAMENTE.
__sub__ -> MÉTODO QUE RECEBE O SELF E OUTRO OBJETO DE MESMA CLASSE E FAZ A SUBTRAÇÃO DE ALGUM ATRIBUTO EM COMUM DIRETAMENTE.
__mult__ -> MÉTODO QUE RECEBE O SELF E OUTRO OBJETO DE MESMA CLASSE E FAZ A MULTIPLICAÇÃO DE ALGUM ATRIBUTO EM COMUM DIRETAMENTE.
__div__ or __truediv__ -> MÉTODO QUE RECEBE O SELF E OUTRO OBJETO DE MESMA CLASSE E FAZ A DIVISÃO DE ALGUM ATRIBUTO EM COMUM DIRETAMENTE.
__doc__ -> MOSTRA A DOCUMENTAÇÃO DA CLASSE.
__call__ -> FAZ COM QUE O MÉTODO DA CLASSE POSSA SER CHAMÁVEL.

APESAR DE NÃO SER NECESSÁRIO É BOA PRÁTICA INDICAR QUE A CLASSE CRIADA HERDA DA CLASSE object.
'class Conta(object):' é melhor do que 'class Conta:'
"""

class Conta(object):
        """
                A classe Conta representa alguma conta do mundo real.
        """
        num_contas = 0
        
        def __init__(self, id, saldo):
                """
                        Documentação do construtor da classe conta.
                """
                self.id = id
                self.saldo = saldo
                Conta.num_contas += 1

        def __str__(self):
                return 'ID: %.3i Saldo: R$ %.2f' %(self.id, self.saldo)

        def __add__(self, outro):
                self.saldo += outro.saldo

        def __sub__(self, outro):
                self.saldo -= outro.saldo

        def __mul__(self, outro):
                self.saldo *= outro.saldo

        # def __div__(self, outro):
        def __truediv__(self, outro):
                self.saldo /= outro.saldo

        def __call__(self):
                print("Sou chamável")
                
                
conta_1 = Conta(1, 10)
conta_2 = Conta(2, 2)

# ATRIBUTO DE CLASSE E NÂO DE OBJETO
print("\nNúmero de contas criadas: %i" %Conta.num_contas)

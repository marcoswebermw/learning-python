# _*_ encoding:utf-8 _*_

class ClassePai:
        var1 = "Variável 1"

class ClasseFilha(ClassePai):
        pass


classe_pai = ClassePai()
classe_filha = ClasseFilha()
print(classe_pai.var1)
print(classe_filha.var1)


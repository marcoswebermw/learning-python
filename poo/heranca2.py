# _*_ coding:utf-8 _*_

class Mamifero(object):
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero

    # Método Abstrato
    def fala(self):
        pass


# -------------------------------------------------------------------------------------

class Pessoa(Mamifero):
    def __init__(self, nome, idade, genero, cabelo):
        # Seguem 3 formas de chamar o construtor da classe base(pai).
        # super(Pessoa, self).__init__(nome, idade, genero)  # Python2 - Deixa o interpretador achar a classe certa.
        # Mamifero.__init__(self, nome, idade, genero) # Chamando o construtor pai diretamente.
        super().__init__(nome, idade, genero)  # Em Python3 - Permite que o interpretador ache a classe correta para vc.
        self.cabelo = cabelo

    def __str__(self):
        return "Nome: %s, Idade: %i, Gênero: %s, Cabelo: %s" % (self.nome, self.idade, self.genero, self.cabelo)

    def fala(self):
        return "Oi! Eu me chamo"
        

# -------------------------------------------------------------------------------------

class Cachorro(Mamifero):
    def __init__(self, nome, idade, genero, raca):
        # super(Cachorro, self).__init__(nome, idade, genero)
        # Mamifero.__init__(self, nome, idade, genero)
        super().__init__(nome, idade, genero)
        self.raca = raca

    def fala(self):
        return "Au! Au! Au!"

    def __str__(self):
        return "\nNome: %s, Idade: %i, Gênero: %s, Raça: %s" % (self.nome, self.idade, self.genero, self.raca)


# -------------------------------------------------------------------------------------

pessoa_1 = Pessoa('Margot Robbie', 26, 'Feminino', 'loira')
pessoa_2 = Pessoa('Scarlett Johanson', 31, 'Feminino', 'ruiva')

print(pessoa_1)
print("%s %s\n" % (pessoa_1.fala(), pessoa_1.nome))
print(pessoa_2)
print("%s %s\n" % (pessoa_2.fala(), pessoa_2.nome))

cachorro_1 = Cachorro('Grafite', 8, 'Masculino', 'Bulldog Francês')
print(cachorro_1)
print("%s" % cachorro_1.fala())


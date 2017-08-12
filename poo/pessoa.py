# _*_ coding: utf-8 _*_
class Pessoa:
        def __init__(self, nome, idade, peso, altura):
                self.nome = nome
                self.idade = idade
                self.peso = peso
                self.altura = altura            
                print("Pessoa criada.")

        def envelhecer(self, idade):
                self.idade += idade
                if self.idade < 21:
                        self.altura += 0.05

        def engordar(self, peso):
                self.peso += peso

        def emagrecer(self, peso):
                self.peso -= peso

        def crescer(self, altura):
                self.altura += altura

        def imprimir_detalhes(self):
                print("Nome: %s" %(self.nome))
                print("Idade: %d" %(self.idade))
                print("Peso: %.2f" %(self.peso))
                print("Altura: %.2f" %(self.altura))
                print("--------------------------------")


p = Pessoa('Scarlett Johanson', 31, 58, 1.63)
p.imprimir_detalhes()
p.envelhecer(1) 
p.engordar(2)
p.emagrecer(1)
p.crescer(0.05)

p.imprimir_detalhes()

print("Dicionário criado implicitamente para o objeto:")
print(p.__dict__)


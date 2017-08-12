# _*_ coding:utf-8 _*_
class Quadrado:
        def __init__(self, lado):
                self.lado = lado
                print("Quadrado criado.")

        def muda_lado(self, lado):
                self.lado = lado

        def mostra_lado(self):
                return self.lado

        def calcula_area(self):
                return self.lado * self.lado


class Retangulo:
        def __init__(self, base, altura):
                self.base = base
                self.altura = altura
                print("Retângulo criado.")

        def muda_lado(self, base, altura):
                self.base = base
                self.altura = altura

        def mostra_lado(self):
                return "Base: %d, Altura: %d" %(self.base, self.altura)

        def calcula_area(self):
                return self.base * self.altura

        def calcula_perimetro(self):
                return 2*(self.base + self.altura)


q = Quadrado(2)
print("Lado: %d --- Área do quadrado: %d" %(q.mostra_lado(), q.calcula_area()) )

q.muda_lado(5)
print("Lado: %d --- Área do quadrado: %d" %(q.mostra_lado(), q.calcula_area()) )

r = Retangulo(3,8)
print("%s --- Área do retângulo: %d --- Perímetro: %d" %(r.mostra_lado(), r.calcula_area(), r.calcula_perimetro()) )

r.muda_lado(4,6)
print("%s --- Área do retângulo: %d --- Perímetro: %d" %(r.mostra_lado(), r.calcula_area(), r.calcula_perimetro()) )

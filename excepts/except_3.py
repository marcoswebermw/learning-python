# -*- coding: utf-8 -*-
 
# Criando minha própria exceção através da classe Exception.

class ValorRepetidoErro(Exception):

    def __init__(self, valor):
        self.valor = valor
    
    def __str__(self):
        return "O valor %i já foi digitado antes." %(self.valor)


lista = []

for i in range(3):
    try:
        valor = int(input("Digite um valor: "))

        if valor not in lista:
            lista.append(valor)
        else:
            raise ValorRepetidoErro(valor) # Chamando a exceção criada passando um valor.

    except ValueError: # Exceção do sistema, que verifica se só números foram digitados.
        print("Só digite números.")
        break


print("A lista digitada foi: ", lista)
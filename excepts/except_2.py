# -*- coding: utf-8 -*-

# Usando uma exceção específica da linguagem.
# ValueError verifica se foi digitado algo diferente de números.

try:
    num = int(input("Digite um valor: "))

except ValueError:
    print("Digite apenas números.")

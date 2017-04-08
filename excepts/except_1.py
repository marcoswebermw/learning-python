# -*- coding: utf-8 -*-

try:
    valor = int(input("Informe um valor: "))
except:
    print("Valor, tem que ser um valor inteiro válido.")
finally:
    print("Programa encerrado.")

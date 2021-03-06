# coding:utf-8
import os
os.system("clear")

# permutações recursivas.

# retorna uma lista de listas (que são permutações da lista original).
def permutacoes(lista):
	if len(lista) == 1: # caso base.
		return [lista]
	primeiro = lista[0]
	resto = lista[1:]
	resultado = []
	for perm in permutacoes(resto):
		for i in range (len(perm) +1):
			resultado = resultado + [ perm[:i] + [primeiro] + perm[i:] ]
	return resultado
# fim da função
x = input("Digite a lista: ")
print(permutacoes(x))

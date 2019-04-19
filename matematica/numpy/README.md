# Numpy  

Numpy é uma biblioteca para computação científica. 
Ela provê objetos arrays multidimensionais de alta performance e ferramentas para trabalhar com esses arrays.  

## Arrays  

- Arrays no numpy são grids de valores;  
- Todos do mesmo tipo.  
- São indexados por tuplas com valores não negativos.  
- O shape de um array é uma tupla de inteiros que indica o tamanho do array ao longo de cada dimensão.  
- É possível iniciar um array numpy a partir de uma lista aninhada.  
   
```py
import numpy as np

a = np.array([1,3,5,7])

print(a)       # [1 3 5 7]
print(type(a)) # <class 'numpy.ndarray'>
print(a.shape) # (4,) # Acho que não faz muito sentido usar o 'shape' em matriz de uma dimensão.
print(a[1])    # 3

a[1] = 25      # Reatribuindo valor.
print(a[1])    # 25

array_2_por_3 = np.array([[1,2,3], [4,5,6]])

print(array_2_por_3)         # [[1 2 3] [4 5 6]]    
print(array_2_por_3.shape)   # (2,3) # Array 2x3
print(array_2_por_3[0,2])    # 3
```   
  
 ```py
 # Cria um array 3x2.
# Preenche o array com zeros.
a = np.zeros((3,2))

print(a)  # [ [0. 0.] [0. 0.] [0. 0.] ]

# Imprime primeiro array, segundo elemento.
print( a[0][1] ) # 0.0

# Index error, pois não existe a posição requerida.
#print(a[0][2])
 ```  
   
 ```py
# Cria um array 2x2.
# Preenche o array com 1.
b = np.ones((2,2))

print(b)  # [ [1. 1.] [1. 1.] ]
 ```  
  
```py
# Cria um array 2x2.
# Preenche o array com os valores que quisermos.
# No caso todos os elementos do array terão o valor 5.
c = np.full( (2,2), 5 )

print(c) # [ [5 5] [5 5] ]
```  
  
```py
# Cria uma matriz identidade de ordem 3.
matriz_identidade = np.eye(3)

print(matriz_identidade)       # [ [1. 0. 0.] [0. 1. 0.] [0. 0. 1.] ]

print(matriz_identidade.shape) # (3,3)
```  
  
 ```py
# Criando uma matriz 3x2 com valores aleatórios.
matriz_aleatoria = np.random.random((3,2))
print(matriz_aleatoria)  # [ [0.70394434 0.24837714] [0.1890589  0.30119754] [0.59894015 0.70585995] ]
 ```  
   
> Estudar mais coisas em [cs231n.github.io](http://cs231n.github.io/python-numpy-tutorial/#python).  
  
  
## Referências  

[cs231n.github.io](http://cs231n.github.io/python-numpy-tutorial/#python)  
[numpy.org](https://www.numpy.org)  


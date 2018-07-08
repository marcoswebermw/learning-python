# Unittest
  
É um framework de testes unitários em Python. Já vem na biblioteca padrão da linguagem.  

Basicamente seu funcionamento começa criando uma classe de testes para uma classe a ser testada. Essa classe de teste deve derivar de `TestCase`. Dentro dela existirão métodos começados com `test_`. E finalmente, devemos rodar os testes com o método `main()` do unittest framework.  

## Lista de Alguns Métodos Assert
  
* assertEqual  
* assertLess  
* assertLessEqual  
* assertTrue  
* assertFalse  
* assertRaises  
  
## Exemplo
  
```py
from unittest import TestCase, main

def soma(x, y):
    return x + y

class Testes(TestCase):
    def test_soma(self):
        self.assertEqual(soma(6,4), 10)

if '__main__' == __name__:
    main()
```

## Referências
  
[Python Docs](https://docs.python.org/3/library/unittest.html)  
[PythonTesting](http://pythontesting.net/framework/unittest/unittest-introduction/)
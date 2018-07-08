# UnitTest na linha de comando
  
O `unittest` roda dentro dos scripts python, mas também pode ser executado pela linha de comando. O que é bem flexível caso  queiramos executar os testes em conjunto com outros scripts externos etc.   

É possível executar testes passando módulos, classes, métodos e inclusive o caminho para arquivos. Veja abaixo exemplos tirados da documentação:  

```py
python -m unittest test_module1 test_module2
python -m unittest test_module.TestClass
python -m unittest test_module.TestClass.test_method
python -m unittest tests/test_something.py

# Modo verboso
python -m unittest -v test_module

# Obter Ajuda
python -m unittest -h

# Test Discovery - Sem argumentos
python -m unittest
```

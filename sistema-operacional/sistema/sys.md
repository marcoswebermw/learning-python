## Sys
  
O módulo `sys` é responsável por tratar sobre o ambiente de execução de um programa.
  
Com ele é possível finalizar um processo e descobrir informações a respeito dos parâmetros passados ao programa pela linha de comando e, também informações do PATH do sistema. Além disso, ele pode encaminhar erros para a saída de erros.
  
O nome do programa é sempre o primeiro parâmetro.
  
### Exemplo
  
```py
import sys

print("Nome do programa: {}".format(sys.argv[0]))
print("Parâmetros passados: {}".format(sys.argv))
print("Números de parâmetros passados: {}".format( len(sys.argv) ))

# Imprimindo o PATH do sistema.
print("-" * 50)
print("\nPath do sistema:\n")

path_sistema = sys.path
for caminho in sys.path:
    print("* {}".format(caminho) )

print("-" * 50)

# Imprimindo números e finalizando o processo do programa.
for x in range(1,5):
    if (x == 3):
        print("Saindo do programa...")
        sys.exit()    
    print(x)

print("Essa linha não é exibida porque o sys.exit() finalizou o meu processo.")
```
  
### Referências
  
* [Python Docs](https://docs.python.org/3/library/sys.html)  

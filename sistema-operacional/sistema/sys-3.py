# Exemplo de programa na linha de comando.
import sys

def main():
    if len(sys.argv) != 4 or '--help' in sys.argv[1:]:
        print('Uso do programa: programa <arg1> <arg2> <arg3>', file=sys.stderr)
        # Código de saída indicando que o programa teve erro.
        # O padrão é sys.exit(0) que indica que tudo ocorreu normalmente.
        sys.exit(1) 
    print("Se estou sendo exibido, os parâmetros foram passados corretamente.")

if __name__ == "__main__":
    main()
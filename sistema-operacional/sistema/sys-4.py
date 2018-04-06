# sys.stdin pode ser a saída de qualquer comando Unix.
# Ex.: echo "Olá Mundo!" | python esse_programa.py
import sys

for linha in sys.stdin:
    print(linha)
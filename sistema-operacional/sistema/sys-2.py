import sys

# As mensagens de erro não devem ir para saída padrão, quando possível.
print('ERRO: Mensagem qualquer.', file=sys.stderr)

try:
    arquivo = open('arquivo-inexistente.txt', 'rb')
except OSError as e:
    print(e, file=sys.stderr)
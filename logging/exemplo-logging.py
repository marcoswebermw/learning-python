import logging
logging.basicConfig(filename='calculadora.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(funcName)s => %(message)s')


def add(x, y):
  logging.debug('parametros: x={}, y={}'.format(x, y))
  return x + y

def mul(x, y):
  logging.debug('parametros: x={}, y={}'.format(x, y))
  return x * y

def sub(x, y):
  logging.debug('parametros: x={}, y={}'.format(x, y))
  return x - y

def div(x, y):
  try:
      logging.debug('parametros: x={}, y={}'.format(x, y))
      return x / y
  except ZeroDivisionError:
      logging.exception('parametros: x={}, y={}'.format(x, y))
      print("Impossível dividir por 0!")


if __name__ == '__main__':
  print(add(8, 4))
  print(mul(8, 4))
  print(div(8, 4))
  print(div(8, 0))
  print(sub(8, 4))

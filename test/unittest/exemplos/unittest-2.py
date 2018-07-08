# Adicionando testes a uma suíte de testes.
import unittest

def soma(x, y):
    return x + y

class Testes(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(6,4), 10)


def suiteDeTestes():
    suite = unittest.TestSuite()
    suite.addTest(Testes('test_soma'))
    return suite

if __name__ == '__main__':
    testador = unittest.TextTestRunner()
    testador.run(suiteDeTestes())
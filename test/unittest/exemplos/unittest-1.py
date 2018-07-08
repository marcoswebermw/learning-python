from unittest import TestCase, main

def soma(x, y):
    return x + y

class Testes(TestCase):
    def test_soma(self):
        self.assertEqual(soma(6,4), 10)

if '__main__' == __name__:
    main()


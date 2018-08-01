from PyQt5.QtWidgets import QApplication, QPushButton

def slot():
    print('Olá Mundo')

app = QApplication([])
botao = QPushButton('Clique Aqui!')

botao.clicked.connect(slot)
botao.clicked.connect(app.quit)

botao.show()

app.exec_()

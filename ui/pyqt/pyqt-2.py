# Exemplo usando tela gerada pelo QtDesigner.
from PyQt5.QtWidgets import QApplication
# Import para usar arquivo ´tela.ui´ gerado pelo QtDesigner.
from PyQt5 import uic

def slot():
    print('Olá Mundo')

app = QApplication([])
ui = uic.loadUi('tela.ui')

ui.botao.clicked.connect(slot)
ui.botao.clicked.connect(app.quit)

ui.show()

app.exec_()

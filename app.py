import sys
from design import *
#Ui_MainWindow(object)
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class Redimensionador(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnEscolherArquivo.clicked.connect(self.abrir_imagem)

    
    def abrir_imagem(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralWidget,
            'Abrir imagem',
            r'C:\Users\adoma',
            #options=QFileDialog.disconnectNotify
            
        )

        imagem = str(imagem).replace("/", "\\")
        self.inputAbrirArquivo.setText(rf"{imagem}")


    
if __name__ == "__main__":
    qt = QApplication(sys.argv)
    red = Redimensionador()
    red.show()
    qt.exec()
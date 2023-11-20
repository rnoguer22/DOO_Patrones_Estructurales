import sys
from lanzador import Lanzador
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':

    app = QApplication(sys.argv)
    lanzador = Lanzador()
    lanzador.lanzar()
    sys.exit(app.exec_())
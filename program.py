import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.run2)
        self.fl = False

    def run(self):
        self.fl = True

    def run2(self):
        self.fl = False

    def paintEvent(self, event):
        if self.fl:
            self.qp = QPainter()
            self.qp.begin(self)
            self.drawFlag()
            self.qp.end()

    def drawFlag(self):
        self.qp.setBrush(QColor(255, 255, 0))
        self.qp.drawEllipse(100, 100, randint(200, 250), randint(200, 250))


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

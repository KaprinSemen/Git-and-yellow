import sys

from random import randrange

from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5.QtWidgets import QWidget, QApplication

class MyWidget(QWidget):
    def __init__(self):
        uic.loadUi("UI.ui", self)
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 200, 800, 800)
        self.pushButton.clicked.connect(self.paintEvent)

    def draww(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.drawCircle(qp)
            qp.end()
    def drawCircle(self, qp):
        qp.setBrush(QColor(255, 55, 0))
        if self.stats == 1:
            qp.drawEllipse(randrange(1, 255), randrange(1, 255), randrange(1, 255), randrange(1, 255))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    wd = MyWidget()
    wd.show()
    sys.exit(app.exec())
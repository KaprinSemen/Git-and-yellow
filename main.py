import sys

from random import randrange

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.setGeometry(600, 200, 800, 800)
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.drawCircle(qp)
            qp.end()


    def drawCircle(self, qp):
         for i in range(3):
            qp.setBrush(QColor(255, 255, 0))
            size = randrange(1, 400)

            qp.drawEllipse(randrange(1, 600), randrange(1, 600), size, size)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wd = MyWidget()
    wd.show()
    sys.exit(app.exec())

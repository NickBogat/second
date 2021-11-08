import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QColor, QPainter, QPolygon
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.figure_x = 0
        self.figure_y = 0
        self.width = randint(1, 160)

    def initUI(self):
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Круги')

    def paintEvent(self, event):
        br = QColor(255, 255, 0)
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setBrush(br)
        painter.drawEllipse(self.figure_x, self.figure_y, self.width, self.width)

    def run(self):
        self.width = randint(1, 160)
        x, y = randint(self.width, 600 - self.width), randint(self.width, 600 - self.width)
        self.figure_x = x
        self.figure_y = y
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
import sys
from PyQt6 import uic
import random
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QColor, QPainter


class Circles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.qp = QPainter()
        self.flag = False
        self.draw_btn.clicked.connect(self.draw1)

    def draw1(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        try:
            r = random.randint(20, 100)
            x, y = random.randint(20, 800), random.randint(20, 600)
            self.qp.setBrush(QColor("yellow"))
            self.qp.drawEllipse(QPointF(x, y), r, r)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())
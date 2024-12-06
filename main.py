import sys
import random
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QColor, QPainter
from UI import Ui_Circles

class Circles(QMainWindow, Ui_Circles):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
            c = [random.randint(0, 255) for _ in range(3)]
            r = random.randint(20, 100)
            x, y = random.randint(20, 800), random.randint(20, 600)
            self.qp.setBrush(QColor(*c))
            self.qp.drawEllipse(QPointF(x, y), r, r)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())
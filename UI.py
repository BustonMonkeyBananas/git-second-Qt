# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Circles(object):
    def setupUi(self, Circles):
        Circles.setObjectName("Circles")
        Circles.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=Circles)
        self.centralwidget.setObjectName("centralwidget")
        self.draw_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.draw_btn.setGeometry(QtCore.QRect(340, 250, 111, 28))
        self.draw_btn.setObjectName("draw_btn")
        Circles.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Circles)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        Circles.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Circles)
        self.statusbar.setObjectName("statusbar")
        Circles.setStatusBar(self.statusbar)

        self.retranslateUi(Circles)
        QtCore.QMetaObject.connectSlotsByName(Circles)

    def retranslateUi(self, Circles):
        _translate = QtCore.QCoreApplication.translate
        Circles.setWindowTitle(_translate("Circles", "Circles"))
        self.draw_btn.setText(_translate("Circles", "Нарисовать круг"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Circles = QtWidgets.QMainWindow()
    ui = Ui_Circles()
    ui.setupUi(Circles)
    Circles.show()
    sys.exit(app.exec())
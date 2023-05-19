from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.centralWidget().setLayout(QtWidgets.QVBoxLayout())


        self.dsbGR = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.dsbGR.setDecimals(3)
        self.dsbGR.setSingleStep(0.1)
        self.dsbGR.setProperty("value", 3.0)
        self.dsbGR.setObjectName("dsbGR")
        self.dsbGR.valueChanged.connect(self.onValueChanged)
        self.centralWidget().layout().addWidget(self.dsbGR)

    def onValueChanged(self, val):
        print(val)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

import sys

from PyQt5 import QtGui, QtWidgets

from LoginWindow import Ui_Login


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.form_widget = Ui_Login(self)
        _widget = QtWidgets.QWidget()
        #_layout = QtWidgets.QGridLayout(_widget)
        #_layout.setGeometry(MainWindow.geometry(self))
        #_layout = QtWidgets.QVBoxLayout(_widget)
        #_layout.addWidget(self.form_widget)
        self.setCentralWidget(self.form_widget)

def main():
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()

if __name__ == '__main__':
    sys.exit(main()) 
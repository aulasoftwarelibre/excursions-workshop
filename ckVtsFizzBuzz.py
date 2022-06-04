from select import select
import sys

from matplotlib.pyplot import title
import ckFizzBuzzController as ctrl

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtGui import QIntValidator


class FizzBuzzDlg(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.title = QLabel('Introduce un número:')
        self.titleEdit = QLineEdit()
        self.titleEdit.setValidator(QIntValidator(0, 100000000, self))
        self.selectButton = QPushButton("Send")
        self.selectButton.clicked.connect(self.checkNumber)

        self.number = QLabel('Introduce un número:')
        self.number.setText("")

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.title, 0, 0)
        grid.addWidget(self.titleEdit, 0, 1)
        grid.addWidget(self.selectButton, 0, 2)
        grid.addWidget(self.number, 1, 1)

        self.setLayout(grid)

        self.setGeometry(500, 500, 350, 100)
        self.setWindowTitle('Review')
        self.show()

    def checkNumber(self):
        ctrl.eventFizzBuzz(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = FizzBuzzDlg()
    sys.exit(app.exec_())

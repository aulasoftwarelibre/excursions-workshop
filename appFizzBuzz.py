import sys
from PyQt5 import QtWidgets
import ckVtsFizzBuzz as vts

app = QtWidgets.QApplication(sys.argv)  # Crea una aplicacion
form = vts.FizzBuzzDlg()  # Crea una instancia del formulario
sys.exit(app.exec_())  # Se inicia la aplicacion y se espera eventos
1
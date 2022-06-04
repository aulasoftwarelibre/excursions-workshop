from pathlib import Path
from PyQt5.QtWidgets import (QFileDialog)
import sys


def fizzBuzz(self):
    if int(self.titleEdit.text()) % 5 == 0 and int(self.titleEdit.text()) % 3 == 0:
        return "FizzBuzz"
    elif int(self.titleEdit.text()) % 3 == 0:
        return "Fizz"
    elif int(self.titleEdit.text()) % 5 == 0:
        return "Buzz"
    return self.titleEdit.text()

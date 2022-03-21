#!/usr/bin/pyton3

import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Button:
    def __init__(self, text, res):
        self.b = QPushButton(str(text))
        self.text = text
        self.res = res
        self.b.clicked.connect(lambda: self.handleInput(self.text))

    def handleInput(self, v):
        current = self.res.text()
        if v == '=':
            equals = eval(self.res.text())
            self.res.setText(str(equals))

        elif v == 'AC':
            self.res.setText('')

        elif v == '±':
            if current[0] == '-':
                newText = str(float(current) * -1)
            else:
                newText = '-' + current
            self.res.setText(newText)

        elif v == '%':
            newText = float(current) / 100
            self.res.setText(str(newText))


        else:
            newResult = current + str(v)
            self.res.setText(newResult)


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.createApp()

    def createApp(self):
        grid = QGridLayout()
        input = QLabel()
        # grid.addWidget(widget, row place, column place, how many rows it takes, how many columns it takes)

        buttons = ['AC', '±', '%', '÷',
                   7, 8, 9, '×',
                   4, 5, 6, '-',
                   1, 2, 3, '+',
                   0, '.', '=']

        grid.addWidget(input, 0, 0, 1, 4)
        row = 1
        column = 0
        for button in buttons:
            if column > 3:
                column = 0
                row += 1

            buttonObj = Button(button, input)

            if button == 0:
                grid.addWidget(buttonObj.b, row, column, 1, 2)
                column += 1
            else:
                grid.addWidget(buttonObj.b, row, column, 1, 1)

            column += 1

        self.setLayout(grid)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec())

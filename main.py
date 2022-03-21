#!/usr/bin/pyton3

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.createApp()

    def createApp(self):
        grid = QGridLayout()
        # grid.addWidget(widget, row place, column place, how many rows it takes, how many columns it takes)

        buttons = ['AC', '±', '%', '÷',
                   7, 8, 9, '×',
                   4, 5, 6, '-',
                   1, 2, 3, '+',
                   0, '.', '=']

        row =0
        column = 0
        for button in buttons:
            if column > 3:
                column = 0
                row += 1

            if(button == 0):
                grid.addWidget(QPushButton(str(button)), row, column, 1, 2)
                column+=1
            else:
                grid.addWidget(QPushButton(str(button)), row, column, 1, 1)
            column += 1


        self.setLayout(grid)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec())

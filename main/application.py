# !/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QGridLayout, QApplication,
                             QPushButton)
from python_simple_app.model.spending import Spending


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        name = QLabel('Name')
        category = QLabel('Category')
        currency = QLabel('Currency')
        amount = QLabel('Amount')
        date = QLabel('Date')
        username = QLabel('Username')

        # Add field on form
        name_edit = QLineEdit()
        category_edit = QLineEdit()
        currency_edit = QLineEdit()
        amount_edit = QLineEdit()
        date_edit = QLineEdit()
        username_edit = QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(name, 1, 0)
        grid.addWidget(name_edit, 1, 1)

        grid.addWidget(category, 1, 2)
        grid.addWidget(category_edit, 1, 3)

        grid.addWidget(amount, 2, 0)
        grid.addWidget(amount_edit, 2, 1)

        grid.addWidget(currency, 2, 2)
        grid.addWidget(currency_edit, 2, 3)

        grid.addWidget(date, 3, 0)
        grid.addWidget(date_edit, 3, 1)

        grid.addWidget(username, 3, 2)
        grid.addWidget(username_edit, 3, 3)

        # Add buttons on form
        btn1 = QPushButton("Ok", self)
        btn2 = QPushButton("Cancel", self)
        grid.addWidget(btn1, 4,0)
        grid.addWidget(btn2, 4,1)

        btn1.clicked.connect(self.show_dialog)
        btn2.clicked.connect(self.button_clicked)

        self.setLayout(grid)
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Add Form')
        self.show()

    def button_clicked(self):
        pass

    def show_dialog(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

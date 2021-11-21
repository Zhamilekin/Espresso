import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
import sqlite3

class Espresso(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Эспрессо')

        connection = sqlite3.connect("coffee.sqlite")
        cur = connection.cursor()
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 120)
        self.tableWidget.setColumnWidth(2, 140)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(5, 60)
        self.tableWidget.setColumnWidth(6, 130)
        self.tableWidget.setRowCount(0)
        result = cur.execute("SELECT * from Coffee")
        self.tableWidget.setRowCount(10)
        tablerow = 0
        for row in result:
            print(list(row))
            self.tableWidget.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(tablerow, 1, QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tablerow, 4, QTableWidgetItem(row[4]))
            self.tableWidget.setItem(tablerow, 5, QTableWidgetItem(str(row[5])))
            self.tableWidget.setItem(tablerow, 6, QTableWidgetItem(str(row[6])))

            tablerow += 1
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Espresso()
    ex.show()
    sys.exit(app.exec_())
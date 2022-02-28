import sqlite3
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic, QtWidgets


class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffee (1).sqlite")
        self.cur = self.con.cursor()
        query = 'SELECT * FROM all_coffee'
        result = self.cur.execute(query).fetchall()
        # self.tableWidget.setRowCount(len(result))
        # print(len(result))
        # self.tw.setColumnCount(3)
        for i, row in enumerate(result):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                print(j, elem)
                self.tableWidget.setItem(
                    i, j, QtWidgets.QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Form()
    win.show()
    sys.exit(app.exec_())
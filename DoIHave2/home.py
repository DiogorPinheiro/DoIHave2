from unit1 import Ui_MainWindow
import insertWin

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QTableWidgetItem, QMessageBox
import sqlite3

# ------------------ SQL Connection-----------
conexao = sqlite3.connect('table.db')
con = conexao.cursor()
con.execute(
    'CREATE TABLE IF NOT EXISTS base (Author TEXT, Title TEXT, Year INTEGER) ')
# --------------------------------------------


class main(QMainWindow, Ui_MainWindow):  # Main Window
    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        self.setFixedSize(803, 570)     # Prevent window resize
        self.setupUi(self)
        self.database()     # Load Database
        self.initUi()

    def database(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        conexao = sqlite3.connect('table.db')
        # Select all elements from database
        # For some reason it actually orders by author
        content = 'SELECT * from base ORDER BY Title ASC'
        conexion = conexao.execute(content)

        for r_index, r_data in enumerate(conexion):     # Rows
            self.tableWidget.insertRow(r_index)
            for c_index, c_data in enumerate(r_data):   # Columns
                self.tableWidget.setItem(
                    r_index, c_index, QTableWidgetItem(str(c_data)))

        conexao.close()  # close sqlite conexion
        self.label_3.setText('Total Items : '+str(self.tableWidget.rowCount()))
        return

    def initUi(self):
        self.show()
        self.pushButton.clicked.connect(self.Show_Add_Dialog)   # Add
        self.pushButton_3.clicked.connect(self.Deldata)
        # self.pushButton_2.clicked.connect(self.procura)    # Delete

    def Show_Add_Dialog(self):      # Show Insert Window
        self.adding = insertWin()
        self.adding.pushButton.clicked.connect(self.add_Data)
        self.adding.exec_()

    def add_Data(self):
        title = self.adding.lineEdit.text()
        author = self.adding.lineEdit_2.text()
        year = self.adding.lineEdit_3.text()
        try:
            con.execute(
                'INSERT INTO base (Author,Title,Year) VALUES (?,?,?)', (author, title, year))
            conexao.commit()
            self.database()
        except Exception as error:
            print(error)

    def Deldata(self):  # Delete data from selected row
        content = 'SELECT * FROM base'
        conexion = conexao.execute(content)
        for r in enumerate(conexion):
            if r[0] == self.tableWidget.currentRow():  # Find selected row
                dados = r[1]  # Get data from selected row
                title = dados[0]
                author = dados[1]
                year = dados[2]
                conexao.execute(
                    'DELETE from base where Author=? AND Title=? AND Year=?', (author, title, year))
                conexao.commit()
                self.database()

    # def procura(self):
     #   conexao = sqlite3.connect('table.db')
      #  procura = self.adding.lineEdit.text()
       # content = 'SELECT * from base where Title='+str(procura) + \
        #    'OR Author='+str(procura)      # Select all elements from database
        #conexion = conexao.execute(content)

        # for r_index, r_data in enumerate(conexion):     # Rows
         #   self.tableWidget.insertRow(r_index)
          #  for c_index, c_data in enumerate(r_data):   # Columns
           #     self.tableWidget.setItem(
            #        r_index, c_index, QTableWidgetItem(str(c_data)))

        # conexao.close()  # c
        # return


class insertWin(QDialog, insertWin.Ui_Dialog):   # Add
    def __init__(self, parent=None):
        super(insertWin, self).__init__(parent)
        self.setupUi(self)


app = QApplication([])
win = main()
app.exec_()

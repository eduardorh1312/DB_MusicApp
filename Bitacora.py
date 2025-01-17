from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2 as bd
from config import config

class Ui_Bitacora(object):
    def __init__(self, id):
        super(Ui_Bitacora, self).__init__()
        self.id = id

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 650)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 650))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 650))
        MainWindow.setStyleSheet("background-color: #d1d1d5")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 50, 900, 550))
        self.frame.setMinimumSize(QtCore.QSize(900, 550))
        self.frame.setMaximumSize(QtCore.QSize(900, 550))
        self.frame.setStyleSheet("background-color: #1c1d32;\n"
"border-radius: 5px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(100, 20, 100, 100))
        self.label.setMinimumSize(QtCore.QSize(225, 205))
        self.label.setMaximumSize(QtCore.QSize(225, 205))
        self.label.setStyleSheet("font: 24pt \"Times\";\n"
"color: #ffffff;\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(400, 20, 20, 20))
        self.label_2.setMinimumSize(QtCore.QSize(100, 100))
        self.label_2.setMaximumSize(QtCore.QSize(100, 100))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("musics.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(30, 190, 841, 321))
        self.tableWidget.setStyleSheet("font: 18pt \"Times\";\n"
"color: #1b1c34;\n"
"background-color: #EDFEFB;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)


        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(389, 120, 120, 120))
        self.label_8.setMinimumSize(QtCore.QSize(210, 50))
        self.label_8.setMaximumSize(QtCore.QSize(210, 50))
        self.label_8.setStyleSheet("font: 22pt \"Times\";\n"
"color: #ffffff;\n"
"")
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
 # ------------------------- termina el gui -----------------------------------------
 # Aqui empieza lo bonito  
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow",""))
        self.label_8.setText(_translate("MainWindow", "Bitácora"))
        self.populateTable()

    def populateTable(self):
    #clear the table
        self.tableWidget.setRowCount(0)
        readbd = None
        params =config()
        readbd = bd.connect(**params)
        cursor = readbd.cursor()
        query = """  SELECT username, typeofmodification, tablemodified, CAST(itemmodified AS TEXT), newData,
                    CAST(datemodified AS TEXT) FROM logbook """
        cursor.execute(query)
        record = cursor.fetchall()
        if(len(record)!= 0):
            self.tableWidget.setColumnCount(len(record[0]))
            for i in range(len(record)):
                self.tableWidget.insertRow(i)
                for j in range(len(record[0])):
                    self.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(record[i][j]))

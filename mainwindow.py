# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QFileDialog, QMessageBox
from main import make_pdf, selectFolder
import os

class Ui_MainWindow(object):
        def __init__(self):
                self.imgdir = ""

        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(534, 415)
                MainWindow.setStyleSheet("background-color: rgb(115, 210, 22);")

                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")

                self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit.setGeometry(QtCore.QRect(240, 70, 271, 25))
                self.lineEdit.setStyleSheet("background-color: white")
                self.lineEdit.setObjectName("lineEdit")

                self.convert_btn = QtWidgets.QPushButton(self.centralwidget)
                self.convert_btn.setGeometry(QtCore.QRect(280, 330, 141, 51))
                self.convert_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border-radius:10")
                self.convert_btn.setObjectName("convert_btn")
                self.convert_btn.clicked.connect(self.convert)
        
                self.selectFolder_btn = QtWidgets.QPushButton(self.centralwidget)
                self.selectFolder_btn.setGeometry(QtCore.QRect(90, 330, 141, 51))
                self.selectFolder_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border-radius:10")
                self.convert_btn.setObjectName("selectfolder_btn")
                self.selectFolder_btn.clicked.connect(self.openFolder)

                self.listWidget = QtWidgets.QListWidget(self.centralwidget)
                self.listWidget.setGeometry(QtCore.QRect(140, 110, 256, 192))
                font = QtGui.QFont()
                font.setPointSize(13)
                self.listWidget.setFont(font)
                self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.listWidget.setObjectName("listWidget")

                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(10, 20, 211, 17))
                font = QtGui.QFont()
                font.setPointSize(15)
                font.setBold(True)
                font.setWeight(75)
                self.label.setFont(font)
                self.label.setStyleSheet("color: rgb(255,255,255);\n""")
                self.label.setObjectName("label")
                MainWindow.setCentralWidget(self.centralwidget)

                self.saida_label = QtWidgets.QLabel(self.centralwidget)
                self.saida_label.setGeometry(QtCore.QRect(10, 70, 220, 20))
                self.saida_label.setText('Digite o nome da saída')
                font = QtGui.QFont()
                font.setPointSize(15)
                font.setBold(True)
                font.setWeight(75)
                self.saida_label.setFont(font)
                self.saida_label.setStyleSheet("color: rgb(255,255,255);\n""")

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "IMG to PDF convertor"))
                MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))
                self.convert_btn.setText(_translate("MainWindow", "Converter para PDF"))
                self.selectFolder_btn.setText(_translate("MainWindow", "Selecionar Pasta"))
                __sortingEnabled = self.listWidget.isSortingEnabled()
                self.listWidget.setSortingEnabled(False)
                self.listWidget.setSortingEnabled(__sortingEnabled)
                self.label.setText(_translate("MainWindow", "Pasta não selecionada"))

        def openFolder(self):
                self.inputFolder = QFileDialog(directory=os.getenv("HOME"))
                self.inputFolder.setWindowTitle("Escolha uma pasta")
                self.inputFolder.setFileMode(QFileDialog.Directory)
                self.inputFolder.setAcceptMode(QFileDialog.AcceptOpen)
                self.inputFolder.ShowDirsOnly
                self.inputFolder.exec_()
        
                self.update()
        
        def update(self):
                self.imgdir = self.inputFolder.selectedFiles()[0]
                print(self.imgdir)
                self.label.setText("pasta selecionada: " + self.imgdir)
                self.label.adjustSize()
                if self.label.width()>MainWindow.width():
                        MainWindow.resize(self.label.width()+30, 415)
                
                self.listWidget.clear()
                for filename in selectFolder(self.inputFolder.selectedFiles()[0]):
                        item = QtWidgets.QListWidgetItem()
                        item.setText(filename)
                        self.listWidget.addItem(item)
 
        def convert(self):
                if self.imgdir:
                        status = make_pdf(self.imgdir, self.lineEdit.text() or 'output')
                        if status:
                                msg = QMessageBox()
                                msg.setWindowTitle("PDF Salvo")
                                msg.setText("PDF salvo com sucesso na pasta fonte")
                                msg.setIcon(QMessageBox.Information)
                                msg.exec_()
                else: 
                        msg = QMessageBox()
                        msg.setWindowTitle("Erro")
                        msg.setText("Selecione a pasta onde estão as imagens")
                        msg.setIcon(QMessageBox.Critical)
                        msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

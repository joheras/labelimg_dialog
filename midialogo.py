# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'midialogo.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(274, 223)
        # Esto hay que añadirlo para luego poder cerrar el dialogo
        self.dialog = Dialog
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 190, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 30, 67, 17))
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(150, 20, 104, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        # Aquí se conecta el botón de Ok con la funcionalidad que quieres.
        # En concreto, el método de actualizar que se define luego. 
        self.pushButton.clicked.connect(self.actualizar)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Ok"))
        self.label.setText(_translate("Dialog", "Numero:"))

    def actualizar(self):
        # Se lee el valor de la caja de texto
        x1 = int(self.plainTextEdit.toPlainText())
        # Se almacena dicho valor para poder usarlo desde el principal. 
        self.res = x1
        # Se cierra el dialogo
        self.dialog.close()

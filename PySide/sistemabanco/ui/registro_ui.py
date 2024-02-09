# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)
import iconos_rc
import ds_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.ApplicationModal)
        Dialog.resize(846, 470)
        Dialog.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"color: black;")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(340, 40, 361, 21))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 150, 141, 18))
        self.cbTipo = QComboBox(Dialog)
        self.cbTipo.addItem("")
        self.cbTipo.addItem("")
        self.cbTipo.addItem("")
        self.cbTipo.addItem("")
        self.cbTipo.setObjectName(u"cbTipo")
        self.cbTipo.setGeometry(QRect(40, 180, 311, 26))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(490, 150, 181, 18))
        self.txtDocumento = QLineEdit(Dialog)
        self.txtDocumento.setObjectName(u"txtDocumento")
        self.txtDocumento.setGeometry(QRect(490, 180, 281, 26))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(490, 250, 181, 18))
        self.txtMonto = QLineEdit(Dialog)
        self.txtMonto.setObjectName(u"txtMonto")
        self.txtMonto.setGeometry(QRect(490, 280, 281, 26))
        self.cbMotivo = QComboBox(Dialog)
        self.cbMotivo.addItem("")
        self.cbMotivo.addItem("")
        self.cbMotivo.addItem("")
        self.cbMotivo.addItem("")
        self.cbMotivo.setObjectName(u"cbMotivo")
        self.cbMotivo.setGeometry(QRect(40, 280, 311, 26))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 250, 141, 18))
        self.checkInternacional = QCheckBox(Dialog)
        self.checkInternacional.setObjectName(u"checkInternacional")
        self.checkInternacional.setGeometry(QRect(40, 350, 221, 24))
        self.checkDolares = QCheckBox(Dialog)
        self.checkDolares.setObjectName(u"checkDolares")
        self.checkDolares.setGeometry(QRect(260, 350, 81, 24))
        self.btnRegistrar = QPushButton(Dialog)
        self.btnRegistrar.setObjectName(u"btnRegistrar")
        self.btnRegistrar.setGeometry(QRect(490, 340, 261, 41))
        self.btnRegistrar.setStyleSheet(u"background-color: rgb(255, 190, 111);")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 30, 91, 81))
        self.label.setPixmap(QPixmap(u":/dd/banco.png"))
        self.label.setScaledContents(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Registrar Transacciones", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Registro de Transferencias</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Tipo de Documento", None))
        self.cbTipo.setItemText(0, QCoreApplication.translate("Dialog", u"--- Seleccione una opcion", None))
        self.cbTipo.setItemText(1, QCoreApplication.translate("Dialog", u"DNI - Documento nacional de identidad", None))
        self.cbTipo.setItemText(2, QCoreApplication.translate("Dialog", u"PSS - Pasaporte", None))
        self.cbTipo.setItemText(3, QCoreApplication.translate("Dialog", u"VISA", None))

        self.label_4.setText(QCoreApplication.translate("Dialog", u"Numero de Documento", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Monto", None))
        self.txtMonto.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.cbMotivo.setItemText(0, QCoreApplication.translate("Dialog", u"--- Seleccione una opcion", None))
        self.cbMotivo.setItemText(1, QCoreApplication.translate("Dialog", u"Honorarios/Servicios tecnicos", None))
        self.cbMotivo.setItemText(2, QCoreApplication.translate("Dialog", u"Remesas/Giros", None))
        self.cbMotivo.setItemText(3, QCoreApplication.translate("Dialog", u"Donaciones", None))

        self.label_6.setText(QCoreApplication.translate("Dialog", u"Motivo del giro", None))
        self.checkInternacional.setText(QCoreApplication.translate("Dialog", u"Transferencia internacional", None))
        self.checkDolares.setText(QCoreApplication.translate("Dialog", u"Dolares", None))
        self.btnRegistrar.setText(QCoreApplication.translate("Dialog", u"Registrar", None))
        self.label.setText("")
    # retranslateUi


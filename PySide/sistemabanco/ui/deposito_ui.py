# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deposito.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QDialog, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import iconos_rc
import ds_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.ApplicationModal)
        Dialog.resize(846, 607)
        Dialog.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"color: black;")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(330, 50, 181, 41))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 150, 141, 18))
        self.cbTipo = QComboBox(Dialog)
        self.cbTipo.addItem("")
        self.cbTipo.addItem("")
        self.cbTipo.addItem("")
        self.cbTipo.addItem("")
        self.cbTipo.setObjectName(u"cbTipo")
        self.cbTipo.setGeometry(QRect(40, 180, 281, 26))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(470, 150, 181, 18))
        self.txtDocumento = QLineEdit(Dialog)
        self.txtDocumento.setObjectName(u"txtDocumento")
        self.txtDocumento.setGeometry(QRect(470, 180, 281, 26))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(470, 460, 181, 18))
        self.txtMonto = QLineEdit(Dialog)
        self.txtMonto.setObjectName(u"txtMonto")
        self.txtMonto.setGeometry(QRect(470, 490, 281, 26))
        self.cbMotivo = QComboBox(Dialog)
        self.cbMotivo.addItem("")
        self.cbMotivo.addItem("")
        self.cbMotivo.addItem("")
        self.cbMotivo.addItem("")
        self.cbMotivo.setObjectName(u"cbMotivo")
        self.cbMotivo.setGeometry(QRect(40, 490, 311, 26))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 460, 141, 18))
        self.checkTerminos = QCheckBox(Dialog)
        self.checkTerminos.setObjectName(u"checkTerminos")
        self.checkTerminos.setGeometry(QRect(40, 540, 311, 24))
        self.btnRegistrar = QPushButton(Dialog)
        self.btnRegistrar.setObjectName(u"btnRegistrar")
        self.btnRegistrar.setGeometry(QRect(470, 530, 281, 41))
        self.btnRegistrar.setStyleSheet(u"background-color: rgb(255, 190, 111);")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 30, 91, 81))
        self.label.setPixmap(QPixmap(u":/dd/banco.png"))
        self.label.setScaledContents(True)
        self.txtPrimerNombre = QLineEdit(Dialog)
        self.txtPrimerNombre.setObjectName(u"txtPrimerNombre")
        self.txtPrimerNombre.setGeometry(QRect(40, 260, 281, 26))
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 230, 181, 18))
        self.txtSegundoNombre = QLineEdit(Dialog)
        self.txtSegundoNombre.setObjectName(u"txtSegundoNombre")
        self.txtSegundoNombre.setGeometry(QRect(470, 260, 281, 26))
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(470, 230, 181, 18))
        self.txtPrimerApellido = QLineEdit(Dialog)
        self.txtPrimerApellido.setObjectName(u"txtPrimerApellido")
        self.txtPrimerApellido.setGeometry(QRect(40, 340, 281, 26))
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 310, 181, 18))
        self.txtSegundoApellido = QLineEdit(Dialog)
        self.txtSegundoApellido.setObjectName(u"txtSegundoApellido")
        self.txtSegundoApellido.setGeometry(QRect(470, 340, 281, 26))
        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(470, 310, 181, 18))
        self.cbSexo = QComboBox(Dialog)
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.cbSexo.setObjectName(u"cbSexo")
        self.cbSexo.setGeometry(QRect(40, 410, 121, 26))
        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(40, 380, 81, 18))
        self.txtFecha = QDateEdit(Dialog)
        self.txtFecha.setObjectName(u"txtFecha")
        self.txtFecha.setGeometry(QRect(180, 410, 141, 27))
        self.txtFecha.setCalendarPopup(True)
        self.label_12 = QLabel(Dialog)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(180, 380, 161, 18))
        self.cbLugar = QComboBox(Dialog)
        self.cbLugar.addItem("")
        self.cbLugar.setObjectName(u"cbLugar")
        self.cbLugar.setGeometry(QRect(470, 410, 281, 26))
        self.label_13 = QLabel(Dialog)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(470, 380, 151, 18))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Registrar Transacciones", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Deposito Bancario</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Tipo de Documento", None))
        self.cbTipo.setItemText(0, QCoreApplication.translate("Dialog", u"--- Seleccione una opcion", None))
        self.cbTipo.setItemText(1, QCoreApplication.translate("Dialog", u"DNI - Documento nacional de identidad", None))
        self.cbTipo.setItemText(2, QCoreApplication.translate("Dialog", u"PSS - Pasaporte", None))
        self.cbTipo.setItemText(3, QCoreApplication.translate("Dialog", u"VISA", None))

        self.label_4.setText(QCoreApplication.translate("Dialog", u"Numero de Documento", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Monto en dolares", None))
        self.txtMonto.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.cbMotivo.setItemText(0, QCoreApplication.translate("Dialog", u"--- Seleccione una opcion", None))
        self.cbMotivo.setItemText(1, QCoreApplication.translate("Dialog", u"Honorarios/Servicios tecnicos", None))
        self.cbMotivo.setItemText(2, QCoreApplication.translate("Dialog", u"Remesas/Giros", None))
        self.cbMotivo.setItemText(3, QCoreApplication.translate("Dialog", u"Donaciones", None))

        self.label_6.setText(QCoreApplication.translate("Dialog", u"Motivo del giro", None))
        self.checkTerminos.setText(QCoreApplication.translate("Dialog", u"Cliente acepta terminos y condiciones", None))
        self.btnRegistrar.setText(QCoreApplication.translate("Dialog", u"Registrar", None))
        self.label.setText("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Primer Nombre", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Segundo Nombre", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Primer Apellido", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Segundo Apellido", None))
        self.cbSexo.setItemText(0, QCoreApplication.translate("Dialog", u"--- Seleccione una opcion", None))
        self.cbSexo.setItemText(1, QCoreApplication.translate("Dialog", u"Mujer", None))
        self.cbSexo.setItemText(2, QCoreApplication.translate("Dialog", u"Hombre", None))
        self.cbSexo.setItemText(3, QCoreApplication.translate("Dialog", u"Otro", None))

        self.label_11.setText(QCoreApplication.translate("Dialog", u"Sexo", None))
        self.txtFecha.setDisplayFormat(QCoreApplication.translate("Dialog", u"dd/mm/yyyy", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Fecha de nacimiento", None))
        self.cbLugar.setItemText(0, QCoreApplication.translate("Dialog", u"--- Seleccione una opcion", None))

        self.label_13.setText(QCoreApplication.translate("Dialog", u"Ciudad de nacimiento", None))
    # retranslateUi


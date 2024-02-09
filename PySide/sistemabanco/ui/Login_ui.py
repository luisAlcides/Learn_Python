# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import icons_rc

class Ui_formLogin(object):
    def setupUi(self, formLogin):
        if not formLogin.objectName():
            formLogin.setObjectName(u"formLogin")
        formLogin.resize(546, 433)
        icon = QIcon()
        icon.addFile(u":/images/d28c7f7b/banco.png", QSize(), QIcon.Normal, QIcon.Off)
        formLogin.setWindowIcon(icon)
        formLogin.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.label = QLabel(formLogin)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 20, 131, 111))
        self.label.setPixmap(QPixmap(u":/icons/banco.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(formLogin)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 170, 181, 16))
        font = QFont()
        font.setFamilies([u"Monospace"])
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_3 = QLabel(formLogin)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 220, 61, 16))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_3.setFont(font1)
        self.label_4 = QLabel(formLogin)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 270, 81, 16))
        self.label_4.setFont(font1)
        self.txtUsuario = QLineEdit(formLogin)
        self.txtUsuario.setObjectName(u"txtUsuario")
        self.txtUsuario.setGeometry(QRect(170, 212, 241, 31))
        self.txtClave = QLineEdit(formLogin)
        self.txtClave.setObjectName(u"txtClave")
        self.txtClave.setGeometry(QRect(170, 262, 241, 31))
        self.txtClave.setEchoMode(QLineEdit.Password)
        self.btnAcceder = QPushButton(formLogin)
        self.btnAcceder.setObjectName(u"btnAcceder")
        self.btnAcceder.setGeometry(QRect(210, 323, 151, 31))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.btnAcceder.setFont(font2)
        self.btnAcceder.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAcceder.setStyleSheet(u"background-color: rgb(255, 190, 111);")
        self.lblMensaje = QLabel(formLogin)
        self.lblMensaje.setObjectName(u"lblMensaje")
        self.lblMensaje.setGeometry(QRect(30, 400, 491, 16))
        font3 = QFont()
        font3.setPointSize(11)
        self.lblMensaje.setFont(font3)
        self.lblMensaje.setStyleSheet(u"color: red;")

        self.retranslateUi(formLogin)

        QMetaObject.connectSlotsByName(formLogin)
    # setupUi

    def retranslateUi(self, formLogin):
        formLogin.setWindowTitle(QCoreApplication.translate("formLogin", u"Inicio de sesion", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("formLogin", u"Inicio de sesion", None))
        self.label_3.setText(QCoreApplication.translate("formLogin", u"Usuario:", None))
        self.label_4.setText(QCoreApplication.translate("formLogin", u"Password:", None))
        self.txtUsuario.setText(QCoreApplication.translate("formLogin", u"admin", None))
        self.txtUsuario.setPlaceholderText("")
        self.txtClave.setText(QCoreApplication.translate("formLogin", u"admin", None))
        self.txtClave.setPlaceholderText("")
        self.btnAcceder.setText(QCoreApplication.translate("formLogin", u"Iniciar", None))
        self.lblMensaje.setText("")
    # retranslateUi


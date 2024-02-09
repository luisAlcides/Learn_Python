# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(800, 600)
        self.actionDesarrolladores = QAction(main)
        self.actionDesarrolladores.setObjectName(u"actionDesarrolladores")
        self.btnRegistrarTransferencias = QAction(main)
        self.btnRegistrarTransferencias.setObjectName(u"btnRegistrarTransferencias")
        self.btnReportarTransferencias = QAction(main)
        self.btnReportarTransferencias.setObjectName(u"btnReportarTransferencias")
        self.btnHistorialTransferencias = QAction(main)
        self.btnHistorialTransferencias.setObjectName(u"btnHistorialTransferencias")
        self.centralwidget = QWidget(main)
        self.centralwidget.setObjectName(u"centralwidget")
        main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuCreditos = QMenu(self.menubar)
        self.menuCreditos.setObjectName(u"menuCreditos")
        main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main)
        self.statusbar.setObjectName(u"statusbar")
        main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuCreditos.menuAction())
        self.menuArchivo.addAction(self.btnRegistrarTransferencias)
        self.menuArchivo.addAction(self.btnReportarTransferencias)
        self.menuArchivo.addAction(self.btnHistorialTransferencias)
        self.menuCreditos.addAction(self.actionDesarrolladores)

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"BancoW-Transferencias", None))
        self.actionDesarrolladores.setText(QCoreApplication.translate("main", u"Desarrolladores", None))
        self.btnRegistrarTransferencias.setText(QCoreApplication.translate("main", u"Registrar Transferencias", None))
#if QT_CONFIG(shortcut)
        self.btnRegistrarTransferencias.setShortcut(QCoreApplication.translate("main", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.btnReportarTransferencias.setText(QCoreApplication.translate("main", u"Reportar Transferencias", None))
        self.btnHistorialTransferencias.setText(QCoreApplication.translate("main", u"Historial de Transferencias", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("main", u"Archivo", None))
        self.menuCreditos.setTitle(QCoreApplication.translate("main", u"Creditos", None))
    # retranslateUi


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWnd(object):
    def setupUi(self, MainWnd):
        MainWnd.setObjectName("MainWnd")
        MainWnd.resize(1020, 837)
        self.centralwidget = QtWidgets.QWidget(MainWnd)
        self.centralwidget.setObjectName("centralwidget")
        MainWnd.setCentralWidget(self.centralwidget)
        self.Menubar = QtWidgets.QMenuBar(MainWnd)
        self.Menubar.setGeometry(QtCore.QRect(0, 0, 1020, 31))
        self.Menubar.setObjectName("Menubar")
        self.menuFile = QtWidgets.QMenu(self.Menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuFileOpenSub = QtWidgets.QMenu(self.menuFile)
        self.menuFileOpenSub.setObjectName("menuFileOpenSub")
        MainWnd.setMenuBar(self.Menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWnd)
        self.statusbar.setObjectName("statusbar")
        MainWnd.setStatusBar(self.statusbar)
        self.action1_1_1 = QtWidgets.QAction(MainWnd)
        self.action1_1_1.setObjectName("action1_1_1")
        self.menuOpenRecent = QtWidgets.QAction(MainWnd)
        self.menuOpenRecent.setObjectName("menuOpenRecent")
        self.menuFileSave = QtWidgets.QAction(MainWnd)
        self.menuFileSave.setObjectName("menuFileSave")
        self.menuFileSaveAs = QtWidgets.QAction(MainWnd)
        self.menuFileSaveAs.setObjectName("menuFileSaveAs")
        self.menuFileClose = QtWidgets.QAction(MainWnd)
        self.menuFileClose.setObjectName("menuFileClose")
        self.menuFileOpenSub.addAction(self.menuOpenRecent)
        self.menuFile.addAction(self.menuFileOpenSub.menuAction())
        self.menuFile.addAction(self.menuFileSave)
        self.menuFile.addAction(self.menuFileSaveAs)
        self.menuFile.addAction(self.menuFileClose)
        self.menuFile.addSeparator()
        self.Menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWnd)
        QtCore.QMetaObject.connectSlotsByName(MainWnd)

    def retranslateUi(self, MainWnd):
        _translate = QtCore.QCoreApplication.translate
        MainWnd.setWindowTitle(_translate("MainWnd", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWnd", "File"))
        self.menuFileOpenSub.setTitle(_translate("MainWnd", "Open"))
        self.action1_1_1.setText(_translate("MainWnd", "1.1.1"))
        self.menuOpenRecent.setText(_translate("MainWnd", "Open Recent"))
        self.menuFileSave.setText(_translate("MainWnd", "Save(Ctl+S)"))
        self.menuFileSave.setShortcut(_translate("MainWnd", "Ctrl+S"))
        self.menuFileSaveAs.setText(_translate("MainWnd", "Save As(Alt+S)"))
        self.menuFileSaveAs.setShortcut(_translate("MainWnd", "Alt+S"))
        self.menuFileClose.setText(_translate("MainWnd", "Close"))


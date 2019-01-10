# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pytst\LoginDlg.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginDlg(object):
    def setupUi(self, LoginDlg):
        LoginDlg.setObjectName("LoginDlg")
        LoginDlg.resize(343, 239)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginDlg.sizePolicy().hasHeightForWidth())
        LoginDlg.setSizePolicy(sizePolicy)
        self.layoutWidget = QtWidgets.QWidget(LoginDlg)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 40, 260, 146))
        self.layoutWidget.setObjectName("layoutWidget")
        self.loginLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.loginLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.loginLayout.setContentsMargins(0, 0, 0, 0)
        self.loginLayout.setObjectName("loginLayout")
        self.LoginMain = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoginMain.sizePolicy().hasHeightForWidth())
        self.LoginMain.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LoginMain.setFont(font)
        self.LoginMain.setTextFormat(QtCore.Qt.AutoText)
        self.LoginMain.setAlignment(QtCore.Qt.AlignCenter)
        self.LoginMain.setObjectName("LoginMain")
        self.loginLayout.addWidget(self.LoginMain, 0, 0, 1, 2)
        self.Account = QtWidgets.QLabel(self.layoutWidget)
        self.Account.setObjectName("Account")
        self.loginLayout.addWidget(self.Account, 1, 0, 1, 1)
        self.AccountEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.AccountEdit.setObjectName("AccountEdit")
        self.loginLayout.addWidget(self.AccountEdit, 1, 1, 1, 1)
        self.PSW = QtWidgets.QLabel(self.layoutWidget)
        self.PSW.setObjectName("PSW")
        self.loginLayout.addWidget(self.PSW, 2, 0, 1, 1)
        self.PSWEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.PSWEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.PSWEdit.setObjectName("PSWEdit")
        self.loginLayout.addWidget(self.PSWEdit, 2, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.loginLayout.addWidget(self.buttonBox, 3, 0, 1, 2)

        self.retranslateUi(LoginDlg)
        self.buttonBox.accepted.connect(LoginDlg.accept)
        self.buttonBox.rejected.connect(LoginDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(LoginDlg)

    def retranslateUi(self, LoginDlg):
        _translate = QtCore.QCoreApplication.translate
        LoginDlg.setWindowTitle(_translate("LoginDlg", "登录"))
        self.LoginMain.setText(_translate("LoginDlg", "登录"))
        self.Account.setText(_translate("LoginDlg", "账号:  "))
        self.PSW.setText(_translate("LoginDlg", "密码:"))


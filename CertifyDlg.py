# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CertifyDlg.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CertifyDlg(object):
    def setupUi(self, CertifyDlg):
        CertifyDlg.setObjectName("CertifyDlg")
        CertifyDlg.resize(431, 381)
        CertifyDlg.setMinimumSize(QtCore.QSize(328, 250))
        self.checkBox_2 = QtWidgets.QCheckBox(CertifyDlg)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 70, 101, 23))
        self.checkBox_2.setObjectName("checkBox_2")
        self.tiplabel = QtWidgets.QLabel(CertifyDlg)
        self.tiplabel.setGeometry(QtCore.QRect(50, 320, 128, 19))
        self.tiplabel.setObjectName("tiplabel")
        self.widget = QtWidgets.QWidget(CertifyDlg)
        self.widget.setGeometry(QtCore.QRect(12, 44, 304, 224))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.certiImg = QtWidgets.QGraphicsView(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.certiImg.sizePolicy().hasHeightForWidth())
        self.certiImg.setSizePolicy(sizePolicy)
        self.certiImg.setMinimumSize(QtCore.QSize(293, 190))
        self.certiImg.setBaseSize(QtCore.QSize(293, 190))
        self.certiImg.setMouseTracking(False)
        self.certiImg.setObjectName("certiImg")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.certiImg)
        self.certiImg.raise_()

        self.retranslateUi(CertifyDlg)
        self.checkBox_2.stateChanged['int'].connect(self.tiplabel.setNum)
        QtCore.QMetaObject.connectSlotsByName(CertifyDlg)

    def retranslateUi(self, CertifyDlg):
        _translate = QtCore.QCoreApplication.translate
        CertifyDlg.setWindowTitle(_translate("CertifyDlg", "验证码"))
        self.checkBox_2.setText(_translate("CertifyDlg", "123"))
        self.tiplabel.setText(_translate("CertifyDlg", "点击图片进行选择"))


# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 10:50:53 2018

@author: rohan.ruan
"""
from CertifyDlg import Ui_CertifyDlg
from InteractionGraphicItem import InteractionGraphicItem
import sys
from PyQt5.QtCore import Qt, QPoint,QEvent
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# QApplication, QDialog, QLabel, QWidget, QLineEdit, QVBoxLayout

from Dingdong12306 import Dingdong12306


class CertDlg(QDialog, Ui_CertifyDlg):
    def __init__(self, streaming):
        super(CertDlg, self).__init__()
        self.setupUi(self)
        self.img = streaming
        self.initui()

    def initui(self):
        # show certification image
        imgscene = QGraphicsScene()
        certgraph = InteractionGraphicItem(self.img)
        imgscene.addItem(certgraph)
        self.certiImg.setScene(imgscene)


        # # img size: 293*190
        # lpos = [(30, 70), (110, 70), (180, 70), (250, 70),
        #         (30, 145), (110, 145), (180, 145), (250, 145)]
        # for i in range(0, 8):
        #     ltxt = QLabel(str(i), self)
        #     ltxt.move(lpos[i][0], lpos[i][1])
        # # tip info
        # self.tiptxt = QLabel("请输入验证答案的编号0-7(无需空格):", self)
        # self.tiptxt.move(10, 192)
        # self.layout.addWidget(self.tiptxt)
        # # input box
        # self.edit = QLineEdit(self)
        # # self.edit.setEchoMode(QLineEdit.Password)
        # self.layout.addWidget(self.edit)
        # self.setLayout(self.layout)
        self.show()

    # def input(self):
    #     return self.edit.text()
    #
    def mousePressEvent(self, event):
        # sendername = self.sender( ).objectName(self)
        # if sendername =="certimg":
        if event.buttons() == Qt.LeftButton:
            # get mouse position
            mousepos = event.pos()
            # QMessageBox.information(self, "POS", str(mousepos))
            # self.setCursor(Qt.BusyCursor)
            startpoint = QPoint(5, 41)
            dist = 72
            rank = int((mousepos.x() - startpoint.x()) / dist) + int((mousepos.y() - startpoint.y()) / dist)*4
            # QMessageBox.information(self, "POS", str(rank))
            self.tiplabel.setText(str(mousepos))
            # self.certiImg.scene().addRect(mousepos.x(),mousepos.y(),20.0,20.0)






app = QApplication(sys.argv)
dd = Dingdong12306()
dlg = CertDlg(dd.captcha())
sys.exit(app.exec_())

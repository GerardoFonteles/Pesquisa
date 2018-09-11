# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyDegua.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_pyDegua(object):
    def setupUi(self, pyDegua):
        pyDegua.setObjectName("pyDegua")
        pyDegua.resize(1158, 586)
        self.centralwidget = QtWidgets.QWidget(pyDegua)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(325, 2, 110, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 2, 110, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(330, 30, 821, 531))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(312, 0, 16, 561))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 5, 301, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        pyDegua.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(pyDegua)
        self.statusbar.setObjectName("statusbar")
        pyDegua.setStatusBar(self.statusbar)

        self.retranslateUi(pyDegua)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(pyDegua)

    def retranslateUi(self, pyDegua):
        _translate = QtCore.QCoreApplication.translate
        pyDegua.setWindowTitle(_translate("pyDegua", "pyDegua"))
        self.pushButton.setText(_translate("pyDegua", "Input Images"))
        self.pushButton_2.setText(_translate("pyDegua", "Export Results"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("pyDegua", "Query 1"))


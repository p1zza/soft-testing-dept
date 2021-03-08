# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(QWidget):
    def __init__(self, parent):
        super(Ui_Login, self).__init__(parent)
        parent.setObjectName("Login")
        parent.setEnabled(True)
        parent.resize(502, 163)
        parent.setMinimumSize(QtCore.QSize(502, 162))
        parent.setMaximumSize(QtCore.QSize(1920, 1080))
        parent.setAutoFillBackground(False)
        self.splitter = QtWidgets.QSplitter(parent)
        self.splitter.setGeometry(QtCore.QRect(20, 10, 471, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setMinimumSize(QtCore.QSize(471, 141))
        self.splitter.setMaximumSize(QtCore.QSize(471, 141))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setBold(True)
        self.splitter.setFont(font)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.frame = QtWidgets.QFrame(self.splitter)
        self.frame.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(471, 51))
        self.frame.setMaximumSize(QtCore.QSize(471, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setBold(True)
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setTabletTracking(False)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Login_label = QtWidgets.QLabel(self.frame)
        self.Login_label.setGeometry(QtCore.QRect(20, 15, 61, 21))
        self.Login_label.setFont(font)
        self.Login_label.setObjectName("Login_label")
        self.Login_textBox = QtWidgets.QTextEdit(self.frame)
        self.Login_textBox.setGeometry(QtCore.QRect(99, 10, 361, 29))
        self.Login_textBox.setFont(font)
        self.Login_textBox.setObjectName("Login_textBox")
        self.frame_2 = QtWidgets.QFrame(self.splitter)
        self.frame_2.setMinimumSize(QtCore.QSize(471, 51))
        self.frame_2.setMaximumSize(QtCore.QSize(471, 41))
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.Password_textBox = QtWidgets.QTextEdit(self.frame_2)
        self.Password_textBox.setGeometry(QtCore.QRect(100, 10, 361, 29))
        self.Password_textBox.setFont(font)
        self.Password_textBox.setObjectName("Password_textBox")
        self.Password_label = QtWidgets.QLabel(self.frame_2)
        self.Password_label.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.Password_label.setFont(font)
        self.Password_label.setObjectName("Password_label")
        self.loginButton = QtWidgets.QPushButton(self.splitter)
        self.loginButton.setMinimumSize(QtCore.QSize(471, 20))
        self.loginButton.setMaximumSize(QtCore.QSize(471, 51))
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")
        self.Login_label.setText("Login")
        self.Password_label.setText("Password")
        self.loginButton.setText("Login")

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transform_img_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(833, 565)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 301, 451))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.image_label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.image_label_2.setText("")
        self.image_label_2.setObjectName("image_label_2")
        self.horizontalLayout.addWidget(self.image_label_2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(500, 40, 301, 451))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.image_label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.image_label_3.setText("")
        self.image_label_3.setObjectName("image_label_3")
        self.horizontalLayout_2.addWidget(self.image_label_3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 781, 31))
        self.label_2.setObjectName("label_2")
        self.btn_transform = QtWidgets.QPushButton(self.centralwidget)
        self.btn_transform.setGeometry(QtCore.QRect(350, 340, 119, 41))
        self.btn_transform.setObjectName("btn_transform")
        self.cbo_algorithms = QtWidgets.QComboBox(self.centralwidget)
        self.cbo_algorithms.setGeometry(QtCore.QRect(350, 210, 119, 41))
        self.cbo_algorithms.setObjectName("cbo_algorithms")
        self.cbo_algorithms.addItem("")
        self.cbo_algorithms.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 170, 119, 30))
        self.label.setObjectName("label")
        self.btn_upload = QtWidgets.QPushButton(self.centralwidget)
        self.btn_upload.setGeometry(QtCore.QRect(350, 120, 119, 41))
        self.btn_upload.setObjectName("btn_upload")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(350, 290, 121, 31))
        self.spinBox.setObjectName("spinBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 260, 121, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(720, 500, 81, 20))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 833, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Fourier Transfrom Application</span></p></body></html>"))
        self.btn_transform.setText(_translate("MainWindow", "Transform"))
        self.cbo_algorithms.setItemText(0, _translate("MainWindow", "High Pass Filtering"))
        self.cbo_algorithms.setItemText(1, _translate("MainWindow", "Low Pass Filtering"))
        self.label.setText(_translate("MainWindow", "Choose Algorithms"))
        self.btn_upload.setText(_translate("MainWindow", "Upload Image"))
        self.label_3.setText(_translate("MainWindow", "Radius"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">Code by Nhom4</span></p></body></html>"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show_info.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QBrush, QPixmap,QDesktopServices
from PyQt5.QtCore import QUrl

from UI import add_window


# 跳转窗口添加 QMainWindow 作为参数，新增 def __init__(self)初始化窗体
class Ui_MainWindow (QMainWindow):
    def __init__(self):
        super ().__init__ ()
        self.setWindowFlags (QtCore.Qt.WindowCloseButtonHint)  # 只显示关闭按钮
        self.setupUi (self)  # 初始化窗体设置

    def setupUi(self, MainWindow):
        MainWindow.setObjectName ("MainWindow")
        MainWindow.resize (655, 489)
        # 添加icon
        icon = QtGui.QIcon ()
        icon.addPixmap (QtGui.QPixmap ("../images/mango03.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon (icon)
        self.centralwidget = QtWidgets.QWidget (MainWindow)
        self.centralwidget.setObjectName ("centralwidget")
        self.frame_4 = QtWidgets.QFrame (self.centralwidget)
        self.frame_4.setGeometry (QtCore.QRect (290, 270, 161, 81))
        self.frame_4.setFrameShape (QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow (QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName ("frame_4")
        self.TJ_bt = QtWidgets.QPushButton (self.frame_4)
        self.TJ_bt.setGeometry (QtCore.QRect (40, 12, 75, 51))
        self.TJ_bt.setObjectName ("TJ_bt")
        self.verticalLayoutWidget = QtWidgets.QWidget (self.centralwidget)
        self.verticalLayoutWidget.setGeometry (QtCore.QRect (30, 10, 581, 80))
        self.verticalLayoutWidget.setObjectName ("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout (self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins (0, 0, 0, 0)
        self.verticalLayout.setObjectName ("verticalLayout")
        self.label_name = QtWidgets.QLabel (self.verticalLayoutWidget)
        font = QtGui.QFont ()
        font.setFamily ("Aharoni")
        font.setPointSize (24)
        font.setBold (True)
        font.setWeight (75)
        self.label_name.setFont (font)
        self.label_name.setFrameShape (QtWidgets.QFrame.WinPanel)
        self.label_name.setFrameShadow (QtWidgets.QFrame.Sunken)
        self.label_name.setAlignment (QtCore.Qt.AlignCenter)
        self.label_name.setObjectName ("label_name")
        self.verticalLayout.addWidget (self.label_name)
        self.frame = QtWidgets.QFrame (self.centralwidget)
        self.frame.setGeometry (QtCore.QRect (70, 110, 161, 81))
        self.frame.setFrameShape (QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow (QtWidgets.QFrame.Raised)
        self.frame.setObjectName ("frame")
        self.add_bt = QtWidgets.QPushButton (self.frame)
        self.add_bt.setGeometry (QtCore.QRect (40, 12, 75, 51))
        self.add_bt.setObjectName ("add_bt")
        self.frame_3 = QtWidgets.QFrame (self.centralwidget)
        self.frame_3.setGeometry (QtCore.QRect (70, 270, 161, 81))
        self.frame_3.setFrameShape (QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow (QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName ("frame_3")
        self.area_bt = QtWidgets.QPushButton (self.frame_3)
        self.area_bt.setGeometry (QtCore.QRect (40, 12, 75, 51))
        self.area_bt.setObjectName ("area_bt")
        self.frame_6 = QtWidgets.QFrame (self.centralwidget)
        self.frame_6.setGeometry (QtCore.QRect (500, 110, 161, 81))
        self.frame_6.setFrameShape (QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow (QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName ("frame_6")
        self.math_bt = QtWidgets.QPushButton (self.frame_6)
        self.math_bt.setGeometry (QtCore.QRect (40, 12, 75, 51))
        self.math_bt.setObjectName ("math_bt")
        self.frame_2 = QtWidgets.QFrame (self.centralwidget)
        self.frame_2.setGeometry (QtCore.QRect (290, 110, 161, 81))
        self.frame_2.setFrameShape (QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow (QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName ("frame_2")
        self.nine_bt = QtWidgets.QPushButton (self.frame_2)
        self.nine_bt.setGeometry (QtCore.QRect (40, 12, 75, 51))
        self.nine_bt.setObjectName ("nine_bt")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget (self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry (QtCore.QRect (470, 360, 160, 80))
        self.verticalLayoutWidget_2.setObjectName ("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout (self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins (0, 0, 0, 0)
        self.verticalLayout_2.setObjectName ("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit (self.verticalLayoutWidget_2)
        font = QtGui.QFont ()
        font.setFamily ("Aharoni")
        font.setPointSize (18)
        font.setBold (True)
        font.setUnderline (True)
        font.setWeight (75)
        self.lineEdit.setFont (font)
        self.lineEdit.setLayoutDirection (QtCore.Qt.RightToLeft)
        self.lineEdit.setAutoFillBackground (True)
        self.lineEdit.setObjectName ("lineEdit")
        self.verticalLayout_2.addWidget (self.lineEdit)
        self.date_label = QtWidgets.QLabel (self.verticalLayoutWidget_2)
        self.date_label.setObjectName ("date_label")
        self.verticalLayout_2.addWidget (self.date_label)
        self.frame_5 = QtWidgets.QFrame (self.centralwidget)
        self.frame_5.setGeometry (QtCore.QRect (500, 270, 161, 81))
        self.frame_5.setFrameShape (QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow (QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName ("frame_5")
        self.OT_bt = QtWidgets.QPushButton (self.frame_5)
        self.OT_bt.setGeometry (QtCore.QRect (40, 12, 75, 51))
        self.OT_bt.setObjectName ("OT_bt")
        MainWindow.setCentralWidget (self.centralwidget)
        self.menubar = QtWidgets.QMenuBar (MainWindow)
        self.menubar.setGeometry (QtCore.QRect (0, 0, 655, 23))
        self.menubar.setObjectName ("menubar")
        MainWindow.setMenuBar (self.menubar)
        self.statusbar = QtWidgets.QStatusBar (MainWindow)
        self.statusbar.setObjectName ("statusbar")
        MainWindow.setStatusBar (self.statusbar)

        # 设置窗体背景
        palette = QtGui.QPalette ()
        # 设置窗体背景自适应
        palette.setBrush (MainWindow.backgroundRole (), QBrush (
            QPixmap (r"C:\Users\Administrator\PycharmProjects\Math Tools\images\together.png").scaled (
                MainWindow.size (),
                QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)))
        MainWindow.setPalette (palette)
        MainWindow.setAutoFillBackground (True)  # 设置自动填充背景

        self.retranslateUi (MainWindow)
        QtCore.QMetaObject.connectSlotsByName (MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle (_translate ("MainWindow", "MainWindow"))
        self.TJ_bt.setText (_translate ("MainWindow", "体积计算"))
        self.label_name.setText (_translate ("MainWindow", "数学计算工具"))
        self.add_bt.setText (_translate ("MainWindow", "加减乘除"))
        self.area_bt.setText (_translate ("MainWindow", "面积计算"))
        self.math_bt.setText (_translate ("MainWindow", "数学公式"))
        self.nine_bt.setText (_translate ("MainWindow", "九九乘法表"))
        self.lineEdit.setText (_translate ("MainWindow", "设计：杨超"))
        self.date_label.setText (_translate ("MainWindow", "2020-08-17"))
        self.OT_bt.setText (_translate ("MainWindow", "其他"))
        self.add_bt.clicked.connect (self.open_add_window)
        self.nine_bt.clicked.connect(self.openurl)

    def open_add_window(self):
        self.other_ui = add_window.Ui_frame ()  # 创建水印窗体对象
        self.other_ui.show ()  # 显示窗体

    def openurl(self):
        QDesktopServices.openUrl(QUrl('https://www.baidu.com/'))
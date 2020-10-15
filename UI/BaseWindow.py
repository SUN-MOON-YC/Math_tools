# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BaseWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QBrush,QPixmap
from PyQt5.QtWidgets import QMessageBox
from UI import show_info

import images.tools
import base64
from PIL import ImageQt,Image
from images.YC_icon import img as img64
import sys,os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(img, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionmyTool = QtWidgets.QAction(MainWindow)
        self.actionmyTool.setObjectName("actionmyTool")
        self.actionAboutSoft = QtWidgets.QAction(MainWindow)
        self.actionAboutSoft.setObjectName("actionAboutSoft")
        self.menuTools.addAction(self.actionmyTool)
        self.menuAbout.addAction(self.actionAboutSoft)
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        # 设置窗体背景
        palette = QtGui.QPalette ()
        # 设置窗体背景自适应
        palette.setBrush (MainWindow.backgroundRole (), QBrush (QPixmap ("../images/piano.png").scaled (MainWindow.size (),
                            QtCore.Qt.IgnoreAspectRatio,QtCore.Qt.SmoothTransformation)))
        MainWindow.setPalette (palette)
        MainWindow.setAutoFillBackground (True)  # 设置自动填充背景

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Some Tools"))
        #固定尺寸
        MainWindow.setFixedSize(800,600)
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionmyTool.setText(_translate("MainWindow", "myTool"))
        self.actionAboutSoft.setText(_translate("MainWindow", "AboutSoft"))
        #添加触发
        self.actionmyTool.triggered.connect(self.open_show_info)
        self.menuAbout.triggered.connect(self.about)

    # 定义打开窗口函数
    def open_show_info(self):
        self.other_ui = show_info.Ui_MainWindow()  # 创建水印窗体对象
        self.other_ui.show()  # 显示窗体

    def about(self):
        QMessageBox.information(None,'关于','''QtCore模块涵盖了包的核心的非GUI功能，此模块被用于处理程序中涉及到的 time、文件、目录、数据类型、文本流、链接、mime、线程或进程等对象。
QtGui模块涵盖多种基本图形功能的类; 包括但不限于：窗口集、事件处理、2D图形、基本的图像和界面 和字体文本。
QtWidgets模块包含了一整套UI元素组件，用于建立符合系统风格的classic界面，非常方便，可以在安装时选择是否使用此功能。
QtMultimedia模块包含了一套类库，该类库被用于处理多媒体事件，通过调用API接口访问摄像头、语音设备、收发消息（radio functionality）等。
QtBluetooth模块包含了处理蓝牙活动的类库，它的功能包括：扫描设备、连接、交互等行为。''',QMessageBox.Ok)


if __name__=='__main__':


    app=QtWidgets.QApplication(sys.argv)
    w=QtWidgets.QMainWindow()
    # 使用时需要解码
    tmp = open ('tmp.png', 'wb+')  # 临时文件，用来保存JPG文件
    tmp.write (base64.b64decode (img64))
    tmp.close ()  # 关闭文件

    # image = Image.open ('./tmp.png')  # 打开文件
    img=QPixmap("./tmp.png")

      # 使用PIL模块读取图片
    ui=Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    # image.close ()
    os.remove ('tmp.png')  # 删除文件
    sys.exit(app.exec_())
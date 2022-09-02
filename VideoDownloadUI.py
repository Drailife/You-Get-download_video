# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VideoDownload.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1084, 570)
        font = QtGui.QFont()
        font.setFamily("304-CAI978")
        font.setUnderline(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("#MainWindow{backgroung-image:url(\"E:\\\\Computer wallpaper\\\\girl.png\")}\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.url_input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.url_input.setGeometry(QtCore.QRect(190, 10, 601, 61))
        self.url_input.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.url_input.setObjectName("url_input")
        self.Analysis = QtWidgets.QPushButton(self.centralwidget)
        self.Analysis.setGeometry(QtCore.QRect(840, 10, 121, 61))
        font = QtGui.QFont()
        font.setFamily("TypeLand 康熙字典體")
        font.setPointSize(9)
        self.Analysis.setFont(font)
        self.Analysis.setObjectName("Analysis")
        self.Download = QtWidgets.QPushButton(self.centralwidget)
        self.Download.setGeometry(QtCore.QRect(810, 320, 151, 51))
        font = QtGui.QFont()
        font.setFamily("TypeLand 康熙字典體")
        font.setPointSize(9)
        self.Download.setFont(font)
        self.Download.setObjectName("Download")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 81, 21))
        font = QtGui.QFont()
        font.setFamily("TypeLand 康熙字典體")
        font.setPointSize(12)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(30, 390, 121, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.message = QtWidgets.QTextBrowser(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(190, 80, 601, 231))
        self.message.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.message.setObjectName("message")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 470, 159, 41))
        font = QtGui.QFont()
        self.message.setText('1.输入视频网址\n2.点击Parse进行解析\n3.下拉选择下载文件\n4.点击DownLoad选择存储目录下载\n\n'
                             'Paste:\t粘贴剪切板内容\nParse:\t解析视频\nMessage Clear:\t清空消息框\nDownload:\t选择文件下载\nOpen Explorer:\t打开文件夹')
        font.setFamily("Armstrong Cursive")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Cls = QtWidgets.QPushButton(self.centralwidget)
        self.Cls.setGeometry(QtCore.QRect(810, 260, 151, 51))
        font = QtGui.QFont()
        font.setFamily("TypeLand 康熙字典體")
        font.setPointSize(9)
        self.Cls.setFont(font)
        self.Cls.setObjectName("Cls")
        self.filedownload = QtWidgets.QComboBox(self.centralwidget)
        self.filedownload.setGeometry(QtCore.QRect(190, 320, 601, 51))
        self.filedownload.setObjectName("filedownload")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(30, 330, 121, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setItalic(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.paste = QtWidgets.QPushButton(self.centralwidget)
        self.paste.setGeometry(QtCore.QRect(790, 10, 51, 61))
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.paste.setFont(font)
        self.paste.setObjectName("paste")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 131, 31))
        font = QtGui.QFont()
        font.setFamily("TypeLand 康熙字典體")
        font.setPointSize(12)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pathText = QtWidgets.QTextBrowser(self.centralwidget)
        self.pathText.setGeometry(QtCore.QRect(189, 381, 601, 61))
        self.pathText.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.pathText.setObjectName("pathText")
        self.explorer = QtWidgets.QPushButton(self.centralwidget)
        self.explorer.setGeometry(QtCore.QRect(810, 380, 151, 61))
        font = QtGui.QFont()
        font.setFamily("TypeLand 康熙字典體")
        font.setPointSize(9)
        self.explorer.setFont(font)
        self.explorer.setObjectName("explorer")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video Download"))
        self.url_input.setPlaceholderText(
            _translate("MainWindow", "请输入视频网址:eg. https://www.bilibili.com/video/BV14Y4y1c7L3/"))
        self.Analysis.setText(_translate("MainWindow", "Parse"))
        self.Download.setText(_translate("MainWindow", "Download"))
        self.label.setText(_translate("MainWindow", "URL:"))
        self.label_2.setText(_translate("MainWindow", "文件地址:"))
        self.label_4.setText(_translate("MainWindow", "©DIridescent"))
        self.Cls.setText(_translate("MainWindow", "Message Clear"))
        self.label_5.setText(_translate("MainWindow", "文件选择:"))
        self.paste.setText(_translate("MainWindow", "paste"))
        self.label_3.setText(_translate("MainWindow", "Message:"))
        self.pathText.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">点击\'Download\'选择保存地址，无需输入</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">点击 \'Open Explorer\'可查看打开保存的位置</span></p></body></html>"))
        self.explorer.setText(_translate("MainWindow", "Open Explorer"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()  # 这个是类名，名字根据自定义的情况变化
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

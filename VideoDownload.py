from os.path import exists
from subprocess import run, Popen, PIPE
import threading
from time import sleep

from pyperclip import paste
from PySide2.QtWidgets import QApplication, QMessageBox, QMainWindow
from PySide2.QtWidgets import QFileDialog

from VideoDownloadUI import Ui_MainWindow


class DownLoad:
    def __init__(self):
        self.widgets = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.widgets)
        self.widgets.show()
        self.format_video = []  # 视频的格式
        self.container_video = []  # 视频的封装格式
        self.size_video = []  # 视频大小
        self.title = 'video'  # 视频的标题
        self.filename = ''  # path + title
        self.thread = []
        self.content = []
        self.video_url = ''
        self.path_ui = '/QT_UI/VideoDownload.ui'
        # self.ui = QUiLoader().load(self.path_ui)  # 从文件加载UI定义

        # self.ui.ChoosePath.setHidden(True)      # 隐藏选择存储路径按钮
        self.ui.filedownload.setEnabled(False)  # 失活文件下载下拉选择框
        self.ui.Download.setEnabled(False)
        self.ui.explorer.setEnabled(False)  # 失活explorse按钮
        self.ui.Analysis.clicked.connect(self.ParsebuttonClick)  # Parse 按钮被点击
        self.ui.Cls.clicked.connect(self.cls_click)  # message cls按钮被点击
        self.ui.paste.clicked.connect(self.url_paste)  # paste按钮被点击
        self.ui.Download.clicked.connect(self.open_fileManager)  # download按钮被点击
        self.ui.explorer.clicked.connect(self.open_explorer)

    # Parse 按钮点击
    def ParsebuttonClick(self):
        self.video_url = self.ui.url_input.toPlainText()
        if 'Thread_Parse' in self.getThread():
            QMessageBox.warning(self.widgets, "警告", "解析进程正在进行，请勿重复操作")
            return
        if 'Thread_Download' in self.getThread():
            QMessageBox.warning(self.widgets, "警告", "下载进程正在进行，请等待")
            return
        if self.video_url == '':
            self.ui.message.append('请输入url!')
            QMessageBox.critical(self.widgets, 'Error', '请输入url')
            return
        if self.video_url[0:4] != 'http' and self.video_url[0:4] != 'www.':
            QMessageBox.critical(self.widgets, 'Error', '请输入正确格式的url')
            return
        self.ui.filedownload.setEnabled(False)  # 激活下拉框
        self.ui.filedownload.clear()
        self.ui.message.clear()
        self.format_video.clear()
        self.container_video.clear()
        self.size_video.clear()
        self.content.clear()
        print(self.video_url)
        self.ui.message.append(f'Vedio Url: {self.video_url}\n\n')
        # 添加线程
        print(self.getThread())

        thread_Parse = threading.Thread(target=self.thread_job_Parse, name='Thread_Parse')
        thread_Parse.start()
        self.ui.message.append(f"当前进程:{self.getThread()[1:]}")
        thread_messa = threading.Thread(target=self.message_to_scree, name='Thread_Message')
        thread_messa.start()
        self.ui.message.append(f"当前进程:{self.getThread()[1:]}")

    # 将解析网址的功能添加为一个线程功能
    def thread_job_Parse(self):
        with open("D:\\output.txt", "w", encoding="utf-8") as f:
            cmd_operation = f'you-get -i {self.video_url}\n'
            info_retu = run(cmd_operation, shell=True, stdout=f, stderr=PIPE,
                            universal_newlines=True, encoding='utf-8', timeout=25)
        print('Parse Finish')
        with open("D:\\output.txt", "r", encoding="utf-8") as f:
            self.content = f.readlines()
        self.ui.message.append("\n['Thread_Parse'] 进程结束")

    # 输出解析内容
    def message_to_scree(self):
        self.ui.message.append("\n正在解析……")
        while 1:
            if 'Thread_Parse' not in self.getThread():
                break
        for line_num, line in enumerate(self.content, 1):
            print(line_num, line, end='', sep='-----')
            sleep(0.0001)  # 延时，不然会报错，离谱
            if line_num <= 2:
                sleep(0.0001)  # 延时，不然会报错，离谱
                self.ui.message.append(line)  # 显示输出内容
            # print(line_num, '---', line, sep='', end='')
            if line_num == 2:
                self.title = line[6:].lstrip(' ')
            elif line_num > 28:
                break
            elif line_num in [5, 11, 17, 18, 23, 24] and line[4] == '-':
                self.format_video.append(line[14:].lstrip(' ').rstrip('\n'))  # 获取format
                self.container_video.append(self.content[line_num][17:].lstrip(' ').rstrip('\n'))  # 获取对应的container
                self.size_video.append(self.content[line_num + 2][17:].lstrip(' ').rstrip('\n'))
                pos = self.size_video[-1].find('(')
                self.size_video[-1] = self.size_video[-1][:pos]
        if not self.format_video:
            self.ui.message.append('----Error: 该网址不支持下载----\n' * 3)
        else:
            # self.ui.ChoosePath.setHidden(False)
            self.ui.message.append('\n\n\n-------------------可供下载的内容为------------------')
            self.ui.message.append(f"Title:\t{self.title}")
            for i in range(len(self.format_video)):
                self.ui.message.append(
                    f"下载选择{i + 1}: {self.format_video[i]}\t{self.container_video[i]}\t{self.size_video[i]}")
            self.ui.message.append('\n')
            self.fileinfo_append()

    # open explorer
    def open_explorer(self):
        pos = self.filename.rfind('/')
        print(f'explorer {self.filename[:pos]}')
        Popen(f'explorer "{self.filename[:pos]}"'.replace('/', "\\"))

    # download 按钮点击打开文件管理器选择存储路径
    def open_fileManager(self):
        # 若用户还未完成解析网址，则首先提醒
        if 'Thread_Download' in self.getThread():
            QMessageBox.warning(self.widgets, "警告", "下载进程正在经行，请勿重复操作")
            return
        if not self.format_video:
            QMessageBox.warning(self.widgets, '警告', '请先解析url')
            return
        dirpath = "D:\\OneDrive - bjtu.edu.cn\\Video-juzi"
        if not exists(dirpath):
            dirpath = 'D:\\'
        filePath = QFileDialog.getSaveFileName(self.widgets, "选择存储路径",
                                               dir=dirpath + f"\\video", )  # filter='video files(*.mp4*.flv)'
        print(filePath)
        self.filename = filePath[0]
        self.ui.pathText.setText(self.filename)  # 显示保存路径
        reply = QMessageBox.question(self.widgets, '确认下载', f'确定下载？\n保存地址: {self.filename}',
                                     QMessageBox.No | QMessageBox.Yes)
        self.ui.explorer.setEnabled(True)
        if reply == QMessageBox.No:
            self.ui.message.append('-----下载取消-----')
            return
        thread_download = threading.Thread(target=self.down_file, name="Thread_Download")
        thread_download.start()

    def down_file(self):
        index_choose = self.ui.filedownload.currentIndex()
        self.ui.message.append(f'-----当前选择下载: {index_choose + 1}文件-----')
        pos = self.filename.rfind('/')
        downloadop = f'you-get -o "{self.filename[:pos]}" -O "{self.filename[pos + 1:]}" --format={self.format_video[index_choose]} {self.video_url}'
        print(downloadop)
        try:
            self.ui.message.append(f"\n当前进程:{self.getThread()[1:]}")
            cmd_download = Popen(downloadop, stdin=PIPE, stdout=PIPE, shell=True)
            while True:
                data = cmd_download.stdout.readline().decode('utf-8')
                sleep(0.01)
                self.ui.message.append(data)
                if cmd_download.poll() is not None:
                    break
            self.ui.message.append('DownLoad Successfully')
        except:
            self.ui.message("出现错误！\n" * 3)
            return

    # 实现剪切板粘贴功能
    def url_paste(self):
        self.ui.url_input.clear()  # 清除url输入框内容
        url_data = paste()  # 得到剪切板内容
        self.ui.url_input.setPlainText(url_data)

    # 向文件下载框添加可以下载的文件内容
    def fileinfo_append(self):
        if not self.format_video:
            return
        self.ui.filedownload.setEnabled(True)  # 激活下拉框
        self.ui.Download.setEnabled(True)
        fileinfo = []
        for i in range(len(self.format_video)):
            info = self.format_video[i] + '__' + self.container_video[i] + '__' + self.size_video[i]
            fileinfo.append(info)
        self.ui.filedownload.addItems(fileinfo)  # 添加数据

    # Clear按钮点击清除文本
    def cls_click(self):
        self.ui.message.clear()
        self.ui.message.setText('1.输入视频网址\n2.点击Parse进行解析\n3.下拉选择下载文件\n4.点击DownLoad选择存储目录下载\n\n'
                                'Paste:\t粘贴剪切板内容\nParse:\t解析视频\nMessage Clear:\t清空消息框\nDownload:\t选择文件下载\nOpen Explorer:\t打开文件夹')

    def getThread(self):
        self.thread.clear()
        thread = threading.enumerate()
        for i in thread:
            self.thread.append(i.getName())
        return self.thread


app = QApplication([])
video = DownLoad()
video.widgets.show()
app.exec_()

import os
import subprocess


def getpath():
    while 1:
        path = input('save_path: ')
        if not os.path.exists(path):
            print("path isn't exited,please input again……")
        else:
            break
    return path


class DownloadVideo:
    video_url = 'https://www.bilibili.com/video/BV1yP411L7oR'
    format_video = []  # 视频的格式
    container_video = []  # 视频的封装格式
    title = ''  # 视频的标题

    def handelvedio(self):
        try:
            cmd_operation = subprocess.Popen('you-get -i ' + self.video_url, stdout=subprocess.PIPE, shell=True,
                                             encoding='utf-8')
        except:
            print('Error:解析错误, 请查看网址是否正确')
        content = cmd_operation.stdout.readlines()
        for line_num, line in enumerate(content, 1):
            # print(line_num, line, end='', sep='-----')
            if line_num == 2:
                h_title = line[6:].lstrip(' ')
            elif line_num > 24:
                break
            elif line_num in [5, 11, 17, 18, 23, 24] and line[4] == '-':
                self.format_video.append(line[14:].lstrip(' ').rstrip('\n'))  # 获取format
                self.container_video.append(content[line_num][17:].lstrip(' ').rstrip('\n'))  # 获取对应的container


# vedio_url = input('vedio-url: ')  # 需要下载的视频的网址
save_path = os.getcwd()
download = DownloadVideo()
download.handelvedio()
print(download.title)
print(download.format_video)
print(download.container_video)
save_path = getpath()
# os.system(f'you-get --format={format_video[0]} {vedio_url} -o {save_path}')

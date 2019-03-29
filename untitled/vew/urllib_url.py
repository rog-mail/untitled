
from urllib import request
import re

host_rul = 'http://www.90aizy.com/'

def request_home(url):
    # 访问获取到的地址
    req = request.Request(url)
    response = request.urlopen(req)
    html = response.read().decode('utf-8')
    return html

def video_list(html_data):
    # 从页面获取视频路径和地址
    vid_path = re.findall(r'"/vodlist/(\d+).html"', html_data)
    vod = list(map(int, set(vid_path)))
    vod.sort()
    return vod

def video_analyze():
    # 从子页面获取视频信息(名称,图片,视频播放地址)
    pass

def main():
    # 获取主页地址并获取在线视频路径
    path_data = video_list(request_home(host_rul))
    print(path_data)

if __name__ == '__main__':
    # 脚本开始
    main()

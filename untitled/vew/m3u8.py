
from urllib import request, response
import os


class index(object):
    def __init__(self):
        self.m3u8_url = 'https://cdn.letv-cdn.com/2018/12/05/JOCeEEUuoteFrjCg/playlist.m3u8'

    def file_(self):
        """判断文件夹是否存在"""
        if os.path.exists('./m3u8') != True:
            os.makedirs('./m3u8')

    def get_m3u8(self, m3u8_url):
        # m3u8_url m3u8文件的文件网络地址
        # 访问m3u8文件地址
        response = request.urlopen(m3u8_url)
        return response

    def seve_m3u8(self, m3u8_url, txt):
        # m3u8_url m3u8文件的文件网络地址
        # txt m3u8文件的数据
        # 将获取到的m3u8文件保存
        text = txt.read().decode()
        with open(f'./m3u8/{m3u8_url[53:]}', 'w+') as f:
            f.write(text)
        path = f'./m3u8/{m3u8_url[53:]}'
        return path

    def read_list(self, path):
        # path 为文件路径
        # 读取m3u8文件并将文件名转换成列表
        file = open(path, mode='r', encoding='utf-8')
        ts = []
        for i in file:
            if '.ts' in i:
                # 将文件名逐个添加至列表并去除换行符
                ts.append(i.strip('\n'))
        return ts

    def seve_m3u8_(self, data, path):
        with open(f'{path}', 'wb+') as f:
            f.write(data.read())

    def main(self):
        # path = self.seve_m3u8(self.m3u8_url, self.get_m3u8(self.m3u8_url))
        ts = self.read_list('./m3u8/playlist.m3u8')
        for i in ts:
            self.seve_m3u8_(self.get_m3u8(self.m3u8_url[:-13] + i), f'./m3u8/{i}')
            print(self.m3u8_url[:-13] + i, '保存完成!~')
        print('文件已全部保存完成!~')

if __name__ == '__main__':
    abc = index()
    abc.file_()
    abc.main()

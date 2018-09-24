# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests,sys
import html5lib

class downloader(object):

    def __init__(self):
        self.server = 'https://www.rrtxt.com'  #首页
        self.target = 'https://www.rrtxt.com/read/DaJieZhu.html' #目标页
        self.names = []    
        self.urls = []
        self.nums = 0

    def  get_download_url(self):
        req = requests.get(url = self.target)
        html = req.text
        div_bf = BeautifulSoup(html,"html5lib")
        div = div_bf.find_all('div',id = 'readerlists')
        a_bf =BeautifulSoup(str(div[0]),"html5lib")
        a = a_bf.find_all('a')
        self.nums = len(a[15:])
        for each in a[15:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    def get_contents(self,target):
        req = requests.get(url = target)
        html = req.text
        bf = BeautifulSoup(html,"html5lib")
        texts = bf.find_all('div',class_ = 'content')
        texts = texts[0].text.replace('\xa0'*8,'\n\n')
        return texts

    def writer(self,name,path,text):
        write_flag = True
        with open(path,'a',encoding ='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == '__main__':
    dl = downloader()
    dl.get_download_url()
    print('《大劫主》开始下载：')
    for i in range(dl.nums):
        dl.writer(dl.names[i],'大劫主.txt',dl.get_contents(dl.urls[i]))
        sys.stdout.write("  已下载:%.3f%%" % float(i/dl.nums) + '\r')
        sys.stdout.flush()
    print('《大劫主》下载完成')    










        
        

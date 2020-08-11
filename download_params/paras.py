from parsel import Selector

from bs4 import BeautifulSoup

from multiprocessing import Process
import os
import subprocess

htmlFile = open("download_params/source.html")

soup = BeautifulSoup(htmlFile,'lxml')
https  = []

def parse_local_html():
    for item in soup.select('table'):
        for it in item.select('tr td a'):
            result = it.string
            if result:
                https.append("https://proofs.filecoin.io/" + result)



def run_proc(name):
    cmd = 'wget ' + name
    subprocess.call(cmd,shell=True)


if __name__ == '__main__':
    parse_local_html()
    for item in https:
        print('Parent process %s.' % os.getpid())
        p = Process(target = run_proc, args = (item, ))
        p.start()
        p.join()
        print("End!!!")
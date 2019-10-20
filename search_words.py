
"""
1. 要确认联网了没
2. 要能链接到一些查词网站
3. 要把音标和解释的文本扒下来
4. 要把扒下来的东西整理成对应字段的信息然后存储

后续可能增加一个某单词词频的统计功能
和最近学习数量的统计功能
"""

import pandas as pd
import os
import subprocess
import urllib.request as request


# 测试网络
def test_network():
    null = open(os.devnull, 'w')
    return1 = subprocess.call('ping 8.8.8.8', shell=True, stdout=null, stderr=null)
    if return1 == 0:
        subprocess.call('msdt.exe /id NetworkDiagnosticsNetworkAdapter', shell=True, stdout=null, stderr=null)
        print('网络有问题，请保证网络通畅！')
        null.close()
        return 0
    else:
        null.close()
        return 1


def get_words_meaning():
# todo 增加一个方法可以自定义增加查询的网址，写一个class， 自增加的网址对应的目标位置也要做定义
    base_url = ['http://iciba.com/','https://translate.google.cn/']
    with request.urlopen('http://python.org/') as response:
        html = response.read()
        print(html)


 
        
if __name__ == '__main__':
    # test_network()
    get_words_meaning()

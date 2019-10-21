
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
import requests
import lxml.html

etree = lxml.html.etree


# 测试网络
def test_network():
    null = open(os.devnull, 'w')
    return1 = subprocess.call('ping 8.8.8.8', shell=True, stdout=null, stderr=null)
    if return1:
        subprocess.call('msdt.exe /id NetworkDiagnosticsNetworkAdapter', shell=True, stdout=null, stderr=null)
        print('网络有问题，请保证网络通畅！')
        null.close()
        return 0
    else:
        null.close()
        return 1


def get_words_meaning(word_list):
    result = []
    for word in word_list:
        res1 = {'原词': word}
        base_url = 'http://iciba.com/'
        use_url = base_url + word
        headers = {
            'Cookie': 'OCSSID=4df0bjva6j7ejussu8al3eqo03',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        }
        response = requests.get(use_url, headers=headers)
        html = response.content.decode('utf-8')
        html = etree.HTML(html)

        location_xpath = ['.//div[@class="base-speak"]/span/span/text()', './/div[@class="in-base"]/ul/li/span/text()',
                          './/div[@class="in-base"]/ul/li/p/span/text()']
        name_list = ['音标', '词性', '释义']
        for i, path in enumerate(location_xpath):
            res = html.xpath(path)
            res1[name_list[i]] = res
        result.append(res1)
        print(res1)
    print(result)
    return result


def main_search(word_list, save_path):
    flag = test_network()
    if flag == 1:
        file = pd.DataFrame(get_words_meaning(word_list))
        file = file[['原词', '音标', '词性', '释义']]
        file.to_csv(save_path, index=None)
    else:
        print("网络问题，请联网再试！")


if __name__ == '__main__':
    list_words = ['name', 'book', 'patronage']
    main_search(list_words, './record.csv')

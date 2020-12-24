# -*- coding: utf-8 -*-
"""
-----------------------------
    File Name: SoapgetText
    Description:
    Author: quan
    data: 2020/07/02
-----------------------------
"""
import requests
import os
from bs4 import BeautifulSoup

def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
    try:
        html = requests.get(url,headers = headers)
        #html.encoding = html.encoding
        html.encoding = html.apparent_encoding
        if html.status_code == 200:
            print('get url ok')
    except Exception as e:
        print('get url fail：%s' %e)
    return html.text

def My_GetHtml(url,name):
    soup = BeautifulSoup(url,'lxml')
    pathD = 'data'
    Old_PathD = os.getcwd()
    if pathD in os.listdir():
        pass
    else:
        os.mkdir(pathD)
    os.chdir(pathD)
    flag_D = 0
    fname =name + '.txt'
    open_file = open(fname,'w',encoding='utf8')

    for sText in soup.stripped_strings:
       #print(sText)
        if sText[0] == "（" or sText[0] == "【" :
            print("-----------")
            flag_D = 1
        if sText == '精品测算':
            print("==========")
            flag_D = 0
        if flag_D:
            #print(sText)
            open_file.write(sText+'\n')

    open_file.close()
    print('Download ok')
    os.chdir(Old_PathD)

if __name__ == '__main__':
    url1 = 'https://m.k366.com/gua/1200000-11-'
    for n in range(1,65):
        url = url1+str('{:0>2d}'.format(n))+'.htm'
        print(url)
        url2 = get_html(url)
        My_GetHtml(url2,str(n))

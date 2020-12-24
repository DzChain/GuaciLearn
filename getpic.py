# -*- coding: utf-8 -*-
"""
-----------------------------
    File Name: GetImage
    Description:
    Author: quan
    data: 2020/06/14
-----------------------------
"""
import requests
#from lxml import etree
import re
import os
import random

def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

    try:
        html = requests.get(url,headers = headers)
        html.encoding = html.encoding
        if html.status_code == 200:
            print('get url ok')
            #print(html.text)
    except Exception as e:
        print('get url fail：%s' %e)
    return html.text

def get_images(html):
    urls =re.findall('"130" src="(.*?)"',html,re.S)
    #print(urls)
    return urls

def downloadimg(urls,name):
    pathD = 'pic'
    Old_PathD = os.getcwd()
    if pathD in os.listdir():
        pass
    else:
        os.mkdir(pathD)
    os.chdir(pathD)
    i =0
    for url in urls:
        imag = requests.get('https:'+url).content
        with open(name+'.gif','wb') as f:
            print('Download %d picture:%s' %(i+1,url))
            f.write(imag)
        i+=1
    print('Download ok')
    os.chdir(Old_PathD)


if __name__ == '__main__':
    url1 = 'https://m.k366.com/gua/1200000-11-'
    for n in range(1,65):
        url = url1+str('{:0>2d}'.format(n))+'.htm'
        print(url)
        html = get_html(url)
        imageurls = get_images(html)
        downloadimg(imageurls,str(n))

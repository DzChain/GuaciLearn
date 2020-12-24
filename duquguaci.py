# -*- coding: utf-8 -*-
"""
-----------------------------
    File Name: duquguaci
    Description:v2
    Author: quan
    data: 2020/07/07
-----------------------------
"""
import random
gkey = 0
def qigua():
    num = random.randint(1,64)
    return num

def getguaming(gkey):
    fname = './data/' + str(gkey) + '.txt'
    f = open(fname, encoding='utf8')
    guaming = ""
    for each_line in f:
        if each_line[0] == '【' or each_line[0] =='（':
            guaming = each_line[:]
            break
    f.close()
    #print(guaming)
    return guaming
def getguaci(gkey):
    fname = './data/'+str(gkey) + '.txt'
    f = open(fname,encoding='utf8')
    guaci = ""
    for each_line in f:
        guaci += each_line
    f.close()
    #print(guaci)
    return guaci
def main():
    #getguaci(1)
    getguaming(2)
if __name__ == '__main__':
    main()

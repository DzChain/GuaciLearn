# -*- coding: utf-8 -*-
"""
-----------------------------
    File Name: Tkshow
    Description:v2
    Author: quan
    data: 2020/07/07
-----------------------------
"""

import duquguaci
from tkinter import *

def shuaxinguaci():
    gkey = duquguaci.qigua()
    global  guaci1 , guaming1
    guaci1 = duquguaci.getguaci(gkey)
    guaming1 = duquguaci.getguaming(gkey)
    picpath = './pic/'+str(gkey)+'.gif'
    newGuatu =PhotoImage(file = picpath)
    GuatuLabel.config(image = newGuatu)
    GuatuLabel.image = newGuatu
    text1.delete(1.0,END)
    text1.insert(INSERT, guaming1)
    text2.delete(1.0, END)
    text2.insert(INSERT, guaci1)
    root.update()

if __name__ == '__main__':
    root  = Tk()
    root.title("周易学习")
    Label(root, text = "卦名").grid(row = 0, sticky = W)
    Guatu = PhotoImage(file = './pic/00.gif')
    GuatuLabel = Label(root, image=Guatu)
    GuatuLabel.grid(row = 0, column = 1, rowspan = 3,sticky =N+S, padx = 0, pady = 5)
    #Label(root, image = Guatu).pack(side = RIGHT)
    Label(root, text = "卦辞").grid(row = 2, sticky = W)

    guaming1 = "显示卦名"
    guaci1 = "显示卦辞"

    text1 =Text(root, width = 35 , height = 1)
    text1.grid(row = 1, column = 0, sticky = W)
    text1.insert(INSERT, guaming1)
    text2 = Text(root, width = 60, height = 30)
    text2.grid(row = 3, column = 0,columnspan = 2)
    text2.insert(INSERT, guaci1)

    scroll = Scrollbar()
    scroll.grid(row = 3, column = 2, sticky =W +E + N + S)
    # 两个控件关联
    scroll.config(command=text2.yview)
    text2.config(yscrollcommand=scroll.set)

    theButton = Button(text = "起卦", width = 10, command = shuaxinguaci)
    theButton.grid(row = 4, columnspan = 3, pady = 5)

    mainloop()

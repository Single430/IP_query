#! /usr/bin/python
# coding=utf-8

import urllib2
import json

from Tkinter import *


def get_ip():
    # global VAR

    url = 'http://apis.baidu.com/apistore/iplookupservice/iplookup?ip=%s' % VAR.get()
    req = urllib2.Request(url)
    req.add_header("apikey", "yourself key")

    resp = urllib2.urlopen(req)
    con = resp.read()
    con = json.loads(con)

    try:
        string = con['retData']['country']+con['retData']['province']+con['retData']['city']+con['retData']['district']+':'+con['retData']['carrier']
        VAR1.set(string)
    except TypeError:
        get_ip()


def tk_gui():
    global VAR, root, VAR1

    root = Tk()
    root.title('IP 查询')
    root.geometry('240x200')
    root.resizable(width=False, height=False)    # 宽不可变, 高不可变,默认为True
    ip = Label(root, text="输入IP", bg="green", font=("Arial", 12), width=5, height=2)
    Label(root, text='IP 查询', font=('Arial', 20)).pack()
    ip.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM

    VAR = StringVar()
    e = Entry(root, textvariable=VAR)
    # VAR.set("input ip")
    e.pack()
    Button(root, text="查询", command=get_ip).pack()
    VAR1 = StringVar()
    e1 = Entry(root, textvariable=VAR1, width="30")
    # VAR.set("input ip")
    e1.pack()

    root.mainloop()

if __name__ == "__main__":
    tk_gui()

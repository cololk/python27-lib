#!/usr/bin/env python
#-*- coding:utf-8 -*-
#本程式示範重新定向系統的標準輸出到指定的文件,而非控制台上(命令提示介面)

import wx
import sys

class Frame(wx.Frame):
    def __init__(self,parent,id,title):
        print "Frame __init__"
        wx.Frame.__init__(self,parent,id,title)

class App(wx.App):
    #wxPython允許在創建應用程序時設置兩個參數
    #第一個參數是redirect,如果值為True,則第二個參數filename也能被設置
    #這樣的話輸出會被重定向到filename指定的文件中
    def __init__(self,redirect=True, filename=None):
        print "App __init__"
        wx.App.__init__(self,redirect,filename)

    def OnInit(self): #OnInit()會被wxPython自動的調用
        print "OnInit" #輸出到stdout
        self.frame=Frame(parent=None,id=-1,title='Startup') #創建框架
        self.frame.Show()
        self.SetTopWindow(self.frame)
        print>>sys.stderr, "A pretend error message" #輸出到stderr
        return True

    def OnExit(self):
        print "OnExit"

if __name__=='__main__':
    app=App(True,"output")  #1 文本重定向從此開始, redirect=True 重定向到output文件中
    print "before MainLoop"
    app.MainLoop()          #2 進入主事件循環
    print "after MainLoop"

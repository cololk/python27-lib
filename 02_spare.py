#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Spare.py is a starting point for a wxPython program """ #這是個文檔字串符,會儲存在該模塊的__doc__屬性中
import wx

class Frame(wx.Frame): #這邊定義自己的Frame,button, list之類的
    pass

class App(wx.App): #這邊定義了一個名為MyApp的子類

    def OnInit(self): #通常我們會在OnInit()方法中創建frame對象
        self.frame=wx.Frame(parent=None, title='Spare') #在wx.Frame接收的參數中,僅有第一個是必須的,其他的都有默認值
        self.frame.Show() #調用Show()方法使frame可見,否則的話是不可見的,Show()默認值為True
        self.SetTopWindow(self.frame) #將frame實例傳入SetTopWindow()方法中,可指定讓wxPython知道哪個框架是主要的
        return True
#這個是Python用來檢測該模塊是作為程序獨立運行,還是被另一模塊所導入,__name__屬性來實現
if __name__=='__main__': 
    app=App()
    app.MainLoop()

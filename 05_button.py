#!/usr/bin/env python
#-*- coding:utf-8 -*-

import wx

class InsertFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Frame With Button',size=(300,100))
        panel=wx.Panel(self) #創建畫板
        #將按鈕添加到畫板
        button=wx.Button(panel, label="Close", pos=(125,10),size=(50,50))
        #綁定按鈕的單擊事件
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        #綁定窗口的關閉事件
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnCloseMe(self,event):
        self.Close(True)

    def OnCloseWindow(self,event):
        self.Destroy()

if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=InsertFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
    

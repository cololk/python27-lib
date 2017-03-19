# -*- coding: utf-8 -*-
import wx

class App(wx.App): #這邊定義了一個名為MyApp的子類

    def OnInit(self): #通常我們會在OnInit()方法中創建frame對象
        frame=wx.Frame(parent=None, title='Bare') #在wx.Frame接收的參數中,僅有第一個是必須的,其他的都有默認值
        frame.Show() #調用Show()方法使frame可見,否則的話是不可見的,Show()默認值為True
        return True

app=App()
app.MainLoop()

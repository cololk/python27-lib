#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Hello, wxPython!program."""
import wx

class Frame(wx.Frame): #2 定義一個wx.Frame子類
    """Frame class that displays an image."""
    #3 給我們的框架構造器增加一個圖像參數
    def __init__(self, image, parent=None, id=-1, pos=wx.DefaultPosition, title='Hello, wxPython!'):
        """Create a Frame instance and display image."""
        #4 顯示圖像
        temp=image.ConvertToBitmap() #轉換圖像到位圖
        size=temp.GetWidth(),temp.GetHeight() #利用圖像的寬度與高度創建一個SIZE元組
        wx.Frame.__init__(self,parent,id,title,pos,size) #size元組被提供給wx.Frame.__init__()調用,以便於框架的尺寸匹配位圖尺寸
        self.bmp=wx.StaticBitmap(parent=self, bitmap=temp) #利用wx.StaticBitmap控件來顯示這個圖像
class App(wx.App):
    """Application class."""
    def OnInit(self): #定義一個帶有OnInit()方法的wx.App的子類,wxPython應用程序最基本的要求
        #我們使用與hello.py在同一目錄下名為wxPython.jpg的文件創建一個圖像對象(物件)
        image=wx.Image('black_cat-007.jpg', wx.BITMAP_TYPE_JPEG)
        self.frame=Frame(image)

        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
#7 創建一個應用程序的實例並啟動wxPython的事件循環
def main():
    app=App()
    app.MainLoop()
    
if __name__=='__main__':
    main()

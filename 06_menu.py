#!/usr/bin/env python
#-*- coding:utf-8 -*-

import wx
from wx.lib import pydocview #注意這邊用法跟書不同

class ToolbarFrame(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'Toolbars',size=(300,200))
		panel=wx.Panel(self)
		panel.SetBackgroundColour('White')
		statusBar=self.CreateStatusBar() #1 創建狀態欄
		toolbar=self.CreateToolBar()     #2 創建工具欄
		toolbar.AddSimpleTool(wx.NewId(), pydocview.New.GetBitmap(),"New","Long help for'New'") #3 給工具欄增加一個工具
		toolbar.Realize()  #4 準備顯示工具欄
		menuBar=wx.MenuBar() #創建menu
		#創建兩個菜單
		menual=wx.Menu()
		menuBar.Append(menual, "&File")
		menu2=wx.Menu()
		#創建菜單的項目
		menu2.Append(wx.NewId(),"&Copy","Copy in status bar")
		menu2.Append(wx.NewId(), "C&ut", "")
		menu2.Append(wx.NewId(), "Paste","")
		menu2.AppendSeparator()
		menu2.Append(wx.NewId(),"&Options...","Display Options")
		menuBar.Append(menu2,"&Edit") #在菜單欄上附上菜單
		self.SetMenuBar(menuBar)  #在框架上附上菜單欄

if __name__=='__main__':
	app=wx.PySimpleApp()
	frame=ToolbarFrame(parent=None,id=-1)
	frame.Show()
	app.MainLoop()



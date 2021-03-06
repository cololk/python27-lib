#!/usr/bin/env python
#-*- coding:utf-8 -*-
import wx

class DoubleEventFrame(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'Frame With Button',size=(300,100))
		self.panel=wx.Panel(self,-1)
		self.button=wx.Button(self.panel,-1,"Click Me",pos=(100,15))
		self.Bind(wx.EVT_BUTTON, self.OnButtonClick,self.button)  #1 綁定按鈕敲擊事件
		self.button.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)  #2 綁定鼠標左鍵按下事件

	def OnButtonClick(self,event): #這個就是按鈕事件的處理器
		self.panel.SetBackgroundColour('Green')
		self.panel.Refresh()

	def OnMouseDown(self,event):  #這個就是滑鼠左鍵點擊事件的處理器
		self.button.SetLabel("Again!")
		event.Skip() #為了進一步的事件處理,必須調用Skip()方法,否則進一步的事件處理將被阻止(按鈕放開才會觸發EVT_BUTTON事件)

if __name__=='__main__':
	app=wx.PySimpleApp()
	frame=DoubleEventFrame(parent=None,id=-1)
	frame.Show()
	app.MainLoop()

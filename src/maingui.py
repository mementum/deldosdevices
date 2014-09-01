# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

from utils.widgets.sortlistctrl import SortListCtrl
import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"DelDosDevices", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrlDosDevices = SortListCtrl( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.LC_VRULES )
		bSizer4.Add( self.m_listCtrlDosDevices, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer1 = wx.GridSizer( 2, 2, 0, 0 )
		
		self.m_checkBoxLoadOnStart = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"Load On Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxLoadOnStart.SetValue(True) 
		gSizer1.Add( self.m_checkBoxLoadOnStart, 0, wx.ALL, 5 )
		
		self.m_checkBoxEmptyDriveLetters = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"Show Empty Drives", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxEmptyDriveLetters.SetValue(True) 
		gSizer1.Add( self.m_checkBoxEmptyDriveLetters, 0, wx.ALL, 5 )
		
		self.m_checkBoxCapitalDriveLetters = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"Capital Drive Letters", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxCapitalDriveLetters.SetValue(True) 
		gSizer1.Add( self.m_checkBoxCapitalDriveLetters, 0, wx.ALL, 5 )
		
		self.m_checkBoxSkipFloppys = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"Skip Floppy Drive Letters", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_checkBoxSkipFloppys, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( gSizer1, 0, wx.EXPAND, 5 )
		
		
		bSizer23.Add( bSizer4, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_buttonRefresh = wx.Button( self.m_panel2, wx.ID_ANY, u"&Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_buttonRefresh, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_buttonDeleteSelected = wx.Button( self.m_panel2, wx.ID_ANY, u"&Delete Selected", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_buttonDeleteSelected, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_buttonAbout = wx.Button( self.m_panel2, wx.ID_ANY, u"About ...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_buttonAbout, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_buttonExit = wx.Button( self.m_panel2, wx.ID_ANY, u"E&xit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_buttonExit, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer23.Add( bSizer10, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		bSizer8.Add( bSizer23, 1, wx.EXPAND, 5 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel2, wx.ID_ANY, u"Operations Log" ), wx.VERTICAL )
		
		self.m_textCtrlLog = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		sbSizer1.Add( self.m_textCtrlLog, 1, wx.EXPAND, 5 )
		
		self.m_buttonClearLog = wx.Button( self.m_panel2, wx.ID_ANY, u"Clear Log", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_buttonClearLog, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer8.Add( sbSizer1, 1, wx.EXPAND, 5 )
		
		
		self.m_panel2.SetSizer( bSizer8 )
		self.m_panel2.Layout()
		bSizer8.Fit( self.m_panel2 )
		bSizer7.Add( self.m_panel2, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		bSizer7.Fit( self )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItemRefresh = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"&Refresh", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItemRefresh )
		
		self.m_menuItemDelete = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Delete", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItemDelete )
		
		self.m_menu1.AppendSeparator()
		
		self.m_menuItemExit = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"E&xit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItemExit )
		
		self.m_menubar1.Append( self.m_menu1, u"&File" ) 
		
		self.m_menu2 = wx.Menu()
		self.m_menuItemAbout = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"&About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.m_menuItemAbout )
		
		self.m_menubar1.Append( self.m_menu2, u"&Help" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_toolBar1 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
		self.m_toolRefresh = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( u"priv/icons/arrow_refresh.png", wx.ART_OTHER ), wx.NullBitmap, wx.ITEM_NORMAL, u"Refresh", wx.EmptyString, None ) 
		
		self.m_toolDelete = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( u"priv/icons/cancel.png", wx.ART_OTHER ), wx.NullBitmap, wx.ITEM_NORMAL, u"Delete", wx.EmptyString, None ) 
		
		self.m_toolBar1.AddSeparator()
		
		self.m_toolAbout = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( u"priv/icons/information.png", wx.ART_OTHER ), wx.NullBitmap, wx.ITEM_NORMAL, u"About", wx.EmptyString, None ) 
		
		self.m_toolBar1.AddSeparator()
		
		self.m_toolExit = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( u"priv/icons/user_go.png", wx.ART_OTHER ), wx.NullBitmap, wx.ITEM_NORMAL, u"Exit", wx.EmptyString, None ) 
		
		self.m_toolBar1.Realize() 
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_SIZE, self.OnSizeMainFrame )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnSizeMainFrame( self, event ):
		event.Skip()
	

###########################################################################
## Class AboutDialog
###########################################################################

class AboutDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"About", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebookAbout = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panelAbout = wx.Panel( self.m_notebookAbout, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticTextAppNameVersion = wx.StaticText( self.m_panelAbout, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextAppNameVersion.Wrap( -1 )
		bSizer10.Add( self.m_staticTextAppNameVersion, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticTextCopyright = wx.StaticText( self.m_panelAbout, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextCopyright.Wrap( -1 )
		bSizer10.Add( self.m_staticTextCopyright, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_hyperlinkURL = wx.HyperlinkCtrl( self.m_panelAbout, wx.ID_ANY, u"wxFB Website", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.HL_ALIGN_CENTRE|wx.HL_DEFAULT_STYLE )
		bSizer10.Add( self.m_hyperlinkURL, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		self.m_panelAbout.SetSizer( bSizer10 )
		self.m_panelAbout.Layout()
		bSizer10.Fit( self.m_panelAbout )
		self.m_notebookAbout.AddPage( self.m_panelAbout, u"About", True )
		
		bSizer8.Add( self.m_notebookAbout, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_buttonClose = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_buttonClose, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
		bSizer8.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class PanelAboutDocument
###########################################################################

class PanelAboutDocument ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL )
		
		bSizer111 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrlDocument = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_AUTO_URL|wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer111.Add( self.m_textCtrlDocument, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer111 )
		self.Layout()
		bSizer111.Fit( self )
	
	def __del__( self ):
		pass
	


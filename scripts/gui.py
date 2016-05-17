###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

ID_SAVE = 1000
ID_QUIT = 1001
ID_ABOUT = 1002

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Franhofer", pos = wx.DefaultPosition, size = wx.Size( 1069,624 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.panel1 = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.slider_label11 = wx.StaticText( self.panel1, wx.ID_ANY, u"slit with(micron)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.slider_label11.Wrap( -1 )
		bSizer4.Add( self.slider_label11, 0, wx.ALL|wx.ALIGN_BOTTOM, 15 )
		
		self.slider11 = wx.Slider( self.panel1, wx.ID_ANY, 120, 10, 400, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_LABELS )
		bSizer4.Add( self.slider11, 1, wx.ALL|wx.ALIGN_BOTTOM, 0 )
		
		self.slider_label12 = wx.StaticText( self.panel1, wx.ID_ANY, u"wave length(nm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.slider_label12.Wrap( -1 )
		bSizer4.Add( self.slider_label12, 0, wx.ALL|wx.ALIGN_BOTTOM, 15 )
		
		self.slider12 = wx.Slider( self.panel1, wx.ID_ANY, 632, 200, 800, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_LABELS )
		bSizer4.Add( self.slider12, 1, wx.ALL|wx.ALIGN_BOTTOM, 0 )
		
		self.slider_label13 = wx.StaticText( self.panel1, wx.ID_ANY, u"Distance from screen(cm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.slider_label13.Wrap( -1 )
		bSizer4.Add( self.slider_label13, 0, wx.ALL|wx.ALIGN_BOTTOM, 15 )
		
		self.slider13 = wx.Slider( self.panel1, wx.ID_ANY, 50, 10, 500, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_LABELS )
		bSizer4.Add( self.slider13, 1, wx.ALL|wx.ALIGN_BOTTOM, 0 )
		
		
		self.panel1.SetSizer( bSizer4 )
		self.panel1.Layout()
		bSizer4.Fit( self.panel1 )
		self.notebook.AddPage( self.panel1, u"One slit diffraction", True )
		self.panel2 = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.slider_label21 = wx.StaticText( self.panel2, wx.ID_ANY, u"slit with(micron)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.slider_label21.Wrap( -1 )
		bSizer6.Add( self.slider_label21, 0, wx.ALL|wx.ALIGN_BOTTOM, 15 )
		
		self.slider21 = wx.Slider( self.panel2, wx.ID_ANY, 435, 10, 6000, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_LABELS )
		bSizer6.Add( self.slider21, 1, wx.ALL|wx.ALIGN_BOTTOM, 0 )
		
		self.slider_label22 = wx.StaticText( self.panel2, wx.ID_ANY, u"distance between slits(mm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.slider_label22.Wrap( -1 )
		bSizer6.Add( self.slider_label22, 0, wx.ALL|wx.ALIGN_BOTTOM, 15 )
		
		self.slider22 = wx.Slider( self.panel2, wx.ID_ANY, 1, 1, 200, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_LABELS )
		bSizer6.Add( self.slider22, 1, wx.ALL|wx.ALIGN_BOTTOM, 0 )
		
		self.slider_label23 = wx.StaticText( self.panel2, wx.ID_ANY, u"wavelength(nm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.slider_label23.Wrap( -1 )
		bSizer6.Add( self.slider_label23, 0, wx.ALL|wx.ALIGN_BOTTOM, 15 )
		
		self.slider23 = wx.Slider( self.panel2, wx.ID_ANY, 632, 200, 800, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_LABELS )
		bSizer6.Add( self.slider23, 1, wx.ALL|wx.ALIGN_BOTTOM, 0 )
		
		self.slider_label24 = wx.StaticText( self.panel2, wx.ID_ANY, u"screen distance(cm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.slider_label24.Wrap( -1 )
		bSizer6.Add( self.slider_label24, 0, wx.ALL|wx.ALIGN_BOTTOM, 15 )
		
		self.slider24 = wx.Slider( self.panel2, wx.ID_ANY, 50, 10, 500, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_LABELS )
		bSizer6.Add( self.slider24, 1, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		
		self.panel2.SetSizer( bSizer6 )
		self.panel2.Layout()
		bSizer6.Fit( self.panel2 )
		self.notebook.AddPage( self.panel2, u"Two slits diffraction", False )
		self.panel3 = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.slider_label31 = wx.StaticText( self.panel3, wx.ID_ANY, u"slit with(micron)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.slider_label31.Wrap( -1 )
		bSizer7.Add( self.slider_label31, 0, wx.ALL|wx.ALIGN_BOTTOM, 15 )
		
		self.slider31 = wx.Slider( self.panel3, wx.ID_ANY, 250, 1, 600, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_LABELS )
		bSizer7.Add( self.slider31, 1, wx.ALL|wx.ALIGN_BOTTOM, 0 )
		
		self.slider_label32 = wx.StaticText( self.panel3, wx.ID_ANY, u"distance between slits(mm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.slider_label32.Wrap( -1 )
		bSizer7.Add( self.slider_label32, 0, wx.ALL|wx.ALIGN_BOTTOM, 15 )
		
		self.slider32 = wx.Slider( self.panel3, wx.ID_ANY, 1, 1, 20, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_LABELS )
		bSizer7.Add( self.slider32, 1, wx.ALL|wx.ALIGN_BOTTOM, 0 )
		
		self.slider_label33 = wx.StaticText( self.panel3, wx.ID_ANY, u"wavelength(nm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.slider_label33.Wrap( -1 )
		bSizer7.Add( self.slider_label33, 0, wx.ALL|wx.ALIGN_BOTTOM, 15 )
		
		self.slider33 = wx.Slider( self.panel3, wx.ID_ANY, 632, 200, 800, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_LABELS )
		bSizer7.Add( self.slider33, 1, wx.ALL|wx.ALIGN_BOTTOM, 0 )
		
		self.slider_label34 = wx.StaticText( self.panel3, wx.ID_ANY, u"screen distance(cm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.slider_label34.Wrap( -1 )
		bSizer7.Add( self.slider_label34, 0, wx.ALL|wx.ALIGN_BOTTOM, 15 )
		
		self.slider34 = wx.Slider( self.panel3, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_LABELS )
		bSizer7.Add( self.slider34, 1, wx.ALL|wx.ALIGN_BOTTOM, 0 )
		
		
		self.panel3.SetSizer( bSizer7 )
		self.panel3.Layout()
		bSizer7.Fit( self.panel3 )
		self.notebook.AddPage( self.panel3, u"Multiple slit diffraction", False )
		
		bSizer3.Add( self.notebook, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		self.statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.menubar = wx.MenuBar( 0 )
		self.file = wx.Menu()
		self.save = wx.MenuItem( self.file, ID_SAVE, u"Save"+ u"\t" + u"Ctrl+X", u"Save graphics", wx.ITEM_NORMAL )
		self.file.AppendItem( self.save )
		
		self.quit = wx.MenuItem( self.file, ID_QUIT, u"Quit"+ u"\t" + u"Ctrl+q", u"Exit program!", wx.ITEM_NORMAL )
		self.file.AppendItem( self.quit )
		
		self.menubar.Append( self.file, u"File" ) 
		
		self.help = wx.Menu()
		self.about = wx.MenuItem( self.help, ID_ABOUT, u"About"+ u"\t" + u"Ctrl+h", u"about this program!", wx.ITEM_NORMAL )
		self.help.AppendItem( self.about )
		
		self.menubar.Append( self.help, u"Help" ) 
		
		self.SetMenuBar( self.menubar )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.slider11.Bind( wx.EVT_SCROLL, self.on_slider11 )
		self.slider12.Bind( wx.EVT_SCROLL, self.on_slider12 )
		self.slider13.Bind( wx.EVT_SCROLL, self.on_slider13 )
		self.slider21.Bind( wx.EVT_SCROLL, self.on_slider21 )
		self.slider22.Bind( wx.EVT_SCROLL, self.on_slider22 )
		self.slider23.Bind( wx.EVT_SCROLL, self.on_slider23 )
		self.slider24.Bind( wx.EVT_SCROLL, self.on_slider24 )
		self.slider31.Bind( wx.EVT_SCROLL, self.on_slider31 )
		self.slider32.Bind( wx.EVT_SCROLL, self.on_slider32 )
		self.slider33.Bind( wx.EVT_SCROLL, self.on_slider33 )
		self.slider34.Bind( wx.EVT_SCROLL, self.on_slider34 )
		self.Bind( wx.EVT_MENU, self.on_save, id = self.save.GetId() )
		self.Bind( wx.EVT_MENU, self.on_exit, id = self.quit.GetId() )
		self.Bind( wx.EVT_MENU, self.on_about, id = self.about.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_slider11( self, event ):
		event.Skip()
	
	def on_slider12( self, event ):
		event.Skip()
	
	def on_slider13( self, event ):
		event.Skip()
	
	def on_slider21( self, event ):
		event.Skip()
	
	def on_slider22( self, event ):
		event.Skip()
	
	def on_slider23( self, event ):
		event.Skip()
	
	def on_slider24( self, event ):
		event.Skip()
	
	def on_slider31( self, event ):
		event.Skip()
	
	def on_slider32( self, event ):
		event.Skip()
	
	def on_slider33( self, event ):
		event.Skip()
	
	def on_slider34( self, event ):
		event.Skip()
	
	def on_save( self, event ):
		event.Skip()
	
	def on_exit( self, event ):
		event.Skip()
	
	def on_about( self, event ):
		event.Skip()
	


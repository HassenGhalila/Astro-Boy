#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 20:23:23 2014

###############################################################################
#                                                                             #
#    Laboratoire de Spectroscopie Atomique, Moléculaire et Applications       #
#                               (L.S.A.M.A)                                   #
#      Faculté de Science de Tunis – Université de Tunis El Manar             #
#            @author: Ahmed Ammar - ammarahmed.ph@gmail.com                   #
#                                                                             #
###############################################################################

"""
import numpy as np
import wx
from wx.lib.wordwrap import wordwrap
import gui
import os
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import \
    FigureCanvasWxAgg as FigCanvas, \
    NavigationToolbar2WxAgg as NavigationToolbar

from matplotlib import style
#style.use('dark_background')
style.use('ggplot')

from matplotlib import rc
#    
#import matplotlib
#matplotlib.use("WxAgg")
#from numpy import arange, sin, pi, cos, log
#from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
#from matplotlib.backends.backend_wx import NavigationToolbar2Wx
#from matplotlib.figure import Figure
#import wx  
#IS_GTK = 'wxGTK' in wx.PlatformInfo
#IS_WIN = 'wxMSW' in wx.PlatformInfo
#IS_MAC = 'wxMac' in wx.PlatformInfo
    
    
class Diffraction(gui.MainFrame):

    def __init__(self, parent):
        gui.MainFrame.__init__(self, parent)
        #SPLSH 
        img = wx.Bitmap("splash.png", wx.BITMAP_TYPE_PNG)
        wx.SplashScreen(img, wx.SPLASH_CENTRE_ON_SCREEN|wx.SPLASH_TIMEOUT, 5000, None, -1)
        # Icon
        try:
            self.SetIcon(wx.Icon("logo.ico", wx.BITMAP_TYPE_ICO))
        finally:
            pass

        self.main_panel()
        self.draw_figure1()
        self.draw_figure2()
        self.draw_figure3()

# ---------------------------------------------------------------------------------------
    def main_panel(self):

# PANEL 1 ----------------

        self.fig1 = Figure()


        self.canvas1 = FigCanvas(self.panel1,-1, self.fig1)
        self.axes1 = self.fig1.add_subplot(111)
        
        # Create the navigation toolbar, tied to the canvas
        self.toolbar1 = NavigationToolbar(self.canvas1)
        #
        # Layout with box sizers
        #
        self.vbox1 = wx.BoxSizer(wx.VERTICAL)
        self.vbox1.Add(self.canvas1, 1, wx.TOP | wx.LEFT | wx.GROW)
        #add navigation toolbar at the botum of the canvas!
        self.vbox1.AddSpacer(5)
        self.vbox1.Add(self.toolbar1, 0, wx.EXPAND)
        self.vbox1.AddSpacer(5)
        # button txtbox and slider should be in a horizontal box!
        self.hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        flags = wx.ALIGN_LEFT | wx.ALL | wx.ALIGN_CENTER_VERTICAL
        self.hbox1.Add(self.slider_label11, 0, flag=flags)
        self.hbox1.Add(self.slider11, 0, border=3, flag=flags)
        self.hbox1.AddSpacer(30)
        self.hbox1.Add(self.slider_label12, 0, flag=flags)
        self.hbox1.Add(self.slider12, 0, border=3, flag=flags)
        self.hbox1.AddSpacer(30)
        self.hbox1.Add(self.slider_label13, 0, flag=flags)
        self.hbox1.Add(self.slider13, 0, border=3, flag=flags)
        # Add hbox to vbox! so textbox, button and sliders shows at the right place!
        self.vbox1.Add(self.hbox1, 0, flag = wx.ALIGN_LEFT | wx.TOP)

        # Set the box sizers in the panel
        self.panel1.SetSizer(self.vbox1)
        self.vbox1.Fit(self)

# PANEL 2 ----------------

        self.fig2 = Figure()
        self.canvas2 = FigCanvas(self.panel2, -1, self.fig2)
        self.axes2 = self.fig2.add_subplot(111)
        self.toolbar2 = NavigationToolbar(self.canvas2)

        self.vbox2 = wx.BoxSizer(wx.VERTICAL)
        self.vbox2.Add(self.canvas2, 1, wx.TOP | wx.LEFT | wx.GROW)
        #add navigation toolbar at the botum of the canvas!
        self.vbox2.AddSpacer(5)
        self.vbox2.Add(self.toolbar2, 0, wx.EXPAND)
        self.vbox2.AddSpacer(5)
        # button txtbox and slider should be in a horizontal box!
        self.hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        flags = wx.ALIGN_LEFT | wx.ALL | wx.ALIGN_CENTER_VERTICAL
        self.hbox2.Add(self.slider_label21, 0, flag=flags)
        self.hbox2.Add(self.slider21, 0, border=3, flag=flags)
        self.hbox2.AddSpacer(30)
        self.hbox2.Add(self.slider_label22, 0, flag=flags)
        self.hbox2.Add(self.slider22, 0, border=3, flag=flags)
        self.hbox2.AddSpacer(30)
        self.hbox2.Add(self.slider_label23, 0, flag=flags)
        self.hbox2.Add(self.slider23, 0, border=3, flag=flags)
        self.hbox2.AddSpacer(30)
        self.hbox2.Add(self.slider_label24, 0, flag=flags)
        self.hbox2.Add(self.slider24, 0, border=3, flag=flags)
        # Add hbox to vbox! so textbox, button and sliders shows at the right place!
        self.vbox2.Add(self.hbox2, 0, flag = wx.ALIGN_LEFT | wx.TOP)

        # Set the box sizers in the panel
        self.panel2.SetSizer(self.vbox2)
        self.vbox2.Fit(self)
# PANEL 3 ----------------

        self.fig3 = Figure()
        self.canvas3 = FigCanvas(self.panel3, -1, self.fig3)
        self.axes3 = self.fig3.add_subplot(111)
        self.toolbar3 = NavigationToolbar(self.canvas3)

        self.vbox3 = wx.BoxSizer(wx.VERTICAL)

        self.vbox3.Add(self.canvas3, 1, wx.TOP | wx.LEFT | wx.GROW)
        #add navigation toolbar at the botum of the canvas!
        self.vbox3.AddSpacer(6)
        self.vbox3.Add(self.toolbar3, 0, wx.EXPAND)
        self.vbox3.AddSpacer(5)
        # button txtbox and slider should be in a horizontal box!
        self.hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        flags = wx.ALIGN_LEFT | wx.ALL | wx.ALIGN_CENTER_VERTICAL
        self.hbox3.Add(self.slider_label31, 0, flag=flags)
        self.hbox3.Add(self.slider31, 0, border=3, flag=flags)
        self.hbox3.AddSpacer(30)
        self.hbox3.Add(self.slider_label32, 0, flag=flags)
        self.hbox3.Add(self.slider32, 0, border=3, flag=flags)
        self.hbox3.AddSpacer(30)
        self.hbox3.Add(self.slider_label33, 0, flag=flags)
        self.hbox3.Add(self.slider33, 0, border=3, flag=flags)
        self.hbox3.AddSpacer(30)
        self.hbox3.Add(self.slider_label34, 0, flag=flags)
        self.hbox3.Add(self.slider34, 0, border=3, flag=flags)
        self.hbox3.AddSpacer(6)
        # Add hbox to vbox! so textbox, button and sliders shows at the right place!
        self.vbox3.Add(self.hbox3, 0, flag = wx.ALIGN_LEFT | wx.TOP)

        # Set the box sizers in the panel
        self.panel3.SetSizer(self.vbox3)
        self.vbox3.Fit(self)

#    End of def main_panel(self):
# ---------------------------------------------------------------------------------------



    def draw_figure1(self):
        """ Redraws the figure
        """
        sb=self.slider11.GetValue()
        slamda=self.slider12.GetValue()
        sD=self.slider13.GetValue()

        npoint = 601
        b = sb * 1.E-06
        lamda= slamda * 1.E-09
        D= sD * 1.E-02

        thetamin1= -np.pi/200
        thetamax1= np.pi/200
        pas =( thetamax1-thetamin1)/npoint

        Theta1=[]


        for i in range(npoint):
            T1 = thetamin1 + i * pas
            Theta1.append(T1)

            U1 = np.pi * b * np.sin(Theta1)/lamda
            Amplitude= np.sin(U1) / U1
            Intens_1f=Amplitude**2
            U1=Theta1*np.array(D)       
#            U1=np.tan(Theta1)*np.array(D)       

#        print Theta1*np.array(D)       
#        print np.tan(Theta1)*np.array(D)       
        self.axes1.clear()
        if 200*1.E-09<=lamda <= 380*1.E-09:
            self.axes1.plot(U1, Intens_1f,linestyle=':', color='violet')
        if 380*1.E-09<=lamda <= 430*1.E-09:
            self.axes1.plot(U1, Intens_1f,linestyle='-', color='purple')
        elif 430*1.E-09< lamda <= 450*1.E-09:
            self.axes1.plot(U1, Intens_1f,linestyle='-', color='darkblue')
        elif 450*1.E-09< lamda <= 500*1.E-09:
            self.axes1.plot(U1, Intens_1f,linestyle='-', color='blue')
        elif 500*1.E-09< lamda <= 520*1.E-09:
            self.axes1.plot(U1, Intens_1f,linestyle='-', color='cyan')
        elif 520*1.E-09< lamda <= 565*1.E-09:
            self.axes1.plot(U1, Intens_1f,linestyle='-', color='lime')
        elif 565*1.E-09< lamda <= 590*1.E-09:
            self.axes1.plot(U1, Intens_1f,linestyle='-', color='yellow')
        elif 590*1.E-09< lamda <= 625*1.E-09:
            self.axes1.plot(U1, Intens_1f,linestyle='-', color='orange')
        elif 625*1.E-09< lamda <= 740*1.E-09:
            self.axes1.plot(U1, Intens_1f,linestyle='-', color='red')
        elif 740*1.E-09< lamda <= 800*1.E-09:
            self.axes1.plot(U1, Intens_1f,linestyle=':', color='tomato')

        else:
            self.axes1.plot(U1, Intens_1f, linestyle=':', color='gray')

        self.axes1.set_title("Diffraction of monochromatic light by one single slit",
                           ha='center', color='k',fontsize=16)
        self.axes1.set_xlabel('x(m)')
        self.axes1.set_ylabel('Intensity')

#        rc('text', usetex = True)
#        self.axes1.annotate(r'$\frac{I(\theta)}{I(0)}= [ \frac{\sin(\frac{\pi b}'
#        r'{\lambda} \frac{x}{D})}{\frac{\pi b}{\lambda} \frac{x}{D}} ]^2$'
#        u'\n  $b = %.1f \mu m $ \n $\lambda = %.1f nm$'
#        u'\n $D =%.1f cm $'% (sb, slamda, sD) ,
#        xy=(0, 0.5),  xycoords='data',
#        xytext=(-400, 5),size=14,color='black', family='fantasy', textcoords='offset points',
#        bbox=dict(boxstyle="round", fc="0.9"))

        self.axes1.annotate(r'$\frac{I(\theta)}{I(0)}= [ \frac{\sin(\frac{\pi b}'
        r'{\lambda} \frac{x}{D})}{\frac{\pi b}{\lambda} \frac{x}{D}} ]^2$',
        xy=(0, 0.5),  xycoords='data',
        xytext=(-300, 100),size=20,color='black',fontweight='bold', family='fantasy', textcoords='offset points',
        bbox=dict(boxstyle="round", fc="0.9"))
        self.axes1.annotate(r' $b = %.1f \mu m $' % (sb),
        xy=(0, 0.5),  xycoords='data',
        xytext=(-300, 55),size=14,color='black', fontweight='500', family='fantasy', textcoords='offset points',
        bbox=dict(boxstyle="round", fc="0.9"))
        self.axes1.annotate(r' $\lambda = %.1f nm$'% (slamda) ,
        xy=(0, 0.5),  xycoords='data',
        xytext=(-300, 30),size=14,color='black', family='fantasy', textcoords='offset points',
        bbox=dict(boxstyle="round", fc="0.9"))
        self.axes1.annotate(r' $D =%.1f cm $'% (sD) ,
        xy=(0, 0.5),  xycoords='data',
        xytext=(-300, 5),size=14,color='black', family='fantasy', textcoords='offset points',
        bbox=dict(boxstyle="round", fc="0.9"))
        
#        self.axes1.annotate(r'$\theta = \frac{I(\theta)}{I(0)}$',xy=(0, 0.5),xycoords='data',
#                xytext=(-300, 25),size=18,color='teal', family='fantasy', textcoords='offset points',
#                bbox=dict(boxstyle="round", fc="0.9"))

        self.canvas1.draw()

# End of draw_figure1
# ---------------------------------------------------------------------------------------

    def draw_figure2(self):
        sb=self.slider21.GetValue()
        sa=self.slider22.GetValue()
        slamda=self.slider23.GetValue()
        sD=self.slider24.GetValue()

        npoint=601
        b= sb* 1.E-06
        a= sa* 1.E-03
        lamda=slamda * 1.E-09
        D= sD * 1.E-02
        thetamin2=-np.pi/self.slider21.GetValue()
        thetamax2=np.pi/self.slider21.GetValue()
        pas=(thetamax2-thetamin2)/npoint
        Theta2=[]
        for i in range(npoint):
            T2 = thetamin2 + i * pas
            Theta2.append(T2)
            U2=np.pi*b*np.sin(Theta2)/lamda
            v=np.pi*a*np.sin(Theta2)/lamda
            Amplitude= np.sin(U2)/U2
            Intens_2f_1= Amplitude**2
            Amplitude = (np.sin(U2)/U2)*(np.cos(v))/2
            Intens_2f= 4*Amplitude**2
            U2=Theta2*np.array(D)
        Tachecentraldiff2=(2*np.array(D)*lamda)/b
        Tachecentralinter2=lamda*np.array(D)/a

        self.axes2.clear()
        if 200*1.E-09<=lamda <= 380*1.E-09:
            self.axes2.plot(U2, Intens_2f,linestyle=':', color='violet')
        if 380*1.E-09<=lamda <= 430*1.E-09:
            self.axes2.plot(U2, Intens_2f,linestyle='-', color='purple')
        elif 430*1.E-09< lamda <= 450*1.E-09:
            self.axes2.plot(U2, Intens_2f,linestyle='-', color='darkblue')
        elif 450*1.E-09< lamda <= 500*1.E-09:
            self.axes2.plot(U2, Intens_2f,linestyle='-', color='blue')
        elif 500*1.E-09< lamda <= 520*1.E-09:
            self.axes2.plot(U2, Intens_2f,linestyle='-', color='cyan')
        elif 520*1.E-09< lamda <= 565*1.E-09:
            self.axes2.plot(U2, Intens_2f,linestyle='-', color='lime')
        elif 565*1.E-09< lamda <= 590*1.E-09:
            self.axes2.plot(U2, Intens_2f,linestyle='-', color='yellow')
        elif 590*1.E-09< lamda <= 625*1.E-09:
            self.axes2.plot(U2, Intens_2f,linestyle='-', color='orange')
        elif 625*1.E-09< lamda <= 740*1.E-09:
            self.axes2.plot(U2, Intens_2f,linestyle='-', color='red')
        elif 740*1.E-09< lamda <= 800*1.E-09:
            self.axes2.plot(U2, Intens_2f,linestyle=':', color='tomato')

        else:
            self.axes2.plot(U2, Intens_2f, linestyle=':', color='gray')
        self.axes2.plot(U2, Intens_2f_1,linestyle='--', color='gray')

        self.axes2.set_title('Diffraction of monochromatic light by double slit',
                           ha='center', color='k',fontsize=16)
        self.axes2.set_xlabel('x(m)')
        self.axes2.set_ylabel('Intensity')

##        rc('text', usetex = True)
##        self.axes2.annotate(r'$\frac{I(\theta)}{I(0)}= 4 \/[ \frac{\sin(\frac{\pi b}'
##                            r'{\lambda} \frac{x}{D})}{\frac{\pi b}{\lambda} \frac{x}{D}} ]^2$'
##                            r'$[\cos(\frac{\pi a}{\lambda} \frac{x}{D})]^2$'
##                            r'\newline $b = %.1f \mu m $\newline \newline $a = %.1f mm $'
##                            r' \newline\newline $\lambda = %.1f nm$ \newline\newline $D =%.1f cm $'% (sb, sa, slamda, sD) ,
##                                     xy=(0, 0.5),  xycoords='data',
##                xytext=(-300, 25),size=18,color='teal', family='fantasy', textcoords='offset points',
##                bbox=dict(boxstyle="round", fc="0.9"))

        self.axes2.annotate(r'$\frac{I(\theta)}{I(0)}= 4 \/[ \frac{\sin(\frac{\pi b}'
        r'{\lambda} \frac{x}{D})}{\frac{\pi b}{\lambda} \frac{x}{D}} ]^2$'
        r'$[\cos(\frac{\pi a}{\lambda} \frac{x}{D})]^2$',
        xy=(0, 0.5),  xycoords='data',
        xytext=(-300, 100),size=20,color='black',fontweight='bold', family='fantasy', textcoords='offset points',
        bbox=dict(boxstyle="round", fc="0.9"))
        self.axes2.annotate(r' $b = %.1f \mu m$'% (sb), 
        xy=(0, 0.5),  xycoords='data',
        xytext=(-300, 55),size=14,color='black', fontweight='500', family='fantasy', textcoords='offset points',
        bbox=dict(boxstyle="round", fc="0.9"))                            
        self.axes2.annotate(r' $a = %.1f mm $'% (sa),
        xy=(0, 0.5),  xycoords='data',
        xytext=(-300, 30),size=14,color='black', family='fantasy', textcoords='offset points',
        bbox=dict(boxstyle="round", fc="0.9"))
        self.axes2.annotate(r' $\lambda = %.1f nm$'% (slamda), 
        xy=(0, 0.5),  xycoords='data',
        xytext=(-300, 5),size=14,color='black', family='fantasy', textcoords='offset points',
        bbox=dict(boxstyle="round", fc="0.9"))                           
        self.axes2.annotate(r' $D =%.1f cm $'% (sD),
        xy=(0, 0.5),  xycoords='data',
        xytext=(-300, -20),size=14,color='black', family='fantasy', textcoords='offset points',
        bbox=dict(boxstyle="round", fc="0.9"))

        self.canvas2.draw()
# End of draw_figure2
# ---------------------------------------------------------------------------------------

    def draw_figure3(self):
        sb=self.slider31.GetValue()
        sa=self.slider32.GetValue()
        slamda=self.slider33.GetValue()
        sD=self.slider34.GetValue()

        npoint=4801
        b=sb * 1.E-06
        a=sa*1.E-03
        lamda=slamda*1.E-09
        D=sD*1.E-02
        N=20
        thetaminN=-np.pi/self.slider31.GetValue()
        thetamaxN=np.pi/self.slider31.GetValue()

        pas=(thetamaxN-thetaminN)/npoint
        ThetaN=[]
        for i in range(npoint):
            TN = thetaminN + i * pas
            ThetaN.append(TN)

            UN = (np.pi*b*np.sin(ThetaN))/lamda
            v = (np.pi*a*np.sin(ThetaN))/lamda
            Amplitude= np.sin(UN)/UN
            Intens_Nf_1 = Amplitude**2
            Amplitude = ((np.sin(UN)/UN)*(np.sin(N*v))/(np.sin(v)))/N
            Intens_Nf = Amplitude**2
            UN=ThetaN*np.array(D)
            #

        self.axes3.clear()
        if 200*1.E-09<=lamda <= 380*1.E-09:
            self.axes3.plot(UN, Intens_Nf,linestyle=':', color='violet')
        if 380*1.E-09<=lamda <= 430*1.E-09:
            self.axes3.plot(UN, Intens_Nf,linestyle='-', color='purple')
        elif 430*1.E-09< lamda <= 450*1.E-09:
            self.axes3.plot(UN, Intens_Nf,linestyle='-', color='darkblue')
        elif 450*1.E-09< lamda <= 500*1.E-09:
            self.axes3.plot(UN, Intens_Nf,linestyle='-', color='blue')
        elif 500*1.E-09< lamda <= 520*1.E-09:
            self.axes3.plot(UN, Intens_Nf,linestyle='-', color='cyan')
        elif 520*1.E-09< lamda <= 565*1.E-09:
            self.axes3.plot(UN, Intens_Nf,linestyle='-', color='lime')
        elif 565*1.E-09< lamda <= 590*1.E-09:
            self.axes3.plot(UN, Intens_Nf,linestyle='-', color='yellow')
        elif 590*1.E-09< lamda <= 625*1.E-09:
            self.axes3.plot(UN, Intens_Nf,linestyle='-', color='orange')
        elif 625*1.E-09< lamda <= 740*1.E-09:
            self.axes3.plot(UN, Intens_Nf,linestyle='-', color='red')
        elif 740*1.E-09< lamda <= 800*1.E-09:
            self.axes3.plot(UN, Intens_Nf,linestyle=':', color='tomato')

        else:
            self.axes3.plot(UN, Intens_Nf, linestyle=':', color='gray')
        self.axes3.plot(UN, Intens_Nf_1,linestyle='--', color='gray')
        self.axes3.set_title('Diffraction of monochromatic light by %d slits'% N,
                           ha='center', color='k',fontsize=16)
        self.axes3.set_xlabel('x(m)')
        self.axes3.set_ylabel('Intensity')

##        rc('text', usetex = True)
##        self.axes3.annotate(r'$\frac{I(\theta)}{I(0)}= [ \frac{\sin(\frac{\pi b}'
##                            r'{\lambda} \frac{x}{D})}{\frac{\pi b}{\lambda} \frac{x}{D}} ]^2$'
##                            r'$[\frac{\sin(N\frac{\pi a}{\lambda} \frac{x}{D})}{N\sin(\frac{\pi a}'
##                            r'{\lambda} \frac{x}{D})}]^2$'
##                            r'\newline $b = %.1f \mu m $ \newline \newline $a = %.1f mm $'
##                            r' \newline \newline $\lambda = %.1f nm$ \newline \newline $D =%.1f cm $'% (sb, sa, slamda, sD) ,
##                                     xy=(0, 0.5),  xycoords='data',
##                xytext=(-300, 25),size=18,color='teal', family='fantasy', textcoords='offset points',
##                bbox=dict(boxstyle="round", fc="0.9"))

        self.axes3.annotate(r'$\frac{I(\theta)}{I(0)}= [ \frac{\sin(\frac{\pi b}'
        r'{\lambda} \frac{x}{D})}{\frac{\pi b}{\lambda} \frac{x}{D}} ]^2$'
        r'$[\frac{\sin(N\frac{\pi a}{\lambda} \frac{x}{D})}{N\sin(\frac{\pi a}'
        r'{\lambda} \frac{x}{D})}]^2$',
        xy=(0, 0.5),  xycoords='data',
        xytext=(-300, 100),size=20,color='black',fontweight='bold', family='fantasy', textcoords='offset points',
        bbox=dict(boxstyle="round", fc="0.9"))
        self.axes3.annotate(r' $b = %.1f \mu m$'% (sb), 
        xy=(0, 0.5),  xycoords='data',
        xytext=(-300, 55),size=14,color='black', fontweight='500', family='fantasy', textcoords='offset points',
        bbox=dict(boxstyle="round", fc="0.9"))                            
        self.axes3.annotate(r' $a = %.1f mm $'% (sa),
        xy=(0, 0.5),  xycoords='data',
        xytext=(-300, 30),size=14,color='black', family='fantasy', textcoords='offset points',
        bbox=dict(boxstyle="round", fc="0.9"))
        self.axes3.annotate(r' $\lambda = %.1f nm$'% (slamda), 
        xy=(0, 0.5),  xycoords='data',
        xytext=(-300, 5),size=14,color='black', family='fantasy', textcoords='offset points',
        bbox=dict(boxstyle="round", fc="0.9"))                           
        self.axes3.annotate(r' $D =%.1f cm $'% (sD),
        xy=(0, 0.5),  xycoords='data',
        xytext=(-300, -20),size=14,color='black', family='fantasy', textcoords='offset points',
        bbox=dict(boxstyle="round", fc="0.9"))
        self.canvas3.draw()

# End of draw_figure3
# ---------------------------------------------------------------------------------------

    def on_slider11(self, event):   # Slider 1 for figure 1 (1 slit)
        self.draw_figure1()

    def on_slider12(self, event):   # Slider 2 for figure 1 (1 slit)
        self.draw_figure1()

    def on_slider13(self, event):    # Slider 3 for figure 1 (1 slit)
        self.draw_figure1()

    def on_slider21(self, event):   # Slider 1 for figure 2 (1 slit)
        self.draw_figure2()

    def on_slider22(self, event):   # Slider 2 for figure 2 (1 slit)
        self.draw_figure2()

    def on_slider23(self, event):   # Slider 3 for figure 2 (1 slit)
        self.draw_figure2()

    def on_slider24(self, event):   # ...
        self.draw_figure2()

    def on_slider31(self, event):   # ...
        self.draw_figure3()

    def on_slider32(self, event):   # ...
        self.draw_figure3()

    def on_slider33(self, event):   # ...
        self.draw_figure3()

    def on_slider34(self, event):   # Slider 4 for figure 3 (1 slit)
        self.draw_figure3()

    def on_save(self, event):               # Fonction de menus
#        file_choices = "PNG (*.png)|*.png"
        file_choices = "EPS (*.eps)|*.eps"

        dlg = wx.FileDialog(
            self,
            message="Save plot as...",
            defaultDir=os.getcwd(),
#            defaultFile="Diffraction.eps",
#             "The items in the basket are %s and %s" % (x,y)
            defaultFile="Diff_ %1.1f .eps" % self.slider23.GetValue(),
            wildcard=file_choices,
            style=wx.SAVE)

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.canvas1.print_figure(path)

    def on_exit(self, event):           
        self.Destroy()

    def on_about(self, event):
        # First we create and fill the info object
        info = wx.AboutDialogInfo()
        info.Name = "Fraunhofer"
        info.Version = "0.1"
        info.Copyright = "(C) 2015  A.A Physics simulations\n Tunis - Tunisia"
        info.Description = wordwrap(
        '''The Franhofer simulator is a software program for the use of teachers and students in Optics class\n
        \nSuch a program is typically one of the simplest programs possible "in a computer language.''',
            350, wx.ClientDC(self))
        
        info.Developers = [ "Ahmed Ammar" ]
        info.WebSite = ("ammarahmed.ph@gmail.com")
        # Then we call wx.AboutBox giving it that info object
        wx.AboutBox(info)
        
if __name__ == '__main__':
#    app = wx.PySimpleApp()
    app = wx.App()
    app.frame=Diffraction(None)
    app.frame.Show(True)
    provider = wx.CreateFileTipProvider("tips.txt", 0)
    wx.ShowTip(None, provider, True)
    app.MainLoop()

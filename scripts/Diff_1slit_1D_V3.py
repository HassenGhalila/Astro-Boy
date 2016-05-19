#!/usr/bin/env python

from __future__ import division
from numpy import pi, linspace,sin
import matplotlib.pyplot as plt

def Diff_1S(lamda=600,b=0.1*1.E-3,D = 1):
    
    a= 10 * 1.E-2
    k=(2.*pi)/(1.E-9*lamda)  #wavelength of light in vaccuum
    X_Mmax=a/2. ; X_Mmin = -a/2.; Y_Mmin = X_Mmin
    N =400
    X=linspace(X_Mmin, X_Mmax,N); Y=X # coordinates of screen
    
    B=(k*b*X)/(2.*D) # intermediate variable
    
    I=(sin(B)/B)**2
    
    fig = plt.figure(figsize=(7, 5))
    fig.suptitle('Fraunhofer Diffraction by one slit',fontsize=14, fontweight='bold')
    
    ax1 = fig.add_subplot(111)
    ax1.grid(True)
    
    if 200<=lamda <= 380:
        ax1.plot(X, I,linestyle=':', color='violet', linewidth=2.5, alpha=0.8)
    if 380<=lamda <= 430:
        ax1.plot(X, I,linestyle='-', color='purple', linewidth=2.5, alpha=0.8)
    elif 430< lamda <= 450:
        ax1.plot(X, I,linestyle='-', color='darkblue', linewidth=2.5, alpha=0.8)
    elif 450< lamda <= 500:
        ax1.plot(X, I,linestyle='-', color='blue', linewidth=2.5, alpha=0.8)
    elif 500< lamda <= 520:
        ax1.plot(X, I,linestyle='-', color='cyan', linewidth=2.5, alpha=0.8)
    elif 520< lamda <= 565:
        ax1.plot(X, I,linestyle='-', color='lime', linewidth=2.5, alpha=0.8)
    elif 565< lamda <= 590:
        ax1.plot(X, I,linestyle='-', color='yellow', linewidth=2.5, alpha=0.8)
    elif 590< lamda <= 625:
        ax1.plot(X, I,linestyle='-', color='orange', linewidth=2.5, alpha=0.8)
    elif 625< lamda <= 740:
        ax1.plot(X, I,linestyle='-', color='red', linewidth=2.5, alpha=0.8)
    elif 740< lamda <= 800:
        ax1.plot(X, I,linestyle=':', color='tomato', linewidth=2.5, alpha=0.8) 
    else:
        ax1.plot(X, I, linestyle=':', color='gray', linewidth=2.5, alpha=0.8)
    ax1.set_xlim(X_Mmin, X_Mmax)
    ax1.set_xlabel(r'$X \ (m)$',fontsize=14, fontweight='bold')
    ax1.set_ylabel(r'$I(X,Y)/I_0$',fontsize=14, fontweight='bold')
    
    ax1.set_title(r"$wavelength \ \lambda = %.0d \ nm, \ b = %s \ m$"% (lamda,b),fontsize=14)
    plt.show()
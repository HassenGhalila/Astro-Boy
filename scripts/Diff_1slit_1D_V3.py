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
    ax1.plot(X,I, linewidth=2, alpha=0.8)
    ax1.set_xlim(X_Mmin, X_Mmax)
    ax1.set_xlabel(r'$X \ (m)$',fontsize=14, fontweight='bold')
    ax1.set_ylabel(r'$I(X,Y)/I_0$',fontsize=14, fontweight='bold')
    
    ax1.set_title(r"$wavelength \ \lambda = %.0d \ nm, \ b = %s \ m$"% (lamda,b),fontsize=14)
    plt.show()

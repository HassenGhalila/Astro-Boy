#!/usr/bin/env python

from __future__ import division
from numpy import pi, linspace,meshgrid,sin
import matplotlib.pyplot as plt
import matplotlib.cm as cm
def Diff_1S(lamda=600,b=0.1*1.E-3,D = 1):
	
    a= 10 * 1.E-2    
    k=(2.*pi)/(lamda*1.E-9)  #wavelength of light in vaccuum
    
    X_Mmax=a/2. ; X_Mmin = -a/2.; Y_Mmin = X_Mmin; Y_Mmax=X_Mmax
    N =400
    X=linspace(X_Mmin, X_Mmax,N); Y=X # coordinates of screen
    
    B=(k*b*X)/(2.*D) # intermediate variable
    
    XX, YY =meshgrid(B,B)
    I=(sin(XX)/XX)**2
    
    fig = plt.figure(figsize=(5, 5))
    fig.suptitle('Fraunhofer Diffraction by one slit',fontsize=14, fontweight='bold')
    
    ax1 = fig.add_subplot(111)
    
    ax1.imshow(I, cmap=cm.copper, interpolation='bilinear',
              origin='lower',vmin=I.min(), vmax= 0.01*I.max())
    
    ax1.set_xticks([0, N/2, N]); ax1.set_xticklabels([-X_Mmax, 0, X_Mmax])
    ax1.set_yticks([0, N/2, N]); ax1.set_yticklabels([-Y_Mmax, 0, Y_Mmax])
    
    ax1.set_xlabel(r'$X \ (m)$',fontsize=14, fontweight='bold')
    ax1.set_ylabel(r'$Y \ (m)$',fontsize=14, fontweight='bold')
    
    ax1.set_title(r"$wavelength \ \lambda = %.0d \ nm, \ b = %s \ m $"% (lamda,b),fontsize=14)
    
    
    plt.show()

#!/usr/bin/env python
from __future__ import division
from numpy import pi, linspace,meshgrid
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import scipy.special as ss
from mpl_toolkits.mplot3d import axes3d

def Rayleigh_2d(lamda=600,r=0.1*1.E-3,d= 5*1.E-3,D = 2):
	
    a= 10 * 1.E-2
    k=(2.*pi)/(lamda *1.E-9) #wavelength of light in vaccuum
    
    X_Mmax=a/2. ; X_Mmin = -a/2.; Y_Mmin = X_Mmin; Y_Mmax=X_Mmax
    N =400
    X=linspace(X_Mmin, X_Mmax,N); Y=X # coordinates of screen
    
    XX, YY =meshgrid(X, Y)
    rm1=((XX-d)**2+YY**2)**0.5
    A1=k*r*rm1/D
    I1=(ss.jv(1,A1)/A1)**2
    
    rm2=((XX+d)**2+YY**2)**0.5
    A2=k*r*rm2/D
    I2=(ss.jv(1,A2)/A2)**2
    
    I=I1 + I2
    
    fig = plt.figure(figsize=(5, 5))
    
    ax1 = fig.add_subplot(111)
    ax1.imshow(I, cmap=cm.copper, interpolation='bilinear',
              origin='lower',vmin=I.min(), vmax=0.01 * I.max())
    
    ax1.set_xticks([0, N/2, N]); ax1.set_xticklabels([-X_Mmax, 0, X_Mmax]) 
    ax1.set_yticks([0, N/2, N]); ax1.set_yticklabels([-Y_Mmax, 0, Y_Mmax])
    ax1.set_title('Fraunhofer Diffraction of circular aperture',fontsize=16)
    
    #fig 3D
    #ax2 = fig.add_subplot(122, projection='3d')
    #ax2.plot_surface( XX, YY,I, rstride=15, cstride=15, cmap=cm.copper, alpha=0.4)
    #ax2.set_zlim3d(0, I.max())
    
    #ax2.set_xlabel(r'$X \ (10^{-2} \ m)$',fontsize=14, fontweight='bold')
    #ax2.set_ylabel(r'$Y \ (10^{-2} \ m)$',fontsize=14, fontweight='bold')
    #ax2.set_zlabel(r'$I(Y, Y)/I_0$',fontsize=14, fontweight='bold')
    #ax2.set_title('Fraunhofer Diffraction of circular aperture',fontsize=16)
    
    plt.show()

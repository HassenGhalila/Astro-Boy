#!/usr/bin/env python
from __future__ import division
from numpy import pi, linspace,meshgrid
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import scipy.special as ss
from mpl_toolkits.mplot3d import axes3d
def Rayleigh_1d(lamda=600,r=0.1*1.E-3,d= 5*1.E-3,D = 2):
	
    a= 10 * 1.E-2
    k=(2.*pi)/(lamda*1.E-9)  #wavelength of light in vaccuum
    
    X_Mmax=a/2. ; X_Mmin = -a/2.; Y_Mmin = X_Mmin; Y_Mmax=X_Mmax
    N =400
    X=linspace(X_Mmin, X_Mmax,N); Y=X # coordinates of screen
    
    rm1=((X-d)**2+Y**2)**0.5
    A1=k*r*rm1/D
    
    I1=(ss.jv(1,A1)/A1)**2
    
    rm2=((X+d)**2+Y**2)**0.5
    A2=k*r*rm2/D
    I2=(ss.jv(1,A2)/A2)**2
    
    I=I1 + I2
    
    fig = plt.figure(figsize=(10,5))
    fig.suptitle('Fraunhofer Diffraction by circular aperture',fontsize=14, fontweight='bold')
    
    ax1 = fig.add_subplot(111)
    ax1.grid(True)
    ax1.plot(X,I1, linewidth=2, alpha=0.8, label="I1")
    ax1.plot(X,I2, linewidth=2, alpha=0.8, label="I2")
    ax1.plot(X,I, linewidth=2, alpha=0.8, label="I = I1 + I2")
    ax1.set_xlim(X_Mmin, X_Mmax)
    ax1.set_xlabel(r'$X \ (m)$',fontsize=14, fontweight='bold')
    ax1.set_ylabel(r'$I(X,Y)/I_0$',fontsize=14, fontweight='bold')
    plt.legend()
    plt.show()

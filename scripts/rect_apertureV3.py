#!/usr/bin/env python

from __future__ import division
from numpy import pi, linspace,meshgrid,sin
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import axes3d

def rect_apert(lamda=600,b=0.1*1.E-3,h=0.1*1.E-3, D = 1):
    
    a= 10 * 1.E-2
    k=(2.*pi)/(lamda*1.E-9)  #wavelength of light in vaccuum
    
    X_Mmax=a/2. ; X_Mmin = -a/2.
    Y_Mmax = X_Mmax ; Y_Mmin = X_Mmin
    N =400
    X=linspace(X_Mmin, X_Mmax,N); Y=X # coordinates of screen
    
    B=(k*b*X)/(2.*D); H=(k*h*Y)/(2.*D) # intermediate variable
    
    #2D
    BB, HH =meshgrid(B,H)
    I=(sin(BB)/BB)**2 * (sin(HH)/HH) **2
    
    fig = plt.figure(figsize=(15, 5))
    fig.suptitle('Fraunhofer Diffraction of rectangular aperture',fontsize=14, fontweight='bold')
    
    ax1 = fig.add_subplot(121)
    ax1.imshow(I, cmap=cm.copper, interpolation='bilinear',
              origin='lower',vmin=I.min(), vmax= 0.01*I.max())
    
    ax1.set_xticks([0, N/2, N]); ax1.set_xticklabels([-X_Mmax, 0, X_Mmax])
    ax1.set_yticks([0, N/2, N]); ax1.set_yticklabels([-Y_Mmax, 0, Y_Mmax])
    
    ax1.set_xlabel(r'$X \ (m)$',fontsize=14, fontweight='bold')
    ax1.set_ylabel(r'$Y \ (m)$',fontsize=14, fontweight='bold')
    
    ax1.set_title(r"$wavelength \ \lambda = % .0d \ nm, \ b = %s \ m, \ h = %s \ m $"% (lamda,b, h),fontsize=14)
    
    #3D
    
    ax2 = fig.add_subplot(122, projection='3d')
    ax2.plot_surface(BB, HH ,I , rstride=10, cstride=10, cmap=cm.copper, alpha=0.5)
    ##ax2.contour(BB, HH ,I, zdir='x', offset=100 * X_Mmin, cmap=cm.Oranges)
    ##ax2.contour(BB, HH ,I, zdir='y', offset=100 * Y_Mmax, cmap=cm.Oranges)
    ##ax2.contourf(BB, HH ,I, zdir='x', offset=100 * X_Mmin, cmap=cm.Blues, alpha=0.5)
    ##ax2.contourf(BB, HH ,I, zdir='y', offset=100 * Y_Mmax, cmap=cm.Blues, alpha=0.5)
    ax2.set_zlim3d(0, 1)
    
    #ax2.set_xticks([]); ax2.set_yticks([])
    ax2.set_xlabel(r'$X \ (10^{-2} \ m)$',fontsize=14, fontweight='bold')
    ax2.set_ylabel(r'$Y \ (10^{-2} \ m)$',fontsize=14, fontweight='bold')
    ax2.set_zlabel(r'$I(Y, Y)/I_0$',fontsize=14, fontweight='bold')
    ax2.set_title(r"$wavelength \ \lambda = % .0d \ nm , \ b = %s \ m, \ h = %s \ m $"% (lamda,b, h),fontsize=14)
    
    plt.show()

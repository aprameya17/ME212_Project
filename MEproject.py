import numpy as np;
import matplotlib.pyplot as plt;
 
class MohrsCircle():
     
    
    def __init__(self, sigmax, sigmay, tauxy):
        self.sigmax = sigmax;
        self.sigmay = sigmay;
        self.tauxy = tauxy; 'shear stress on x-face'
         
    def circleCenter(self):
        return (self.sigmax + self.sigmay)/2;
     
    def radius(self):
        a = (self.sigmax - self.sigmay)/2;
        b = self.tauxy
        return (a**2 + b**2)**(1/2);
     
    def maxPrincipalStress(self):
        return self.circleCenter() + self.radius();
     
    def minimumPrincipalStress(self):
        return self.circleCenter() - self.radius()
     
    def maximumShearStress(self):
        return self.radius()
     
    def mohrsCirclePlot(self):
        'Circle Points'
        radians = np.linspace(0, 360, 361)*(2*np.pi/360)
        sigmapts = self.circleCenter()+self.radius()*np.cos(radians)
        taupts = self.radius()*np.sin(radians)
         
        'Figure size and lines'
        plt.figure(figsize=[5,5])
        plt.plot(sigmapts, taupts, label = "Mohrs' Circle", color = 'k')
        plt.plot([self.sigmax, self.sigmay],[self.tauxy, -self.tauxy], color = 'b')
        plt.plot([self.circleCenter()],[0], marker = 'o', color = 'k')
         
        'Labels'
        plt.title("Mohr's Circle", fontsize = 18)
        plt.ylabel(r'$\tau$', fontsize = 14)
        plt.xlabel(r'$\sigma$', fontsize = 14)
         
        plt.axhline(color = 'k')
        plt.axvline(color = 'k')
         
        
        plt.fill_between(sigmapts, taupts, color = 'y', alpha = 0.1)
         
        
        plt.grid()
 
        
        plt.text(self.maxPrincipalStress(), 0, r'$\sigma_{max}$', va = 'bottom', ha = 'right', fontsize = 18)
        plt.text(self.minimumPrincipalStress(), 0, r'$\sigma_{min}$', ha = 'left', va = 'bottom', fontsize = 18)
        plt.text(self.circleCenter(), self.maximumShearStress(), r'$\tau_{max}$', va='top', ha = 'center', fontsize = 18)         
         
        
        plt.tight_layout()
        plt.show()

x=MohrsCircle(float(input("Enter the value of σx: ")),
float(input("Enter the value of σy: ")),
float(input("Enter the value of 𝜏xy: ")))
print("Centre of circle: "+str(x.circleCenter()))

print("Radius of circle: "+str(x.radius()))

print("Maximum principal stress: "+str(x.maxPrincipalStress()))

print("Minimum principal stress: "+str(x.minimumPrincipalStress()))

print("Maximum shear stress: "+str(x.maximumShearStress()))

x.mohrsCirclePlot()

import numpy as np
import sympy as sp

try:
    deltai_p=np.deg2rad((90-float(input('please input the inclination of the planent(deg) '))))
    deltai_b=np.deg2rad((90-float(input('please input the inclination of the binary star(deg) '))))
    a_p=float(input('please input the semi axis(a) of planet(AU) '))
    e_p=float(input('please input the eccentric(e) of the planet '))
    omega_p=np.deg2rad(float(input('please input the Argument of periapsis(small omega) of the planet(deg) ')))
    OMEGA_p=np.deg2rad(float(input('please input the Longitude of the ascending node(big omega) of the planet(deg) ')))

except:
    print('invalid input')

x_b=sp.Symbol('x_b')
C_p=sp.Symbol('C_p')
F=sp.Symbol('F')
dist=sp.Symbol('dist')
P_p=a_p*(1-np.square(e_p))
C_p1=sp.Symbol('C_p1')
C_p2=sp.Symbol('C_p1')

C_p1,C_p2=sp.solveset((x_b)**2-(P_p**2)*((np.sin(omega_p))**2)+2*x_b*(e_p*x_b-P_p*np.cos(omega_p))*C_p+((P_p**2)*((np.sin(omega_p))**2)+(e_p*x_b-P_p*np.cos(omega_p))**2)*(C_p**2), C_p)

F=(P_p**2)/((1+e_p*C_p1)**2)

dist=np.abs(OMEGA_p*x_b+deltai_p*sp.sqrt(F-(x_b)**2)-deltai_b*sp.sqrt(F-(x_b)**2))
print('dist=',dist)

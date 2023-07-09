import numpy as np
from scipy.fft import fftshift
import matplotlib.pyplot as plt
from manim import *


s=1
nt=513
tf=100
zf=300
dt=tf/nt
dz=(dt**2)/2
nz=np.ceil(zf/dz)
nz=int(nz)
z=np.arange(0,nz)*dz
dw=2*PI/tf
w=np.arange(-nt/2,nt/2)
w2=fftshift(w**2)
t=np.arange(0,tf-dt,dt)
message=[0,0,1,0,1,0,1,1,0]
#message=[0, message, 0]
sech=lambda x: 1/np.cosh(x)
p=0.57
a=0.6

#funcion de onda

def f(t,tn,bool):
    return p*bool*sech(a*(t-tn))

part_num=len(message)
parts=np.linspace(0,tf,part_num)
B = 1/(parts[2]-parts[1]) #tal vez es con [] en python

u0=np.zeros(nt-1)
U=np.zeros((nt-1,int(nz)),dtype=complex)


for i in range(len(message)):
    u0=u0+f(t, parts[i], message[i])

U[:,0]=u0
coef=dz/dt**2 * s/2 * complex(0,1)
# mainDiag=-2*np.ones((1,nt-1))
# topDiag=np.ones((1,nt-1))
# bottomDiag=np.ones((1,nt-1))
# D = coef *( np.diag((mainDiag,0)) + np.diag((topDiag,1)) + np.diag((bottomDiag,-1)) )

D = np.zeros((nt-1,nt-1))
#llenar matriz memo

#made in an O(n^2) way

'''
Forma Roy de hacer la matriz escalada del operador de la segunda derivada
'''
#  for i = 2:nz-1
#  ter1=2*(D*U(:,i));
#  ter2=2*( (dz/1i) * abs(U(:,i)) .^ 2 .* U(:,i));
#  ter3= U(:,i-1);
#  %U(:,i+1) = 2*(D*U(:,i) + (dz/1i)*abs(U(:,i)).^2.*U(:,i)) + U(:,i-1);
#  U(:,i+1) = ter1 + ter2 + ter3;
#  end


'''
Forma de Memo de hacer la matriz escalada del operador de la segunda derivada
'''
D[0][0] = -2
for i in range(1,nt-1):
    for j in range(1,nt-1):
        if i == j:
            D[i][j] = -2
            D[i-1][j] = 1
            D[i][j-1] = 1
D= -coef*D


'''
Forma de Copilot de hacer la matriz escalada (se empino a memo porque la hace mas rapido xd)
'''
#made in an O(n) way
# for i in range(1,nt-2):
#     D[i][i-1] = 1
#     D[i][i] = -2
#     D[i][i+1] = 1

'''
Condicion inicial de la solucion
'''
# equacion = V^2*u0 + dz/i*u0^2*u0 +u0 = 0
U[:,1]=np.dot(D,u0) + dz/complex(0,1) * np.multiply(np.square(np.abs(u0)) , u0) + u0



for i in range(1,nz-1):

    # V^2*U(:,i) + 
    ter1=np.dot(D,U[:,i])
    # dz/i*U(:,i)^2*U(:,i) +
    ter2=(dz/complex(0,1)*(np.square(np.abs(U[:,i])) * U[:,i]))
    # U(:,i-1)
    ter3= U[:,i-1]


    #sumar los terminos de la ecuacion
    U[:,i+1]=2*(ter1+ter2)+ter3
    

    #Fase de debuggeo, cosas raras que me ayudaron a corregir errores
    if False:
        print(ter1[0]) # esta bien ahuevo perro ppcdsalvc ME QUIERO IR A DORMIR PERO YA MERO LO RESUELVO PERRO
        print("break")
        print(ter2[0]) # YA ESTA BIEN AHUEVO PERROOOOOO
        print("break")
        print(ter3[0]) # AHUEVO YA ESTA BIEN SOLO ME FALTA EL TER 2
        break



plt.imshow(np.abs(U))
plt.show()
# plt.plot(t,u0)
# plt.show()







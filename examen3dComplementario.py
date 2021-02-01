"""
Examen del triangulo
Autor: Angel Nereo Jimenez Mayo
"""
import matplotlib.pyplot as plt 
import numpy as np
from math import sin, cos, radians,sqrt
import tools3d 
import msvcrt
import keyboard

#______Coordenadas iniciales
xg=[]
yg=[]
zg=[]

#Cordenadas centrales
xc=80
yc=40
zc=40

#Plano y linea de sistema
x=[-40,-40,40,-40,-20]
y=[0,0,0,-20,-10]
z=[-10,10,10,15,0]

for i in range(len(x)):
    xg.append(x[i]+xc)
    yg.append(y[i]+yc)
    zg.append(z[i]+zc)

#____Plotear el sistema 
#def plotPlaneLine(xg,yg,zg,xh,yh,xhg,yhg,hitcolor):
def plotPlaneLine(xg,yg,zg,Whitpoint,a,a1,a2):
    plt.axis([0,150,100,0])
    plt.axis('on')
    plt.grid(True)
    plt.plot([xg[0],xg[1]],[yg[0],yg[1]],color='k')
    plt.plot([xg[1],xg[2]],[yg[1],yg[2]],color='k')
    plt.plot([xg[2],xg[0]],[yg[2],yg[0]],color='k')

    plt.plot([xg[0],xg[4]],[yg[0],yg[4]],color='red', linestyle=":")
    plt.plot([xg[4],xg[1]],[yg[4],yg[1]],color='red', linestyle=":")
    plt.plot([xg[4],xg[2]],[yg[4],yg[2]],color='red', linestyle=":")

    plt.plot([xg[3],xg[4]],[yg[3],yg[4]],color='b')#Line

    if(Whitpoint == 1):
        plt.text(10,10,'Esta fuera del plano')
    else:
        plt.text(10,10,'Esta dentro del plano')
    
    plt.text(10,15,'A=' + str(a))
    plt.text(10,20,'A1=' + str(a1))
    plt.text(10,25,'A2=' + str(a2))
    plt.text(10,30,'A2 + A1=' + str(a2 + a1))

    plt.show()

def hitpoint(x,y,z):
    #_____distance point 0 to 1
    a=x[0]-x[1]
    b=y[0]-y[1]
    c=z[0]-z[1]
    Q01=sqrt(a*a+b*b+c*c) 
    #_____distance point 1 to 2
    a=x[1]-x[2]
    b=y[1]-y[2]
    c=z[1]-z[2]
    Q12=sqrt(a*a+b*b+c*c)
    #_____distance point 2 to 0
    a=x[2]-x[0]
    b=y[2]-y[0]
    c=z[2]-z[0]
    Q20=sqrt(a*a+b*b+c*c)
    #Area
    s=(Q01+Q12+Q20)/2
    a= sqrt((s*(s-Q01))*(s-Q12)*(s-Q20))

    # hit a 0
    a=x[3]-x[0]
    b=y[3]-y[0]
    c=z[3]-z[0]
    Q30=sqrt(a*a+b*b+c*c)
    # 1 a hit
    a=x[1]-x[3]
    b=y[1]-y[3]
    c=z[1]-z[3]
    Q13=sqrt(a*a+b*b+c*c)
    #Area1
    s=(Q01+Q13+Q30)/2
    a1= sqrt((s*(s-Q01))*(s-Q13)*(s-Q30))  

    
    #_____distance point 0 to 2
    a=x[0]-x[2]
    b=y[0]-y[2]
    c=z[0]-z[2]
    Q02=sqrt(a*a+b*b+c*c) 
    #2 a hit
    a=x[2]-x[3]
    b=y[2]-y[3]
    c=z[2]-z[3]
    Q23=sqrt(a*a+b*b+c*c) 
    #Area2
    s=(Q02+Q23+Q30)/2
    a2= sqrt((s*(s-Q02))*(s-Q23)*(s-Q30)) 

    Whitpoint=0
    if ((a1+a2)>=a):
        Whitpoint = 0
    else:
        Whitpoint = 1
    
    
    #return xh,yh,xhg,yhg,hitcolor
    plotPlaneLine(xg,yg,zg,Whitpoint,a,a1,a2) 


def plotPlaneLinex(xc,yc,zc,Rx,hx1,hx2,hy1,hy2):
    for i in range(len(y)):
        x[3] = int(hx1)
        x[4] = int(hx2)
        y[3] = int(hy1)
        y[4] = int(hy2)
        [xg[i],yg[i],zg[i]]=tools3d.rotRx(xc,yc,zc,x[i],y[i],z[i],Rx)
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
    hitpoint(x,y,z)

def plotPlaneLiney(xc,yc,zc,Ry,hx1,hx2,hy1,hy2):
    for i in range(len(y)):
        x[3] = int(hx1)
        x[4] = int(hx2)
        y[3] = int(hy1)
        y[4] = int(hy2)
        [xg[i],yg[i],zg[i]]=tools3d.rotRy(xc,yc,zc,x[i],y[i],z[i],Ry)
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
    hitpoint(x,y,z)

def plotPlaneLinez(xc,yc,zc,Rz,hx1,hx2,hy1,hy2):
    for i in range(len(y)):
        x[3] = int(hx1)
        x[4] = int(hx2)
        y[3] = int(hy1)
        y[4] = int(hy2)
        [xg[i],yg[i],zg[i]]=tools3d.rotRz(xc,yc,zc,x[i],y[i],z[i],Rz)
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
    hitpoint(x,y,z)
    

####_____pedir al usaurio que eje desea trabajar y plotear el PlaneLine
axis=input("Teclea el eje que deseas visualizar 'x,y,z' o pulsa numero de control para salir ?:")  
while True:
    if axis=='x':#plotear el eje X
        hx1=input("Hitpoint x1:")
        hx2=input("Hitpoint x2:")
        hy1=input("Hitpoint y1:")
        hy2=input("Hitpoint y2:")
        Rx=radians(float(input('Dame los grados de rotacion ?: ')))
        plotPlaneLinex(xc,yc,zc,Rx,hx1,hx2,hy1,hy2)#LLamamos a la funcion de ploteo
    if axis=='y':
        hx1=input("Hitpoint x1:")
        hx2=input("Hitpoint x2:")
        hy1=input("Hitpoint y1:")
        hy2=input("Hitpoint y2:")
        Rx=radians(float(input('Dame los grados de rotacion ?: ')))
        plotPlaneLinex(xc,yc,zc,Ry,hx1,hx2,hy1,hy2)#LLamamos a la funcion de ploteo
    if axis=='z':
        hx1=input("Hitpoint x1:")
        hx2=input("Hitpoint x2:")
        hy1=input("Hitpoint y1:")
        hy2=input("Hitpoint y2:")
        Rx=radians(float(input('Dame los grados de rotacion ?: ')))
        plotPlaneLinex(xc,yc,zc,Rx,hx1,hx2,hy1,hy2)#LLamamos a la funcion de ploteo
    if keyboard.is_pressed('esc'):
        break  
    
           


#!/usr/bin/env python

import numpy as np

#MinDistDet(px,py,pz) return the closest distance of point (px,py,pz) to the IceCube detector (IC86)
#Negative distance means the point is in the detector volume


#based on string 36 (middle of the detector)
detTop = 500.97
detBottom = -503.25

detParamAx = [338.44, 576.37, 361.0, -256.14, -570.9, -347.88, 22.11, 101.04]
detParamAy = [463.72, 170.92, -422.83, -521.08, -125.14, 451.52, 509.5, 412.79]
detParamNx = [237.93, -215.37, -617.14, -314.76, 223.02, 369.99, 78.93, 237.40]
detParamNy = [-292.80, -593.75, -98.25, 395.94, 576.66, 57.98, -96.71, 50.93]


vertMinDistDet = lambda pz : min(abs(pz-detBottom),abs(pz-detTop))

def insideL(i,px,py): # detector side is True
    sign = (((detParamNx[i])*(py-detParamAy[i]))-((detParamNy[i])*(px-detParamAx[i])))
    if(sign<0):
        return True
    else:
        return False
    
def InOutHorizontal(px,py):
    inSideH = []
    for i in range(8):
        inSideH.append(insideL(i,px,py))
    if(not ((inSideH[0])&(inSideH[1])&(inSideH[2])&(inSideH[3])&(inSideH[4])&(inSideH[5]))):
        return False
    elif(inSideH[6]|inSideH[7]):
        return True
    else:
        return False

def InOutVertical(pz):
    if((pz<detTop)&(pz>detBottom)):
        return True #inside
    else:
        return False #outside

def minDistSeg(px,py,ax,ay,nx,ny):
    A = (nx*nx) + (ny*ny)
    B = 2.*((ax*nx)+(ay*ny)-(px*nx)-(py*ny))
    C = (px*px)+(py*py)+(ax*ax)+(ay*ay)-(2.*px*ax)-(2.*py*ay)
    t_min = -.5*B/A
    #dist_inf = (A*t_min*t_min) + (B*t_min) + C
    if(t_min<=0):
        dist_seg2 = C
    elif(t_min>=1):
        dist_seg2 = A + B + C
    else:
        dist_seg2 = (A*t_min*t_min) + (B*t_min) + C
    dist_seg = np.sqrt(dist_seg2)
    return [dist_seg,t_min]
        
def minDistDet(px,py,pz):
    inoutH = InOutHorizontal(px,py)
    inoutV = InOutVertical(pz)
    distEdge_all = []
    for i in range(8):
        distEdge_all.append(minDistSeg(px,py,detParamAx[i],detParamAy[i],detParamNx[i],detParamNy[i])[0])
    distEdge_min = min(distEdge_all)
    if((inoutH==True)&(inoutV==True)):
        dist_min = min(vertMinDistDet(pz),distEdge_min)
    elif((inoutH==True)&(inoutV==False)):
        dist_min = vertMinDistDet(pz)
    elif((inoutH==False)&(inoutV==True)):
        dist_min = distEdge_min
    elif((inoutH==False)&(inoutV==False)):
        dist_min = distEdge_min
    else:
        raise ValueError # inoutH and inoutV must be True or False
    if((inoutH==True)&(inoutV==True)):
        inSide=1
    else:
        inSide=-1
    #print( InOutHorizontal(px,py))
    #fig = plt.figure(figsize=(6,6))
    #plt.plot(np.append(detPx,detPx[0]),np.append(detPy,detPy[0]),'o-')
    #plt.plot(px,py,'ro')
    return -1.*inSide*dist_min

#!/usr/bin/env python

#calculating the boundry of the detector by corner points
#Lines are parmetrized as (x,y)=(detParamAx,detParamAy) + t*(detParamNx,detParamNy) and 0<t<1
#this file is not needed if you are working with the IC86 detector

#based on string 36 (middle of the detector)
detTop = 500.97
detBottom = -503.25

detPx = []
detPy = []

#String 74
detPx.append(338.44)
detPy.append(463.72)

#String 50
detPx.append(576.37)
detPy.append(170.92)

#String 6
detPx.append(361.00)
detPy.append(-422.83)

#String 1
detPx.append(-256.14)
detPy.append(-521.08)

#String 31
detPx.append(-570.90)
detPy.append(-125.14)

#String 75
detPx.append(-347.88)
detPy.append(451.52)

#String 78
detPx.append(22.11)
detPy.append(509.50)

#String 72
detPx.append(101.04)
detPy.append(412.79)

detParamAx = []
detParamAy = []
detParamNx = []
detParamNy = []

for i in range(8):
    if(i==7):
        j=0
    else:
        j= i+1
    detParamAx.append(detPx[i])
    detParamAy.append(detPy[i])
    detParamNx.append(detPx[j]-detPx[i])
    detParamNy.append(detPy[j]-detPy[i])



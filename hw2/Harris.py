import utils
import configs
import numpy as np
import scipy.signal as sci
import matplotlib.pyplot as plt

img=utils.read_img_gray(configs.img_route)

win_norm=utils.win_norm(9)
win_gauss=utils.win_gauss(7,2)

Ix=sci.convolve2d(img,configs.kernel_x,'same')
Iy=sci.convolve2d(img,configs.kernel_y,'same')


Ixx=sci.convolve2d(Ix*Ix,win_gauss,'same')
Ixy=sci.convolve2d(Ix*Iy,win_gauss,'same')
Iyy=sci.convolve2d(Iy*Iy,win_gauss,'same')
'''
Ixx=sci.convolve2d(Ix*Ix,win_norm,'same')
Ixy=sci.convolve2d(Ix*Iy,win_norm,'same')
Iyy=sci.convolve2d(Iy*Iy,win_norm,'same')
'''


R=np.zeros(Ixx.shape)

maxx=-1
minn=1e7

for i in range(Ixx.shape[0]):
    for j in range(Ixx.shape[1]):
        det=Ixx[i,j]*Iyy[i,j]-pow(Ixy[i,j],2)
        trace=Ixx[i,j]+Iyy[i,j]
        R[i,j]=det-configs.alpha*pow(trace,2)
        if R[i,j]>maxx:
            maxx=R[i,j]
        if R[i,j]<minn:
            minn=R[i,j]

neigh=configs.neigh
res=np.zeros(R.shape)
res_x=[]
res_y=[]
#threshold=1/20*maxx
threshold=minn+1/3.5*(maxx-minn)

for i in range(1,R.shape[0]-1):
    for j in range(1,R.shape[1]-1):
        if R[i,j]<threshold:
            res[i,j]=0
            continue
        flag=True
        for k in range(8):
            if flag==False:
                break
            if R[i,j]<R[i+neigh[0][k],j+neigh[1][k]]:
                res[i,j]=0
                flag=False
            if k==7:
                res[i,j]=255
                res_y.append(i)
                res_x.append(j)

plt.imshow(img,cmap='gray')
plt.plot(res_x,res_y,'*')
plt.show()

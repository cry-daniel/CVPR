from math import pi, tan
import utils
import configs
import cv2 as cv
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from tqdm import tqdm

img=utils.read_img_gray(configs.img_route)

img=cv.GaussianBlur(img,(3,3),1)    #滤波

magnitude,theta=utils.gradient(img,configs.true) #,configs.true)

for i in range(theta.shape[0]):
    for j in range(theta.shape[1]):
        if theta[i][j]<0:
            theta[i][j]+=180

case=configs.case

maxx=-1
minn=1e5

for i in tqdm(range(theta.shape[0])):
    for j in range(theta.shape[1]):
        if i==0 or i==theta.shape[0]-1 or j==0 or j==theta.shape[1]-1:
            magnitude[i][j]=0
            continue
        num=int(theta[i][j]/45)
        if theta[i][j]%45==0:
            num-=1
        if theta[i][j]==0:
            num=0
        x=np.array([0,1])
        y1=np.array([magnitude[i+case[num][0][0]][j+case[num][0][1]],\
            magnitude[i+case[num][1][0]][j+case[num][1][1]]])
        y2=np.array([magnitude[i-case[num][0][0]][j-case[num][0][1]],\
            magnitude[i-case[num][1][0]][j-case[num][1][1]]])
        f1=interpolate.interp1d(x,y1)
        f2=interpolate.interp1d(x,y2)
        alpha=theta[i][j]-num*45
        len=tan(alpha/180*pi)
        #print(len)
        temp1=f1(len)
        temp2=f2(len)
        if magnitude[i][j]>max(temp1,temp2):
            if magnitude[i][j]>maxx:
                maxx=magnitude[i][j]
            if magnitude[i][j]<minn:
                minn=magnitude[i][j]
        else:
            magnitude[i][j]=0

plt.imshow(magnitude,cmap='gray')
plt.show()

#up_threshold=minn+2/3*(maxx-minn)
#down_threshold=minn+1/3*(maxx-minn)

threshold=minn+2/3*(maxx-minn)

for i in tqdm(range(magnitude.shape[0])):
    for j in range(magnitude.shape[1]):
        if magnitude[i][j]<threshold:
            magnitude[i][j]=0

plt.imshow(magnitude,cmap='gray')
plt.show()
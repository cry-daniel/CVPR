import utils
import configs
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

x_size=y_size=2

#draw_gauss_or_laplace=configs.gauss
draw_gauss_or_laplace=configs.laplace

img=utils.read_img(configs.img_route)
img=np.dot(img,[0.299,0.587,0.114])   #转灰度
img=cv.resize(img,configs.size)

print(img.shape)

cnt=0

while img.shape[0]>=16:
    cnt+=1
    plt.subplot(x_size,y_size,cnt)
    if draw_gauss_or_laplace==configs.gauss:
        plt.imshow(img,cmap ='gray')
    Img=cv.GaussianBlur(img,(3,3),1)
    if draw_gauss_or_laplace==configs.laplace:
        res=img-Img
        plt.imshow(res,cmap ='gray')
    img=np.zeros((int(Img.shape[0]/2),int(Img.shape[1]/2)))
    for i in range(Img.shape[0]):
        for j in range(Img.shape[1]):
            if i%2==0 and j%2==0:
                img[int(i/2)][int(j/2)]=Img[i][j]

plt.show()
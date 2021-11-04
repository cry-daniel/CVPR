from os import error
import matplotlib
import numpy as np
import matplotlib.image as mg
import matplotlib.pyplot as plt
import math
import configs
import cv2 as cv
import scipy.signal as sci

def read_img(route):
    img=mg.imread(route)
    print("img size : ",img.shape)
    return img

def read_img_gray(route):
    img=read_img(route)
    img=np.dot(img,[0.299,0.587,0.114])   #转灰度
    return img

def draw(img,num,title):
    plt.subplot(configs.plt_x,configs.plt_y,num)
    plt.title(title)
    plt.imshow(img)

def func_forward(img,trans_A,trans_B):  #最近邻
    i,j,k=img.shape
    Img=np.full((i,j,k),255,dtype=np.uint8)
    for x in range(i):
        for y in range(j):
            x_,y_=(np.dot(trans_A,[x,y]+trans_B))   #新坐标
            x_=int(round(x_))
            y_=int(round(y_))
            if x_ in (range(i)) and y_ in range(j):
                Img[x_][y_]=img[x][y]
    return Img

def func_inverse(img,trans_A,trans_B):
    i,j,k=img.shapey
    trans_A=np.linalg.inv(trans_A)
    Img=np.full((i,j,k),255,dtype=np.uint8)
    for x in range(i):
        for y in range(j):
            x_,y_=np.dot(trans_A,[x,y]-trans_B) #原坐标
            x_=int(round(x_))
            y_=int(round(y_))
            if x_ in range(i) and y_ in range(j):
                Img[x][y]=img[x_][y_]
    return Img

def translation(img,delta_x,delta_y,forward_or_inverse=configs.forward):   #delta_x > 0 左移；delta_y > 0 右移
    trans_A=np.array([[1,0],[0,1]])
    trans_B=np.array([delta_x,delta_y])
    if forward_or_inverse==configs.forward:
        Img=func_forward(img,trans_A,trans_B)
    elif forward_or_inverse==configs.inverse:
        Img=func_inverse(img,trans_A,trans_B)
    else:
        error('Unexpected Img')
    return Img

def rotate(img,beta,forward_or_inverse=configs.forward):  #beta为角度
    beta=beta*math.pi/180
    trans_A=np.array([[math.cos(beta),math.sin(beta)],[-math.sin(beta),math.cos(beta)]])
    trans_B=np.array([0,0])
    if forward_or_inverse==configs.forward:
        Img=func_forward(img,trans_A,trans_B)
    elif forward_or_inverse==configs.inverse:
        Img=func_inverse(img,trans_A,trans_B)
    else:
        error('Unexpected Img')
    return Img

def euclid(img,delta_x,delta_y,beta,forward_or_inverse=configs.forward):
    beta=beta*math.pi/180
    trans_A=np.array([[math.cos(beta),math.sin(beta)],[-math.sin(beta),math.cos(beta)]])
    trans_B=np.array([delta_x,delta_y])
    if forward_or_inverse==configs.forward:
        Img=func_forward(img,trans_A,trans_B)
    elif forward_or_inverse==configs.inverse:
        Img=func_inverse(img,trans_A,trans_B)
    else:
        error('Unexpected Img')
    return Img

def similar(img,x,y,delta_x,delta_y,beta,forward_or_inverse=configs.forward):   #乘x，乘y
    beta=beta*math.pi/180
    trans_A=np.array([[math.cos(beta)/x,math.sin(beta)/x],[-math.sin(beta)/y,math.cos(beta)/y]])
    trans_B=np.array([delta_x/x,delta_y/y])
    if forward_or_inverse==configs.forward:
        Img=func_forward(img,trans_A,trans_B)
    elif forward_or_inverse==configs.inverse:
        Img=func_inverse(img,trans_A,trans_B)
    else:
        error('Unexpected Img')
    return Img

def affine(img,x1,x2,x3,y1,y2,y3,forward_or_inverse=configs.forward):
    trans_A=np.array([[x1,x2],[y1,y2]])
    trans_B=np.array([x3,y3])
    if forward_or_inverse==configs.forward:
        Img=func_forward(img,trans_A,trans_B)
    elif forward_or_inverse==configs.inverse:
        Img=func_inverse(img,trans_A,trans_B)
    else:
        error('Unexpected Img')
    return Img

def gradient(Img,draw_picture=configs.false):
    Img_x=sci.convolve2d(Img,configs.kernel_x)
    Img_y=sci.convolve2d(Img,configs.kernel_y)
    '''
    plt.subplot(1,2,1)
    plt.imshow(Img_x,cmap='gray')
    plt.subplot(1,2,2)
    plt.imshow(Img_y,cmap='gray')
    plt.show()
    '''
    magnitude=np.zeros(Img_x.shape)
    theta=np.zeros(Img_x.shape)
    for i in range(magnitude.shape[0]):
        for j in range(magnitude.shape[1]):
            if Img_x[i][j]==0 and Img_y[i][j]==0:
                continue
            magnitude[i][j]=math.sqrt(pow(Img_x[i][j],2)+pow(Img_y[i][j],2))
            theta[i][j]=math.atan2(Img_y[i][j],Img_x[i][j])*180/math.pi
    if draw_picture==configs.true:
        plt.subplot(1,2,1)
        plt.imshow(magnitude,cmap='gray')
        plt.subplot(1,2,2)
        #plt.imshow(theta)
        plt.imshow(theta,cmap='gray')
        plt.show()
    return magnitude,theta

def win_norm(length):
    return np.full((length,length),1/pow(length,2))

def win_gauss(length,sigma):
    win=np.zeros((length,length))
    mid=(length-1)/2
    tot=0
    for i in range(length):
        for j in range(length):
            win[i,j]=1/(2*math.pi*pow(sigma,2))*\
                math.exp(-(pow((i-mid),2)+pow((j-mid),2))/(2*pow(sigma,2)))
            tot+=win[i,j]
    #print(win)
    #print(tot)
    return win
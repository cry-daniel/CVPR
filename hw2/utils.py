from os import error
import numpy as np
import matplotlib.image as mg
import matplotlib.pyplot as plt
import math
import configs
import cv2 as cv

def read_img(route):
    img=mg.imread(route)
    print("size : ",img.shape)
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
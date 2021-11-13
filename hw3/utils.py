import cv2
import numpy as np

def load_image(path, gray=False):
    if gray:
        img = cv2.imread(path)
        return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    else:
        return cv2.imread(path)

def func_inverse(img,trans_A,trans_B):
    i,j,=img.shape
    trans_A=np.linalg.inv(trans_A)
    Img=np.full(img.shape,255,dtype=np.uint8)
    for x in range(i):
        for y in range(j):
            x_,y_=np.dot(trans_A,[x,y]-trans_B) #原坐标
            x_=int(round(x_))
            y_=int(round(y_))
            if x_ in range(i) and y_ in range(j):
                Img[x][y]=img[x_][y_]
    return Img

def affine(img,x1,x2,x3,y1,y2,y3):
    trans_A=np.array([[x1,x2],[y1,y2]])
    trans_B=np.array([x3,y3])
    Img=func_inverse(img,trans_A,trans_B)
    return Img

'''
def transform(origin):
    h, w,  = origin.shape
    generate_img = np.zeros(origin.shape)
    for i in range(h):
        for j in range(w):
            generate_img[i, w - 1 - j] = origin[i, j]
    return generate_img.astype(np.uint8)
'''

def transform(origin):
    Img=affine(origin,1.2,0.3,0.1,0.3,1,0.8)
    return Img

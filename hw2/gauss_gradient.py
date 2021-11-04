import utils
import configs
import cv2 as cv

import matplotlib.pyplot as plt

img=utils.read_img_gray(configs.img_route)

Img=cv.GaussianBlur(img,(3,3),0.01)
utils.gradient(Img,configs.true)

Img=cv.GaussianBlur(img,(3,3),1)
utils.gradient(Img,configs.true)
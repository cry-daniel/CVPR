img_route='./imgs/test.jpg'

plt_x=2
plt_y=3

forward=1
inverse=-1

gauss=1
laplace=-1

size=(512,512)

#sobel 算子
kernel_x=[[-1,0,1],[-2,0,2],[-1,0,1]]
kernel_y=[[-1,-2,-1],[0,0,0],[1,2,1]]

true=1
false=-1

case=[[[1,0],[1,1]],[[1,1],[0,1]],[[0,1],[-1,1]],[[-1,1],[-1,0]]]
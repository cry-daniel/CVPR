import utils
import configs
import matplotlib.pyplot as plt

inv=configs.inverse

img=utils.read_img(configs.img_route)
utils.draw(img,1,'origin')
Img=utils.translation(img,100,100,inv)
utils.draw(Img,2,'translation')
Img=utils.rotate(img,-30,inv)
utils.draw(Img,3,'rotate')
Img=utils.euclid(img,-100,100,45,inv)
utils.draw(Img,4,'Euclid')
Img=utils.similar(img,2,2,-100,100,45,inv)
utils.draw(Img,5,'similar')
Img=utils.affine(img,0.5,0,50,0.4,0.7,100,inv)
utils.draw(Img,6,'affine')
plt.show()
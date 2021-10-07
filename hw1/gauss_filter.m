%生成滤波核，HW1

clear;
clc;

%sigma=input("Input sigma : ");
sigma=1;
size=25;
filter=zeros(size,size);
mid=(size+1)/2;
tot=0;

%% 生成高斯核
for i = 1:size
    for j =1:size
        filter(i,j)=1/(2*pi*sigma^2)*exp(-((i-mid)^2+(j-mid)^2)/(2*sigma^2));
        tot=tot+filter(i,j);
    end
end

%% 归一化
for i = 1:size
    for j =1:size
        %filter(i,j)=1/(2*pi*sigma^2)*exp(-((i-mid)^2+(j-mid)^2)/(2*sigma^2));
        filter(i,j)=filter(i,j)/tot;
    end
end

%% 读图像
img=imread('test2.jpeg');

%% 处理图像并写图像
subplot(3,2,1);
imshow(img);title("origin");

Img=imfilter(img,filter,0);
subplot(3,2,3);
imshow(Img);title("0 padding");

Img=imfilter(img,filter,'symmetric');
subplot(3,2,4);
imshow(Img);title("reflect");

Img=imfilter(img,filter,'replicate');
subplot(3,2,5);
imshow(Img);title("copy edge");

Img=imfilter(img,filter,'circular');
subplot(3,2,6);
imshow(Img);title("wrap around");

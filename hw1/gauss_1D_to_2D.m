clear;
clc;

%sigma=input("Input sigma : ");
sigma=1;
size=25;
filter1=zeros(size,1);
filter2=zeros(1,size);
mid=(size+1)/2;
tot=0;

%% 生成高斯核
for i = 1:size
        filter1(i)=1/sqrt(2*pi*sigma^2)*exp(-((i-mid)^2)/(2*sigma^2));
        filter2(i)=filter1(i);
        tot=tot+filter1(i);
end

%% 归一化
for i = 1:size
        filter1(i)=filter1(i)/tot;
        filter2(i)=filter2(i)/tot;
end

%% 读图像
img=imread('test0.jpeg');

%% 处理图像并写图像
subplot(2,3,1);
imshow(img);title("origin");

Img=imfilter(img,filter1);
subplot(2,3,3);
imshow(Img);title("列向量滤波");

Img=imfilter(img,filter2);
subplot(2,3,4);
imshow(Img);title("行向量滤波");

Img=imfilter(Img,filter1);
subplot(2,3,5);
imshow(Img);title("先行再列滤波");

filter=conv2(filter1,filter2);

Img=imfilter(img,filter);
subplot(2,3,6);
imshow(Img);title("二维向量滤波");
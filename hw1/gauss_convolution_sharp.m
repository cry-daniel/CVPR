%生成滤波核，HW1

clear;
clc;

%sigma=input("Input sigma : ");
sigma=1;
size=25;
filter=zeros(size,size);
mid=(size+1)/2;
tot=0;

sigma_=100;
size_=25;
filter_=zeros(size_,size_);
mid_=(size_+1)/2;
tot_=0;
%% 生成高斯核
for i = 1:size
    for j =1:size
        filter(i,j)=1/(2*pi*sigma^2)*exp(-((i-mid)^2+(j-mid)^2)/(2*sigma^2));
        tot=tot+filter(i,j);
    end
end
for i = 1:size_
    for j =1:size_
        filter_(i,j)=1/(2*pi*sigma_^2)*exp(-((i-mid_)^2+(j-mid_)^2)/(2*sigma_^2));
        tot_=tot_+filter_(i,j);
    end
end
%% 归一化
for i = 1:size
    for j =1:size
        filter(i,j)=filter(i,j)/tot;
    end
end
for i = 1:size_
    for j =1:size_
        filter_(i,j)=filter_(i,j)/tot_;
    end
end

subplot(2,2,1);
imshow(filter);title("sigma = 1");
subplot(2,2,2)
imshow(filter_);title("sigma = 10");
subplot(2,2,3)
temp=conv2(filter,filter_);
imshow(temp);title("conv")

figure;

sub=filter-filter_;

tot_sub=0;

for i = 1:size_
    for j =1:size_
        %sub(i,j)=abs(sub(i,j));
        tot_sub=tot_sub+sub(i,j);
    end
end
for i = 1:size_
    for j =1:size_
        sub(i,j)=sub(i,j)/tot_sub;
    end
end

sub;

close;

%% 读图像
img=imread('test.jpeg');

%% 处理图像并写图像
subplot(2,3,1);
imshow(img);title("origin");

Img=imfilter(img,filter);
subplot(2,3,2);
imshow(Img);title("sigma = 1");
temp1=Img;

Img=imfilter(img,filter_);
subplot(2,3,3);
imshow(Img);title("sigma = 100");
temp2=Img;

Img=imfilter(img,sub);
subplot(2,3,4);
%imshow(sub)
imshow(Img);title("sub");

Img=temp1-temp2;
subplot(2,3,5);
%imshow(sub)
imshow(Img);title("sharp minus");

Img=0.5*Img+temp1;
subplot(2,3,6);
%imshow(sub)
imshow(Img);title("sharp");
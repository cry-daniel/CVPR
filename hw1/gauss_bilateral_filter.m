%生成滤波核，HW1

clear;
clc;

%sigma=input("Input sigma : ");
sigma=1;
sigma2=2;
size_=25;
filter=zeros(size_,size_);
filter2=zeros(size_,size_);
mid=(size_+1)/2;
tot=0;

%% 生成高斯核
for i = 1:size_
    for j =1:size_
        filter(i,j)=1/(2*pi*sigma^2)*exp(-((i-mid)^2+(j-mid)^2)/(2*sigma^2));
        tot=tot+filter(i,j);
    end
end

%% 归一化
for i = 1:size_
    for j =1:size_
        %filter(i,j)=1/(2*pi*sigma^2)*exp(-((i-mid)^2+(j-mid)^2)/(2*sigma^2));
        filter(i,j)=filter(i,j)/tot;
    end
end

%% 读图像
img=imread('test0.jpeg');

%% 处理图像并写图像
subplot(2,2,1);
imshow(img);title("origin");

Img=imfilter(img,filter,"circular");
subplot(2,2,3);
imshow(Img);title("gauss filter");

[a,b,~]=size(img);

find = exist('Img2.mat','file');

if find
    load('Img2.mat')
else
    Img2=zeros(a,b,3);
    for i=1:a
        fprintf("%f %% \n",i/a);
        for j=1:b
            for m=1:3
                tot=0;
                %求值域化
                for k = 1:size_
                    for l =1:size_
                        x1=mod(i+mid-k,a)+1;
                        y1=mod(j+mid-l,b)+1+(m-1)*b;
                        filter2(k,l)=filter(k,l)*exp( double((img(x1,y1)-img(i,j+(m-1)*b))^2 / (2*sigma2^2)) );
                        tot=tot+filter2(k,l);
                    end
                end
                %归一化并求值
                temp=0.;
                for k = 1:size_
                    for l =1:size_
                        filter2(k,l)=filter2(k,l)/tot;
                    end
                end
                for k = 1:size_
                    for l =1:size_
                        x1=mod(i+mid-k,a)+1;
                        y1=mod(j+mid-l,b)+1+(m-1)*b;
                        temp=double(temp+double(filter2(size_-k+1,size_-l+1)*img(x1,y1)));

                    end
                end
                Img2(i,j,m)=floor(temp);
            end
        end
    end
    save Img2.mat Img2
end

subplot(2,2,4);
imshow(Img2/256);title("bilateral");

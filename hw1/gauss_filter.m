%生成滤波核，HW1

%% 读图像

if ~exist('img','var')
    clear;
    clc;
    img=imread('test0.jpeg');
    find=0;
else
    find=1;
end

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

%% 处理图像并写图像
if ~find
    subplot(2,3,1);
    imshow(img);title("origin");

    Img=imfilter(img,filter,0);
    subplot(2,3,3);
    imshow(Img);title("0 padding");

    Img=imfilter(img,filter,'symmetric');
    subplot(2,3,4);
    imshow(Img);title("reflect");

    Img=imfilter(img,filter,'replicate');
    subplot(2,3,5);
    imshow(Img);title("copy edge");

    Img=imfilter(img,filter,'circular');
    subplot(2,3,6);
    imshow(Img);title("wrap around");
    clc;
    clear;
else
    %img= rgb2gray(img);
    %img=double(img);
    img=imfilter(img,filter,'circular');
    f=fft2(img);        %傅里叶变换
    f=fftshift(f);      %使图像对称
    r=real(f);          %图像频域实部
    i=imag(f);          %图像频域虚部
    margin=log(abs(f));      %图像幅度谱，加log便于显示
    phase=log(angle(f)*180/pi);     %图像相位谱
    l=log(f);           
    subplot(2,2,1),imshow(img),title('源图像');
    subplot(2,2,2),imshow(l,[]),title('图像频谱');
    subplot(2,2,3),imshow(margin,[]),title('图像幅度谱');
    subplot(2,2,4),imshow(phase,[]),title('图像相位谱');
end

%% Use BWBM3D
clear all;
clc

%% data
addpath('BM3D');
for i = 130%:700
    path = strcat('\\storage-3\tabgha\users\gq\CNNIQA-master\ct_mat\low_mat\imglow_',num2str(i,'%04d'),'.mat');
    load(path);
    sigma = 5;
    t = min(img(:));
    z = max(img(:));
    input = (img-t)/(z-t);
    [~,output] = BM3D(1,input,sigma);
    img = (output*(z-t))+t;
    %path_save = strcat('\\storage-3\tabgha\users\gq\CNNIQA_CN\ct_mat\bm3d_mat\imglow_',num2str(i,'%04d'),'.mat');
    %save(path_save,'img','-v7.3')
end
%figure,imshow(img,[-86 325])
close
clear all;
clc

%% data
for i = 1:700
    path = strcat('\\storage-3\tabgha\users\gq\CNNIQA-master\ct_mat\low_mat\imglow_',num2str(i,'%04d'),'.mat');
    load(path);
    h1 = fspecial('gaussian',5,1.3);
    img = imfilter(img,h1,'replicate');
    path_save = strcat('\\storage-3\tabgha\users\gq\CNNIQA-master\ct_mat\denoise_mat\imglow_',num2str(i,'%04d'),'.mat');
    save(path_save,'img','-v7.3')
end
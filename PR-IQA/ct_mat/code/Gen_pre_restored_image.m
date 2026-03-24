%% Generate pre-restored images with NLM, BM3D, Bilateral filtering(BF)
clear all;
clc

%% NLM part
%%addpath('NLM');
%%path_save = '.\ct_mat\3dgr_mat\';
%%mkdir(path_save);
%%deta = 20;    % denoise degree of nlm
%%for i = 1:153
    %%disp(i)
    %%path = strcat('.\ct_mat\low_mat\imglow_',num2str(i,'%04d'),'.mat');
    %%load(path);
    
    %%img = imnlmfilt(img,'DegreeOfSmoothing', deta);
    %%name_save = strcat('imglow_',num2str(i,'%04d'),'.mat');
    %%save([path_save name_save],'img','-v7.3')
%%end

%% BM3D part
addpath('BM3D');
path_save = '/home/liuyiwei/PR-IQA/ct_mat/bm3d_mat_3dgr/';  % 你的输出文件夹
mkdir(path_save);
sigma = 5;     % denoise degree of bm3d

% 指向你存放 153 张图片的文件夹
img_folder = '/home/liuyiwei/cut_image/cut_image/cut_3dgr/'; 
files = dir(fullfile(img_folder, '*.png'));

if isempty(files)
    error('救命！在这个路径下没有找到任何图片，请检查路径拼写或图片后缀名！');
end

for i = 1:length(files) % 把原来的 1:700 改成了 1:153
    % 1. 拼接图片路径 (替换了原来的 path = strcat...)
    path = fullfile(img_folder, files(i).name);
    
    % 2. 读取 png 图片并转为双精度矩阵 (替换了原来的 load(path))
    img = double(imread(path));
    if size(img, 3) == 3
        img = rgb2gray(img); % 防止图片是 3 通道的 RGB
    end
    
    % ========== 下面是原作者核心逻辑，一字未改 ==========
    min_vaule = min(img(:));
    max_vaule = max(img(:));
    if max_vaule - min_vaule == 0 % 加个小保险，防止全黑图报错
        continue;
    end
    input = (img-min_vaule)/(max_vaule-min_vaule);
    [~,output] = BM3D(1,input,sigma);
    img = (output*(max_vaule-min_vaule))+min_vaule;
    % ====================================================
    
    % 3. 保存为 .mat 文件 (用原来的文件名，后缀改成 .mat)
    [~, base_name, ~] = fileparts(files(i).name);
    name_save = strcat(base_name, '.mat');
    
    save([path_save name_save],'img','-v7.3')
    
    % 加个打印，让你看着踏实，知道跑到第几个了
    disp(['BM3D处理中: ', num2str(i), '/', num2str(length(files))]);
end

%% BF part
%%path_save = '.\ct_mat\bf_mat\';
%%mkdir(path_save);
%%sigma = 5;     
%%for i = 1:700
    %%path = strcat('.\ct_mat\low_mat\imglow_',num2str(i,'%04d'),'.mat');
    %%load(path);
    
    %%imgVar = std2(img)^2;
    %%DoS = 2*imgVar;    % denoise degree of bf
    %%img = imbilatfilt(I,DoS);
    %%name_save = strcat('imglow_',num2str(i,'%04d'),'.mat');
    %%save([path_save name_save],'img','-v7.3')
%%end
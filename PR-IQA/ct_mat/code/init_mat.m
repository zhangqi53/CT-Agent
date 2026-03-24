clear all
clc

%% 路径设置（修改这里）
png_dir = '/home/liuyiwei/PR-IQA/3dgr/';        % 152张PNG重建图所在文件夹
fbp_path = '/home/liuyiwei/PR-IQA/low_3dgr/fbp_recon_23.13dB_ssim0.5143.png';      % FBP图路径
mat_dir = '/home/liuyiwei/PR-IQA/ct_mat/3dgr_mat/';    % 输出mat保存路径
error_mat_dir = '/home/liuyiwei/PR-IQA/ct_mat/3dgr_error_mat/'; % 输出error_mat路径

mkdir(mat_dir);
mkdir(error_mat_dir);

%% 读取FBP参考图
fbp = imread(fbp_path);
fbp = double(fbp);          % 转为double类型
if size(fbp, 3) == 3
    fbp = rgb2gray(uint8(fbp));  % 如果是彩色图转灰度
    fbp = double(fbp);
end

%% 获取所有PNG文件
files = dir(fullfile(png_dir, '*.png'));
if isempty(files)
    files = dir(fullfile(png_dir, '*.jpg'));
end
files = sort({files.name});   % 按文件名排序

%% 逐张处理
for i = 1:length(files)
    disp(i)
    
    % 读取PNG重建图
    img_path = fullfile(png_dir, files{i});
    img = imread(img_path);
    img = double(img);
    if size(img, 3) == 3
        img = double(rgb2gray(uint8(img)));
    end
    
    % 保存 3dgr_mat（重建图）
    mat_name = strcat('imglow_', num2str(i, '%04d'), '.mat');
    save([mat_dir mat_name], 'img', '-v7.3');
    
    % 计算并保存 error_mat（FBP图 - 重建图）
    img = fbp - img;   % 注意：这里变量名保持img，和原项目一致
    save([error_mat_dir mat_name], 'img', '-v7.3');
end

disp('全部完成！')
clear all
clc

% 1. 配置三个关键文件夹路径 (严格对照你截图里的真实路径)
path_low = '/home/liuyiwei/cut_image/cut_image/cut_3dgr/';       % 你的原始重建图(泥水)
path_denoise = '/home/liuyiwei/PR-IQA/ct_mat/bm3d_mat_3dgr/';    % 刚刚用 BM3D 洗出来的(清水)
path_save = '/home/liuyiwei/PR-IQA/ct_mat/bm3d_error_mat_3dgr/'; % 准备存放 error_mat 的新文件夹(纯泥巴)

% 如果存放 error 的文件夹不存在，就建一个
if ~exist(path_save, 'dir')
    mkdir(path_save);
end

% 找所有的原始 .png 图
files = dir(fullfile(path_low, '*.png'));

if isempty(files)
    error('原图路径下没找到图片，请检查 path_low！');
end

for i = 1:length(files)
    % 2. 拿到文件名，准备拼接寻找对应的 .mat 文件
    img_name = files(i).name;
    [~, base_name, ~] = fileparts(img_name);
    mat_name = strcat(base_name, '.mat'); 
    
    % 3. 读取原图 (Low Image)
    file_low = fullfile(path_low, img_name);
    low_img = double(imread(file_low));
    if size(low_img, 3) == 3
        low_img = rgb2gray(low_img);
    end
    
    % 4. 读取降噪图 (Denoise Image)
    file_denoise = fullfile(path_denoise, mat_name);
    
    % 加个小保险：防止你刚才的 BM3D 有漏跑的
    if ~exist(file_denoise, 'file')
        disp(['警告：找不到对应的降噪图 ', mat_name, '，自动跳过。']);
        continue;
    end
    
    % load 进来后，变量名自动叫 img
    load(file_denoise); 
    denoise_img = img;
    
    % ========== 原作者最核心的残差提取逻辑，一字未改 ==========
    img = low_img - denoise_img;
    % ==========================================================
    
    % 5. 保存为 error_mat
    save([path_save mat_name], 'img', '-v7.3');
    
    disp(['Error Mat 提取中: ', num2str(i), '/', num2str(length(files))]);
end

disp('🎉 全部 error_mat 生成完毕！数据预处理大功告成！')
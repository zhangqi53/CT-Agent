%% Calculate SSIM and NIQE scores
clear all
clc

ssim_scores = zeros(700,1);
niqe_scores = zeros(700,1);

% load the trained niqe model
load('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\niqe_model.mat');
for i = 1:700
    disp(i)
    path1 = strcat('\\storage-3\tabgha\users\gq\PR-IQA\ct_mat\low_mat\imglow_',num2str(i,'%04d'),'.mat');        % replace to personal path
    path2 = strcat('\\storage-3\tabgha\users\gq\PR-IQA\ct_mat\denoise_mat\imglow_',num2str(i,'%04d'),'.mat');    % replace to personal path
    in = load(path1);
    ref = load(path2);
    in = double(in.img);
    ref = double(ref.img);
    L = max(ref(:));
    NIQE = niqe(ref,model);
    niqe_scores(i,:) = 100-NIQE;
    ssim_one  =  ssim(in, ref, 'DynamicRange', L);
    ssim_scores(i,:) = ssim_one;
end

save('.\ssim_niqe_scores.mat', 'ssim_scores','niqe_scores','-v7.3')
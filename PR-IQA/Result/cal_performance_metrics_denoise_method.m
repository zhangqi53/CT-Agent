%% Calculate the PLCC, SROCC and RMSE under different denoise method
clear all
clc

addpath('.\tools');

%% Initialization data
plcc_baseline = 0;
srocc_baseline = 0;
rmse_baseline = 0;
plcc_bilat = 0;
srocc_bilat = 0;
rmse_bilat = 0;
plcc_nlm = 0;
srocc_nlm = 0;
rmse_nlm = 0;
plcc_bm3d = 0;
srocc_bm3d = 0;
rmse_bm3d = 0;

%% Calculate the PLCC, SROCC and RMSE
for seed_id = 1:10
    % Extract the label scores (Mos_test) of the test set
    path = strcat('\\storage-3\tabgha\users\gq\PR-IQA\data\CTinfo_seed_',num2str(seed_id,'%02d'),'.mat');
    load(path)
    load('\\storage-3\tabgha\users\gq\PR-IQA\data\mos.mat')
    
    path = strcat('.\data\seed_',num2str(seed_id,'%02d'),'\test_id_seed_',num2str(seed_id,'%02d'),'.mat');
    load(path)
    [num,~] = size(test_id);
    Mos_test = zeros(1,num);
    for i = 1:num
        Mos_test(1,i) = Mos(test_id(i),1);
    end
    
    % Baseline
    path = strcat('.\data\seed_',num2str(seed_id,'%02d'),'\score_single.mat');
    load(path)
    [Plcc_baseline,Srocc_baseline,Rmse_baseline] = verify_performance(Mos_test',score_fuse);
    plcc_baseline = plcc_baseline + Plcc_baseline;
    srocc_baseline = srocc_baseline + Srocc_baseline;
    rmse_baseline = rmse_baseline + Rmse_baseline;
    
    % BF
    path = strcat('.\data\seed_',num2str(seed_id,'%02d'),'\score_bf_3_30.mat');
    load(path)
    [Plcc_bilat,Srocc_bilat,Rmse_bilat] = verify_performance(Mos_test',score_fuse);
    plcc_bilat = plcc_bilat + Plcc_bilat;
    srocc_bilat = srocc_bilat + Srocc_bilat;
    rmse_bilat = rmse_bilat + Rmse_bilat;
    
    % NLM
    path = strcat('.\data\seed_',num2str(seed_id,'%02d'),'\score_nlm_3_30.mat');
    load(path)
    [Plcc_nlm,Srocc_nlm,Rmse_nlm] = verify_performance(Mos_test',score_fuse);
    plcc_nlm = plcc_nlm + Plcc_nlm;
    srocc_nlm = srocc_nlm + Srocc_nlm;
    rmse_nlm = rmse_nlm + Rmse_nlm;
    
    % BM3D
    path = strcat('.\data\seed_',num2str(seed_id,'%02d'),'\score_bm3d_3_30.mat');
    load(path)
    [Plcc_bm3d,Srocc_bm3d,Rmse_bm3d] = verify_performance(Mos_test',score_fuse);
    plcc_bm3d = plcc_bm3d + Plcc_bm3d;
    srocc_bm3d = srocc_bm3d + Srocc_bm3d;
    rmse_bm3d = rmse_bm3d + Rmse_bm3d;
    
end

matrix = [plcc_baseline srocc_baseline rmse_baseline
          plcc_bm3d srocc_bm3d rmse_bm3d
          plcc_nlm srocc_nlm rmse_nlm
          plcc_bilat srocc_bilat rmse_bilat];
matrix = matrix/10;      % calculate the mean vaule
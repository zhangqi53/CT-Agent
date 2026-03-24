%% Statistical significance in residual of different IQA methods
clear all
clc

%% Initialization data
addpath('tools');
load('\\storage-3\tabgha\users\gq\PR-IQA\data\mos.mat')
num = 130;
q_bm3d = zeros(num,1);
q_nlm = zeros(num,1);
q_bf = zeros(num,1);
q_baseline = zeros(num,1);
q_brisque = zeros(num,1);
q_niqe = zeros(num,1);
q_piqe = zeros(num,1);
q_mad = zeros(num,1);
q_gmsd = zeros(num,1);
q_fsim = zeros(num,1);
q_ssim = zeros(num,1);
q_psnr = zeros(num,1);

for seed_id = 1:10
    
    % Extract the label scores (Mos_test) of the test set
    path = strcat('\\storage-3\tabgha\users\gq\PR-IQA\data\CTinfo_cnet_seed_',num2str(seed_id,'%02d'),'.mat');
    load(path)
    
    path = strcat('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\seed_',num2str(seed_id,'%02d'),'\test_id_seed_',num2str(seed_id,'%02d'),'.mat');
    load(path)
    [test_num,~] = size(test_id);
    Mos_test = zeros(test_num,1);
    for i = 1:test_num
        Mos_test(i,1) = Mos(test_id(i),1);
    end
    
    Mos_test = Mos_test(1:num);
    
    %% Calculate the residual scores
    path = strcat('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\seed_',num2str(seed_id,'%02d'),'\score_10_00_00.mat');
    load(path)
    score_fuse = score_fuse(1:num);
    [~,~,~,y_pre,~] = verify_performance(Mos_test',score_fuse);
    Q_bm3d = abs(Mos_test-y_pre);
    q_bm3d = q_bm3d + Q_bm3d;
    
    path = strcat('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\seed_',num2str(seed_id,'%02d'),'\score_nlm_3_30.mat');
    load(path)
    score_fuse = score_fuse(1:num);
    [~,~,~,y_pre,~] = verify_performance(Mos_test',score_fuse);
    Q_nlm = abs(Mos_test-y_pre);
    q_nlm = q_nlm + Q_nlm;
    
    path = strcat('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\seed_',num2str(seed_id,'%02d'),'\score_bf_3_30.mat');
    load(path)
    score_fuse = score_fuse(1:num);
    [~,~,~,y_pre,~] = verify_performance(Mos_test',score_fuse);
    Q_bf = abs(Mos_test-y_pre);
    q_bf = q_bf + Q_bf;
    
    path = strcat('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\seed_',num2str(seed_id,'%02d'),'\score_single.mat');
    load(path)
    score_single = score_single(1:num);
    [~,~,~,y_pre,~] = verify_performance(Mos_test',score_single);
    Q_baseline = abs(Mos_test-y_pre);
    q_baseline = q_baseline + Q_baseline;
    
    % classic IQA method
    path = strcat('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\seed_',num2str(seed_id,'%02d'),'\compare_methods_scores.mat');
    load(path)
    BRISQUE_scores = BRISQUE_scores(1:num);
    NIQE_scores = NIQE_scores(1:num);
    PIQE_scores = PIQE_scores(1:num);
    MAD_scores = MAD_scores(1:num);
    FSIM_scores = FSIM_scores(1:num);
    SSIM_scores = SSIM_scores(1:num);
    PSNR_scores = PSNR_scores(1:num);
    GMSD_scores = GMSD_scores(1:num);
    
    [~,~,~,y_pre,~] = verify_performance(Mos_test',BRISQUE_scores);
    y_pre = y_pre(1:num);
    Q_brisque = abs(Mos_test-y_pre);
    q_brisque = q_brisque + Q_brisque;
    
    [~,~,~,y_pre,~] = verify_performance(Mos_test',NIQE_scores);
    Q_niqe = abs(Mos_test-y_pre);
    q_niqe = q_niqe + Q_niqe;
    
    [~,~,~,y_pre,~] = verify_performance(Mos_test',PIQE_scores);
    Q_piqe = abs(Mos_test-y_pre);
    q_piqe = q_piqe + Q_piqe;
    
    [~,~,~,y_pre,~] = verify_performance(Mos_test',MAD_scores);
    Q_mad = abs(Mos_test-y_pre);
    q_mad = q_mad + Q_mad;
    
    [~,~,~,y_pre,~] = verify_performance(Mos_test',GMSD_scores);
    Q_gmsd = abs(Mos_test-y_pre);
    q_gmsd = q_gmsd + Q_gmsd;
    
    [~,~,~,y_pre,~] = verify_performance(Mos_test',FSIM_scores);
    Q_fsim = abs(Mos_test-y_pre);
    q_fsim = q_fsim + Q_fsim;
    
    [~,~,~,y_pre,~] = verify_performance(Mos_test',SSIM_scores);
    Q_ssim = abs(Mos_test-y_pre);
    q_ssim = q_ssim + Q_ssim;
    
    [~,~,~,y_pre,~] = verify_performance(Mos_test',PSNR_scores);
    Q_psnr = abs(Mos_test-y_pre);
    q_psnr = q_psnr + Q_psnr;
    
end
%% F test for equal variances
q = q_bf;

[t_bm3d]= vartest2(q,q_bm3d);
[t_nlm]= vartest2(q,q_nlm);
[t_bf]= vartest2(q,q_bf);
[t_baseline]= vartest2(q,q_baseline);
[t_brisque]= vartest2(q,q_brisque);
[t_niqe]= vartest2(q,q_niqe);
[t_piqe]= vartest2(q,q_piqe);
[t_mad]= vartest2(q,q_mad);
[t_gmsd]= vartest2(q,q_gmsd);
[t_fsim]= vartest2(q,q_fsim);
[t_ssim]= vartest2(q,q_ssim);
[t_psnr]= vartest2(q,q_psnr);

[h_bm3d]= vartest2(q,q_bm3d,'tail','left');
[h_nlm]= vartest2(q,q_nlm,'tail','left');
[h_bf]= vartest2(q,q_bf,'tail','left');
[h_baseline]= vartest2(q,q_baseline,'tail','left');
[h_brisque]= vartest2(q,q_brisque,'tail','left');
[h_niqe]= vartest2(q,q_niqe,'tail','left');
[h_piqe]= vartest2(q,q_piqe,'tail','left');
[h_mad]= vartest2(q,q_mad,'tail','left');
[h_gmsd]= vartest2(q,q_gmsd,'tail','left');
[h_fsim]= vartest2(q,q_fsim,'tail','left');
[h_ssim]= vartest2(q,q_ssim,'tail','left');
[h_psnr]= vartest2(q,q_psnr,'tail','left');
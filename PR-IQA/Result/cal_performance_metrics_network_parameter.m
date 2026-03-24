%% Calculate the PLCC, SROCC and RMSE under different kernel_size, patch_size and kernel_number
clear all
clc

%% Extract the label scores (Mos_test) of the test set
addpath('tools');
load('\\storage-3\tabgha\users\gq\PR-IQA\data\CTinfo_seed_10.mat')
load('\\storage-3\tabgha\users\gq\PR-IQA\data\mos.mat')

load('.\seed_10\test_id_seed_10.mat')
[num,~] = size(test_id);
Mos_test = zeros(num,1);
for i = 1:num
    Mos_test(i,1) = Mos(test_id(i),1);
end

%% kernel_size
load('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\seed_10\score_10_00_00_bm3d_kernel3.mat')
[plcc_3,srocc_3,rmse_3] = verify_performance(Mos_test',score_fuse);

load('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\seed_10\score_10_00_00_bm3d_kernel5.mat')
[plcc_5,srocc_5,rmse_5] = verify_performance(Mos_test',score_fuse);

load('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\seed_10\score_10_00_00_bm3d_kernel9.mat')
[plcc_9,srocc_9,rmse_9] = verify_performance(Mos_test',score_fuse);

%% patch_size
load('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\seed_10\score_10_00_00_bm3d_patch16.mat')
[plcc_16,srocc_16,rmse_16] = verify_performance(Mos_test',score_fuse);

load('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\seed_10\score_10_00_00_bm3d_patch32.mat')
[plcc_32,srocc_32,rmse_32] = verify_performance(Mos_test',score_fuse);

load('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\seed_10\score_10_00_00_bm3d_patch48.mat')
[plcc_48,srocc_48,rmse_48] = verify_performance(Mos_test',score_fuse);

load('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\seed_10\score_10_00_00_bm3d_patch64.mat')
[plcc_64,srocc_64,rmse_64] = verify_performance(Mos_test',score_fuse);

%% kernel number
load('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\seed_10\score_10_00_00_bm3d_kn10.mat')
[plcc_10,srocc_10,rmse_10] = verify_performance(Mos_test',score_fuse);

load('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\seed_10\score_10_00_00_bm3d_kn20.mat')
[plcc_20,srocc_20,rmse_20] = verify_performance(Mos_test',score_fuse);

load('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\seed_10\score_10_00_00_bm3d_kn25.mat')
[plcc_25,srocc_25,rmse_25] = verify_performance(Mos_test',score_fuse);

load('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\seed_10\score_10_00_00_bm3d_kn30.mat')
[plcc_30,srocc_30,rmse_30] = verify_performance(Mos_test',score_fuse);

load('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\seed_10\score_10_00_00_bm3d_kn35.mat')
[plcc_35,srocc_35,rmse_35] = verify_performance(Mos_test',score_fuse);

load('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\seed_10\score_10_00_00_bm3d_kn40.mat')
[plcc_40,srocc_40,rmse_40] = verify_performance(Mos_test',score_fuse);

load('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\seed_10\score_10_00_00_bm3d_kn45.mat')
[plcc_45,srocc_45,rmse_45] = verify_performance(Mos_test',score_fuse);

load('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\seed_10\score_10_00_00_bm3d_kn55.mat')
[plcc_55,srocc_55,rmse_55] = verify_performance(Mos_test',score_fuse);

load('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\seed_10\score_10_00_00_bm3d_kn60.mat')
[plcc_60,srocc_60,rmse_60] = verify_performance(Mos_test',score_fuse);

load('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\seed_10\score_10_00_00_bm3d_kn70.mat')
[plcc_70,srocc_70,rmse_70] = verify_performance(Mos_test',score_fuse);

load('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\seed_10\score_10_00_00_bm3d_kn80.mat')
[plcc_80,srocc_80,rmse_80] = verify_performance(Mos_test',score_fuse);

%% Generate performance matrix
patch_size = [plcc_16 srocc_16 rmse_16
              plcc_32 srocc_32 rmse_32
              plcc_48 srocc_48 rmse_48
              plcc_64 srocc_64 rmse_64];

kernel_size = [plcc_3  srocc_3  rmse_3
               plcc_5  srocc_5  rmse_5
               plcc_32 srocc_32 rmse_32
               plcc_9  srocc_9  rmse_9];

kernel_number = [plcc_10 srocc_10 rmse_10
                 plcc_20 srocc_20 rmse_20
                 plcc_25 srocc_25 rmse_25
                 plcc_30 srocc_30 rmse_30
                 plcc_35 srocc_35 rmse_35
                 plcc_40 srocc_40 rmse_40
                 plcc_45 srocc_45 rmse_45
                 plcc_32 srocc_32 rmse_32
                 plcc_55 srocc_55 rmse_55
                 plcc_60 srocc_60 rmse_60
                 plcc_70 srocc_70 rmse_70
                 plcc_80 srocc_80 rmse_80];
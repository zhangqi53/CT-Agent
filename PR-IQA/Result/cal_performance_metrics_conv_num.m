%% Calculate the PLCC, SROCC and RMSE under different conv layer number
clear all
clc

addpath('.\tools');

%% load network parameter configuration
para_set = [[3,30,0,0,0,0,800,800];...                                                         % Conv layer -- 1. The front -- Conv kernel size. The back -- Conv kernel number
    [5,20,3,40,0,0,800,800]; [5,30,3,60,0,0,800,800]; [5,40,3,80,0,0,800,800];...              % Conv layer -- 2.
    [7,20,3,40,0,0, 800,800]; [7,30,3,60,0, 0, 800,800]; [7,40,3,80,0, 0, 800,800];...         % Conv layer -- 2. 
    [7,20,5,40,0,0, 800,800]; [7,30,5,60,0, 0, 800,800]; [7,40,5,80,0, 0, 800,800];...         % Conv layer -- 2.
    [7,20,5,40,3,80,800,800]; [7,30,5,60,3,120,800,800]; [7,40,5,80,3,160,800,800]];           % Conv layer -- 3.

[m,~] = size(para_set);
matrix = zeros(m,3);

%% Calculate the PLCC, SROCC and RMSE between the network prediction scores and MOS
for seed_id = 10     % Only conduct comparative experiments when seed_id=10
    
    % Extract the label scores (Mos_test) of the test set
    path = strcat('\\storage-3\tabgha\users\gq\PR-IQA\data\CTinfo_seed_',num2str(seed_id,'%02d'),'.mat');
    load(path)
    load('\\storage-3\tabgha\users\gq\PR-IQA\data\Mos.mat')
    
    path = strcat('.\data\seed_',num2str(seed_id,'%02d'),'\test_id_seed_',num2str(seed_id,'%02d'),'.mat');
    load(path)
    [num,~] = size(test_id);
    Mos_test = zeros(1,num);
    for i = 1:num
        Mos_test(1,i) = Mos(test_id(i),1);
    end
    
    for para_id = 1:m
        para = para_set(para_id,:);
        
        % Conv layer -- 1
        if para_id == 1
            path = strcat('.\data\seed_',num2str(seed_id,'%02d'),'\score_bm3d_',num2str(para(1)),'_',num2str(para(2)),'.mat');
            load(path);
            [plcc,srocc,rmse] = verify_performance(Mos_test',score_fuse);
        end
        
        % Conv layer -- 2
        if para_id >= 2 && para_id <= 10
            path = strcat('.\data\seed_',num2str(seed_id,'%02d'),'\score_bm3d_',num2str(para(1)),'_',num2str(para(2)),'_',num2str(para(3)),'_',num2str(para(4)),'.mat');
            load(path);
            [plcc,srocc,rmse] = verify_performance(Mos_test',score_fuse);  
        end
        
        % Conv layer -- 3
        if para_id >= 11
            path = strcat('.\data\seed_',num2str(seed_id,'%02d'),'\score_bm3d_',num2str(para(1)),'_',num2str(para(2)),'_',num2str(para(3)),'_',num2str(para(4)),'_',num2str(para(5)),'_',num2str(para(6)),'.mat');
            load(path);
            [plcc,srocc,rmse] = verify_performance(Mos_test',score_fuse);
        end
        matrix(para_id,1:3) = matrix(para_id,1:3)+[plcc,srocc,rmse];
    end
end
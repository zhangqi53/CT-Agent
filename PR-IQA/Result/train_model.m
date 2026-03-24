%% Train BRISQUE and NIQE models (must run on matlab 2018 or higher version)
clear all
clc

for seed_id = 1:10
    
    %% load the same training data as the PR-IQA model
    path = strcat('\\storage-3\tabgha\users\gq\PR-IQA\Result_analysis\data\seed_',num2str(seed_id,'%02d'),'\train_id_seed_',num2str(seed_id,'%02d'),'.mat');
    load(path);
    load('\\storage-3\tabgha\users\gq\PR-IQA\data\Mos.mat')
    [m,~] = size(train_id);
    Mos_train = zeros(m,1);
    for i = 1:m
        Mos_train(i,1) = Mos(train_id(i),1);
    end
    
    %% model train (usage: https://ww2.mathworks.cn/help/images/train-and-use-a-no-reference-quality-assessment-model.html)
    % brisque
    setDir = strcat('\\storage-3\tabgha\users\gq\PR-IQA\Result_analysis\data\seed_',num2str(seed_id,'%02d'),'\low_mat_train_seed_',num2str(seed_id,'%02d'),'\');
    imds = imageDatastore(setDir,'FileExtensions',{'.mat'});
    opinionScores = Mos_train;
    model = fitbrisque(imds,opinionScores');
    path = strcat('\\storage-3\tabgha\users\gq\PR-IQA\Result_analysis\data\seed_',num2str(seed_id,'%02d'),'\brisque_model_667.mat');
    save(path,'model','-v7.3')
    
    % niqe
    setDir = strcat('\\storage-3\tabgha\users\gq\PR-IQA\Result_analysis\data\seed_',num2str(seed_id,'%02d'),'\ref_mat_train_seed_',num2str(seed_id,'%02d'),'\');
    imds = imageDatastore(setDir,'FileExtensions',{'.mat'});
    model = fitniqe(imds,'BlockSize',[96 96]);
    path = strcat('\\storage-3\tabgha\users\gq\PR-IQA\Result_analysis\data\seed_',num2str(seed_id,'%02d'),'\niqe_model.mat');
    save(path,'model','-v7.3')
    
end
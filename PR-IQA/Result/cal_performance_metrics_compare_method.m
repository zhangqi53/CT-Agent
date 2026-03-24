%% Calculate the PLCC, SROCC and RMSE of comparative IQA methods
clear all
clc

addpath('tools');
addpath(genpath('iqa_packages'));
load('\\storage-3\tabgha\users\gq\PR-IQA\data\Mos.mat')

for seed_id = 1:10
    %% Extract the label scores (Mos_test) of the test set
    path = strcat('\\storage-3\tabgha\users\gq\PR-IQA\data\CTinfo_seed_',num2str(seed_id,'%02d'),'.mat');
    load(path)
    path = strcat('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\seed_',num2str(seed_id,'%02d'),'\test_id_seed_',num2str(seed_id,'%02d'),'.mat');
    load(path)
    [num,~] = size(test_id);
    Mos_test = zeros(num,1);
    for i = 1:num
        Mos_test(i,1) = Mos(test_id(i),1);
    end
    
    %% Initialization data
    PSNR_scores = zeros(num,1);
    SSIM_scores = zeros(num,1);
    FSIM_scores = zeros(num,1);
    MAD_scores = zeros(num,1);
    GMSD_scores = zeros(num,1);
    PIQE_scores = zeros(num,1);
    BRISQUE_scores = zeros(num,1);
    NIQE_scores = zeros(num,1);
    
    %% load brisque and niqe model
    path = strcat('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\seed_',num2str(seed_id,'%02d'),'\brisque_model_3.mat');
    load(path);
    brisque_model = model;
    path = strcat('\\storage-3\tabgha\users\gq\PR-IQA\Result\data\seed_',num2str(seed_id,'%02d'),'\niqe_model.mat');
    load(path);
    niqe_model = model;
    
    %% Calculate predicted scores of comparative IQA methods
    for i = 1:num
        disp(i)
        filename1 = strcat('imglow_',num2str(test_id(i),'%04d'),'.mat');
        pathname1 = '\\storage-3\tabgha\users\gq\PR-IQA\ct_mat\low_mat\';
        lowname = [pathname1, filename1];
        filename2 = strcat('imgref_',num2str(ref_ids(test_id(i)),'%04d'),'.mat');
        pathname2 = '\\storage-3\tabgha\users\gq\PR-IQA\ct_mat\ref_mat\';
        refname = [pathname2, filename2];
        ref = load(refname);
        in = load(lowname);
        in = double(in.img);
        ref = double(ref.img);
        L = max(ref(:));
        
        % NIQE
        NIQE = niqe(in,niqe_model);
        NIQE_scores(i,:) = NIQE;
        
        % BRISQUE
        BRISQUE = brisque(in,brisque_model);
        BRISQUE_scores(i,:) = BRISQUE;
        
        % PIQE
        PIQE = piqe(in);
        PIQE_scores(i,:) = PIQE;
        
        % PSNR and SSIM
        psnr_one  =  psnr(in, ref, L);
        ssim_one  =  ssim(in, ref, 'DynamicRange', L);
        PSNR_scores(i,:) = psnr_one;
        SSIM_scores(i,:) = ssim_one;
        
        % GMSD
        GMSD_one = GMSD(ref,in);
        GMSD_scores(i,:) = GMSD_one;
        
        % FSIM
        FSIM = FeatureSIM(ref,in);
        FSIM_scores(i,:) = FSIM;
        
        % MAD
        MAD_one = MAD_index(ref,in);
        MAD_scores(i,:) = MAD_one.MAD;
    end
    
    %% Calculate the PLCC, SROCC and RMSE
    [plcc_MAD,srocc_MAD,rmse_MAD,pre_MAD] = verify_performance(Mos_test',MAD_scores);
    [plcc_FSIM,srocc_FSIM,rmse_FSIM,pre_FSIM] = verify_performance(Mos_test',FSIM_scores);
    [plcc_GMSD,srocc_GMSD,rmse_GMSD,pre_GMSD] = verify_performance(Mos_test',GMSD_scores);
    [plcc_PSNR,srocc_PSNR,rmse_PSNR,pre_PSNR] = verify_performance(Mos_test',PSNR_scores);
    [plcc_SSIM,srocc_SSIM,rmse_SSIM,pre_SSIM] = verify_performance(Mos_test',SSIM_scores);
    [plcc_PIQE,srocc_PIQE,rmse_PIQE,pre_PIQE] = verify_performance(Mos_test',PIQE_scores);
    [plcc_BRISQUE,srocc_BRISQUE,rmse_BRISQUE,pre_BRISQUE] = verify_performance(Mos_test',BRISQUE_scores);
    [plcc_NIQE,srocc_NIQE,rmse_NIQE,pre_NIQE] = verify_performance(Mos_test',NIQE_scores);
    
    %% save data
    path = strcat('.\data\seed_',num2str(seed_id,'%02d'),'\compare_methods_performance_metrics.mat');
    save(path,'plcc_MAD','srocc_MAD','rmse_MAD','pre_MAD','plcc_FSIM','srocc_FSIM','rmse_FSIM','pre_FSIM','plcc_GMSD','srocc_GMSD','rmse_GMSD','pre_GMSD','plcc_PSNR','srocc_PSNR','rmse_PSNR','pre_PSNR',...
        'plcc_SSIM','srocc_SSIM','rmse_SSIM','pre_SSIM','plcc_PIQE','srocc_PIQE','rmse_PIQE','pre_PIQE','plcc_BRISQUE','srocc_BRISQUE','rmse_BRISQUE','pre_BRISQUE','plcc_NIQE','srocc_NIQE','rmse_NIQE','pre_NIQE','-v7.3')
    path = strcat('.\data\seed_',num2str(seed_id,'%02d'),'\compare_methods_scores.mat');
    save(path,'MAD_scores','FSIM_scores','GMSD_scores','PSNR_scores','SSIM_scores','PIQE_scores','BRISQUE_scores','NIQE_scores','-v7.3')
end
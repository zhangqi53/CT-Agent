clear all
clc

addpath('function');

%% The number of full-dose reference images taken by each case. (The front is the number of chest images, The back is the number of abdominal images)
img_num = [5 0;8 20;8 10;7 15;6 0;18 5;8 10;5 0;5 10];
patient_num = 9; % Number of selected cases

%% Calculate the total number of reference images and distorted images
ref_num = 0;
low_num = 0;
for i = 1:patient_num
    ref_num = ref_num+img_num(i,1)+img_num(i,2);
    low_num = low_num+img_num(i,1)*4+img_num(i,2)*6; % 4 different doses' images are simulated on the chest 
                                                     % 6 different doses' images are simulated on the abdomen
end

%% Save file names of reference images and distorted images
im_names = cell(low_num,1);
for i = 1:low_num
    im_names{i} = strcat('low_mat/imglow_',num2str(i,'%04d'),'.mat');
end

ref_names = cell(ref_num,1);
for i = 1:ref_num
    ref_names{i} = strcat('ref_mat/imgref_',num2str(i,'%04d'),'.mat');
end

%% Calculate the id of the reference image corresponding to each distorted image
ref_ids = zeros(low_num,1);
num = 0;
idx = 0;
for i = 1:patient_num
    chest_num = img_num(i,1);
    abdomen_num = img_num(i,2);
    for dose = 1:6
        id = idx;
        for k = 1:abdomen_num
            num = num + 1;
            id = id + 1;
            ref_ids(num,1) = id;
        end
    end
    idx = id;
    for dose = 1:4
        id = idx;
        for k = 1:chest_num
            num = num + 1;
            id = id + 1;
            ref_ids(num,1) = id;
        end
    end
    idx = id;
end

%% Calculate label scores
load('\\storage-3\tabgha\users\gq\CNNIQA-master\data\Mos.mat');
subjective_scores = Mos(1:low_num);
load('\\storage-3\tabgha\users\gq\CNNIQA-master\data\ssim_niqe_scores.mat');
ssim_scores = scale_self(ssim_scores,100,1);
niqe_scores = scale_self(niqe_scores,100,1);
ssim_scores = ssim_scores(1:low_num);
niqe_scores = niqe_scores(1:low_num);

for i = 1:10
    index = zeros(1,ref_num);
    rand('seed',i);    %% seed_id, for scramble data
    r = randperm(ref_num);
    index(1,:) = r;      %随机数指标
    path = strcat('\\storage-3\tabgha\users\gq\CNNIQA-master\data\CTinfo_seed_',num2str(i,'%02d'),'.mat');
    save(path, 'im_names','index','ref_ids','ref_names','subjective_scores','ssim_scores','niqe_scores','-v7.3');
end
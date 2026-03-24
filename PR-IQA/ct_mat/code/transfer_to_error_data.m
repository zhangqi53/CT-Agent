clear all
clc

path_save = '\\storage-3\tabgha\users\gq\CNNIQA-master\ct_mat\nlm_deta20_error_mat\';
mkdir(path_save);
for i = 1:700
    path = strcat('\\storage-3\tabgha\users\gq\CNNIQA-master\ct_mat\low_mat\imglow_',num2str(i,'%04d'),'.mat');
    load(path);
    low_img = img;
    path = strcat('\\storage-3\tabgha\users\gq\CNNIQA-master\ct_mat\nlm_deta20_mat\imglow_',num2str(i,'%04d'),'.mat');
    load(path);
    denoise_img = img;
    img = low_img-denoise_img;
    name_save = strcat('imglow_',num2str(i,'%04d'),'.mat');
    save([path_save name_save],'img','-v7.3')
end

% load('\\storage-3\tabgha\users\gq\CNNIQA-master\data\CTinfo_seed_10.mat');
% for i = 1:700
%     path = strcat('\\storage-3\tabgha\users\gq\CNNIQA-master\ct_mat\low_mat\imglow_',num2str(i,'%04d'),'.mat');
%     load(path);
%     low_img = img;
%     id = ref_ids(i);
%     path = strcat('\\storage-3\tabgha\users\gq\CNNIQA-master\ct_mat\ref_mat\imgref_',num2str(id,'%04d'),'.mat');
%     load(path);
%     ref_img = img;
%     img = low_img-ref_img;
%     path = strcat('\\storage-3\tabgha\users\gq\CNNIQA-master\ct_mat\error_mat\imglow_',num2str(i,'%04d'),'.mat');
%     save(path,'img','-v7.3')
% end
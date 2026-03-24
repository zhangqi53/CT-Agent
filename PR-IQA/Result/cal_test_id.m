%% Calculate the id of training data and test data under different seed_id
clear all
clc

for seed_id = 1:10
    path = strcat('\\storage-3\tabgha\users\gq\PR-IQA\data\CTinfo_seed_',num2str(seed_id,'%02d'),'.mat');
    load(path)
    
    % test_id
    [~,n] = size(index);
    test_index = index(1,0.8*n+1:n);
    test_id = zeros(1,1);
    test_num = 0;
    for i = 1:700
        for j = 1:0.2*n
            if ref_ids(i,1) == test_index(1,j)
                test_num = test_num+1;
                test_id(test_num,1) = i;
            end
        end
    end
    
    % train_id
    train_index = index(1,1:0.6*n);
    train_id = zeros(1,1);
    train_num = 0;
    for i = 1:700
        for j = 1:0.6*n
            if ref_ids(i,1) == train_index(1,j)
                train_num = train_num+1;
                train_id(train_num,1) = i;
            end
        end
    end
    
    path_train_id = strcat('.\data\seed_',num2str(seed_id,'%02d'),'\train_id_seed_',num2str(seed_id,'%02d'),'.mat');
    path_test_id = strcat('.\data\seed_',num2str(seed_id,'%02d'),'\test_id_seed_',num2str(seed_id,'%02d'),'.mat');
    save(path_train_id,'train_id','-v7.3');
    save(path_test_id,'test_id','-v7.3');
end
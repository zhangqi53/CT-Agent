%% 将挑选的mat数据转成神经网络训练数据格式，保存为IQA_data
clear all
clc

fileFolder=fullfile('\\storage-3\Tabgha\users\gq\Mayo_IQA_data\real_IQA_data');  
dirOutput=dir(fullfile(fileFolder,'*'));
[s1,~] = size(dirOutput);
id = 0;
info = strings(140,6);
im_ref = zeros(512,512,140);
for i = 3:11
    C = dirOutput(i,:);
    ans1 = C.name;
    dirOutput1 = dir(fullfile(fileFolder,ans1,'*'));
    [s2,~] = size(dirOutput1);
    
    for j = 3:s2
        D = dirOutput1(j,:);
        ans2 = D.name;
        dirOutput2 = dir(fullfile(fileFolder,ans1,ans2,'*'));
        [s3,~] = size(dirOutput2);
        
        for k = 3
            E = dirOutput2(k,:);
            ans3 = E.name;
            dirOutput3 = dir(fullfile(fileFolder,ans1,ans2,ans3,'*'));
            [s4,~] = size(dirOutput3);
            
            for l = s4
                F = dirOutput3(l,:);
                ans4 = F.name;
                filepath = F.folder;
                file_path = [filepath,'\',ans4];
                disp(file_path);
                img_ref = load(file_path);
                img_ref = img_ref.Img;
                [~,~,s] = size(img_ref);
                dose = strsplit(string(ans4),'_');
                for m = 1:s
                    flag = 1;
                    img = img_ref(:,:,m);
                    if size(ans2,2) == 5
                        if ans2 == 'chest'
                            flag = 0;
                            img = 255 * double(img-0.002) / (0.032-0.002);
                        end
                    end
                    if size(ans2,2) == 7
                        if  ans2 == 'abdomen'
                            flag = 0;
                            img = 255 * double(img-0.013) / (0.027-0.013);
                        end
                    end
                
                    id = id+1;
                    mat_name = strcat('imgref_',num2str(id,'%04d'),'.mat');
                    mat_path = '\\storage-3\tabgha\users\gq\CNNIQA_CN\ct_mat\ref_mat\';
                    save([mat_path mat_name],'img','-v7.3');
                    
                    info(id,1) = string(ans1);
                    info(id,2) = string(ans2);
                    info(id,3) = string(ans3);
                    info(id,4) = dose(2);
                    info(id,5) = string(ans4);
                    info(id,6) = m;
                end
            end       
        end  
    end
    if flag == 1
        disp('error');
        break;
    end
end
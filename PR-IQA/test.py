from argparse import ArgumentParser
import os
import pickle
import numpy as np
import random
from scipy import stats
import torch
from torch.utils.data import DataLoader
from torch import nn
import torch.nn.functional as F
from torch.optim import Adam
import datetime
from load_data import IQA,NonOverlappingCropPatches
import torchvision.transforms as transforms
from tkinter import _flatten
import h5py
from PIL import Image
import scipy.io as sio
from ipdb import set_trace

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

# define CNNIQA network architecture
class CNNIQAnet(nn.Module):
    def __init__(self, ker_size, n_kers, n1_nodes, n2_nodes):
        super(CNNIQAnet, self).__init__()
        self.conv1  = nn.Conv2d(1, n_kers, ker_size)
        self.fc1    = nn.Linear(2 * n_kers, n1_nodes)
        self.fc2    = nn.Linear(n1_nodes, n2_nodes)
        self.fc3    = nn.Linear(n2_nodes, 1)

    def forward(self, x):
        x  = x.view(-1, x.size(-3), x.size(-2), x.size(-1))  #

        h  = self.conv1(x)

        # h1 = F.adaptive_max_pool2d(h, 1)
        # h2 = -F.adaptive_max_pool2d(-h, 1)
        h1 = F.max_pool2d(h, (h.size(-2), h.size(-1)))
        h2 = -F.max_pool2d(-h, (h.size(-2), h.size(-1)))
        h  = torch.cat((h1, h2), 1)  # max-min pooling
        h  = h.squeeze(3).squeeze(2)

        h  = F.relu(self.fc1(h))
        h  = F.dropout(h)
        h  = F.relu(self.fc2(h))

        q  = self.fc3(h)
        return q
    

if __name__ == "__main__":
    
    for seed_id in range(10,11):
        print(seed_id)
        
        ker_size = 3
        n_kers = 30
        
        # Read the optimal Epoch and corresponding network model
        #max_plcc = 0
        #with open('./model_save/seed_' + '%02d' %seed_id +'/model_bm3d_' + '%d' %ker_size + '_' + '%d' %n_kers + '/train_information.txt','rb') as file_pi:
        #    loss_train = pickle.load(file_pi)
        #    plcc_val = pickle.load(file_pi)
        #for epoch in range (0,100):
        #    if plcc_val[epoch] > max_plcc:
        #        max_plcc = plcc_val[epoch]
        #        Epoch = epoch + 1
        #print(Epoch)
        Epoch = 97
        device = torch.device("cuda")
        model_fr = CNNIQAnet(ker_size = ker_size,
                        n_kers = n_kers,
                        n1_nodes=800,
                        n2_nodes=800)
        model_fr.load_state_dict(torch.load('./model_save/seed_' + '%02d' %seed_id +'/model_bm3d_' + '%d' %ker_size + '_' + '%d' %n_kers + '/fr/CNN_FR_epoch' + '%d' %Epoch +'.pkl'))
        model_fr = model_fr.cuda()
        
        model_nr = CNNIQAnet(ker_size = ker_size,
                        n_kers = n_kers,
                        n1_nodes=800,
                        n2_nodes=800)
        model_nr.load_state_dict(torch.load('./model_save/seed_' + '%02d' %seed_id +'/model_bm3d_' + '%d' %ker_size + '_' + '%d' %n_kers + '/nr/CNN_NR_epoch' + '%d' %Epoch +'.pkl'))
        model_nr = model_nr.cuda()

        y_predict = []
        y_fr = []
        y_nr = []
        
        # Read test data
        root='./ct_mat/'
        Info = h5py.File('./data/CTinfo_seed_' + '%02d' %seed_id +'.mat', mode = 'r')
        Mos = Info['subjective_scores']
        index = Info['index'][:, 0]
        ref_ids = Info['ref_ids'][0, :]
        train_ratio = 0.6
        test_ratio = 0.2
        trainindex = index[:int(train_ratio * len(index))]
        testindex = index[int((1-test_ratio) * len(index)):]
        train_index, val_index, test_index = [],[],[]
        for i in range(len(ref_ids)):
            train_index.append(i+1) if (ref_ids[i] in trainindex) else \
                test_index.append(i+1) if (ref_ids[i] in testindex) else \
                    val_index.append(i+1)
        final_index = test_index

        # Run the network to output test results
        with torch.no_grad():
            model_fr.eval()
            model_nr.eval()
            for i in range(len(final_index)):
                ids = final_index[i]
                
                imagePath_fr = 'bm3d_error_mat/imglow_' + '%04d' %ids + '.mat'
                Im_fr = h5py.File(os.path.join(root, imagePath_fr), mode = 'r')
                im_fr = Im_fr['img'][:]
                patches_fr = NonOverlappingCropPatches(im_fr, 16, 16)
                patch_scores_fr = model_fr(torch.stack(patches_fr).to(device))
        
                imagePath_nr = 'bm3d_mat/imglow_' + '%04d' %ids + '.mat'
                Im_nr = h5py.File(os.path.join(root, imagePath_nr), mode = 'r')
                im_nr = Im_nr['img'][:]
                patches_nr = NonOverlappingCropPatches(im_nr, 16, 16)
                patch_scores_nr = model_nr(torch.stack(patches_nr).to(device))
                predict_scores = (patch_scores_fr.mean().item()) * (patch_scores_nr.mean().item()) / 100
                y_fr = np.append(y_fr, patch_scores_fr.mean().item())  
                y_nr = np.append(y_nr, patch_scores_nr.mean().item())  
                y_predict = np.append(y_predict, predict_scores)     
        
        # save test results
        path = './Result/data/seed_' + '%02d' %seed_id +'/score_bm3d_' + '%d' %ker_size + '_' + '%d' %n_kers + '.mat'
        os.makedirs(os.path.dirname(path), exist_ok=True)
        sio.savemat(path, {'score_fr':y_fr,'score_nr':y_nr,'score_fuse':y_predict})
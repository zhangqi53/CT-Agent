from PIL import Image
import os
import os.path
import errno
import numpy as np
import sys
import pickle

import torch.utils.data as data
from torchvision.datasets.utils import download_url, check_integrity

import torch
import torch.nn.functional as F
from torch.autograd import Variable as V
from torchvision.transforms.functional import to_tensor
from scipy.signal import convolve2d
import torchvision.transforms as transforms
import scipy.io as sio
import h5py

from ipdb import set_trace

## Local Normalization for the input image patch
def LocalNormalization(patch, P=3, Q=3, C=1): # P,Q: Local normalized region size; C: constant
    kernel = np.ones((P, Q)) / (P * Q)
    patch_mean = convolve2d(patch, kernel, boundary='symm', mode='same')
    patch_sm = convolve2d(np.square(patch), kernel, boundary='symm', mode='same')
    patch_std = np.sqrt(np.maximum(patch_sm - np.square(patch_mean), 0)) + C
    patch_ln = torch.from_numpy((patch - patch_mean) / patch_std).float().unsqueeze(0)
    return patch_ln

## Extract image patch
def NonOverlappingCropPatches(im, patch_size=32, stride=32):
    w = im.shape[0]
    h = im.shape[1]
    patches = []
    for i in range(0, h - stride, stride):
        for j in range(0, w - stride, stride):
            patch = to_tensor(im[j:j+patch_size, i:i + patch_size])
            patch = LocalNormalization(patch[0].numpy())
            patches.append(patch)
    return patches

class IQA(data.Dataset):
    def __init__(self, root='', train=True):
        self.root = root
        self.train = train
        self.patch_size = 16
        self.stride = 16
        Info = h5py.File('./data/CTinfo_seed_10.mat', mode = 'r')    # Read data information and label scores
        Mos = Info['subjective_scores']                                   # Mos is the label score
        Frs = Info['ssim_scores']                                       # Objective scores, try to use it restrict the network output, but the performance is not good
        Nrs = Info['niqe_scores']
        index = Info['index'][:, 0]
        ref_ids = Info['ref_ids'][0, :]
        train_ratio = 0.6
        trainindex = index[:int(train_ratio * len(index))]
        train_index = []
        for i in range(len(ref_ids)):
            if ref_ids[i] in trainindex:
                train_index.append(i+1)
        print("# Train Images: {}".format(len(train_index)))
        print('Ref Index:')
        print(trainindex)
        if  self.train:                                                   # Read train data and label scores
            self.train_fr_data = []
            self.train_nr_data = []
            self.train_fr_labels = []
            self.train_nr_labels = []
            self.train_labels = []
            for i in range(len(train_index)):
                ids = train_index[i]
                label_fr = Frs[0][ids-1] # 标签读取
                label = Mos[0][ids-1]
                imagePath_fr = 'bm3d_error_mat/imglow_' + '%04d' %ids + '.mat'         # Read residual image (use BM3D as denoise method)
                # imagePath_fr = 'nlm_error_mat/imglow_' + '%04d' %ids + '.mat'        # Read residual image (use NLM as denoise method)
                # imagePath_fr = 'bf_error_mat/imglow_' + '%04d' %ids + '.mat'         # Read residual image (use BF as denoise method)
                Im_fr = h5py.File(os.path.join(root, imagePath_fr), mode = 'r')
                im_fr = Im_fr['img'][:]
                patches = NonOverlappingCropPatches(im_fr, self.patch_size, self.stride)
                patches = np.concatenate(patches)
                patches_num = len(patches)
                patches = patches.reshape((patches_num, 1, self.patch_size, self.patch_size))
                self.train_fr_data.append(patches)
                for i in range(patches_num):
                    self.train_fr_labels.append(float(label_fr))                       # FR_labels. It is not used in this experiment 
                    self.train_labels.append(float(label))                             # MOS labels                                 
            self.num_train = len(self.train_fr_labels)
            self.train_fr_data = np.concatenate(self.train_fr_data)
            self.train_fr_data = self.train_fr_data.reshape((self.num_train, 1, self.patch_size, self.patch_size))
            self.train_fr_data = self.train_fr_data.transpose((0, 2, 3, 1))
            
            for i in range(len(train_index)):
                ids = train_index[i]
                label_nr = Nrs[0][ids-1] # 标签读取
                imagePath_nr = 'bm3d_mat/imglow_' + '%04d' %ids + '.mat'               # Read Pre-restored image (use BM3D as denoise method) 
                #imagePath_nr = 'nlm_mat/imglow_' + '%04d' %ids + '.mat'               # Read Pre-restored image (use NLM as denoise method) 
                #imagePath_nr = 'bf_mat/imglow_' + '%04d' %ids + '.mat'                # Read Pre-restored image (use BF as denoise method) 
                Im_nr = h5py.File(os.path.join(root, imagePath_nr), mode = 'r')
                im_nr = Im_nr['img'][:]
                patches = NonOverlappingCropPatches(im_nr, self.patch_size, self.stride)
                patches = np.concatenate(patches)
                patches_num = len(patches)
                patches = patches.reshape((patches_num, 1, self.patch_size, self.patch_size))
                self.train_nr_data.append(patches)
                for i in range(patches_num):
                    self.train_nr_labels.append(float(label_nr))                        # NR_labels. It is not used in this experiment 
            self.num_train = len(self.train_nr_labels)
            self.train_nr_data = np.concatenate(self.train_nr_data)
            self.train_nr_data = self.train_nr_data.reshape((self.num_train, 1, self.patch_size, self.patch_size))
            self.train_nr_data = self.train_nr_data.transpose((0, 2, 3, 1))

    def __getitem__(self, index):
        if self.train:
            img_fr, img_nr, target, target_fr, target_nr = self.train_fr_data[index], self.train_nr_data[index], \
                self.train_labels[index], self.train_fr_labels[index], self.train_nr_labels[index]
            img_fr = torch.from_numpy(img_fr)
            img_fr = img_fr.reshape(1,16,16)
            
            img_nr = torch.from_numpy(img_nr)
            img_nr = img_nr.reshape(1,16,16)
            
        return img_fr, img_nr, target, target_fr, target_nr

    def __len__(self):
        if self.train:
            return self.num_train
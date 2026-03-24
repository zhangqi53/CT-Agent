from argparse import ArgumentParser
import os
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
import pickle
os.environ["CUDA_VISIBLE_DEVICES"] = '0'

# read train, val and test data
def build_dataset():
    train_transform = transforms.Compose([transforms.ToTensor(),])
    train_data = IQA(root='/home/liuyiwei/PR-IQA/ct_mat/', train=True)      
    train_loader = torch.utils.data.DataLoader(train_data, batch_size=args.batch_size, shuffle=True, num_workers=args.prefetch, pin_memory=True)
    
    return train_loader

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

# loss function
def loss_fn(y_pred, y):
    return F.l1_loss(y_pred, y)

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

# define test function   
def test(epochs, data_folder):
    
    y_true = []
    y_predict = []
    y_fr = []
    y_nr = []
    
    # Read test data
    root='./ct_mat/'
    Info = h5py.File('./data/CTinfo_seed_10.mat', mode = 'r')       # Read data information and label scores
    Mos = Info['subjective_scores']
    Frs = Info['ssim_scores']
    Nrs = Info['niqe_scores']
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
                
    if data_folder == 'train':
        final_index = train_index
    if data_folder == 'val':
        final_index = val_index
    if data_folder == 'test':
        final_index = test_index
    with torch.no_grad():
        model_fr.eval()
        model_nr.eval()
        for i in range(len(final_index)):
            ids = final_index[i]
            label = Mos[0][ids-1] # 标签读取
            
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
            y_true = np.append(y_true, label)
            predict_scores = (patch_scores_fr.mean().item()) * (patch_scores_nr.mean().item()) / 100
            y_predict = np.append(y_predict, predict_scores)
        
        # Calculate SROCC, KROCC, PLCC, RMSE, MAE
        sq = y_true
        q = y_predict
        srocc = stats.spearmanr(sq, q)[0]
        krocc = stats.stats.kendalltau(sq, q)[0]
        plcc = stats.pearsonr(sq, q)[0]
        rmse = np.sqrt(((sq - q) ** 2).mean())
        mae = np.abs((sq - q)).mean()
        print('Epoch: [%d/%d]\t'
            'SROCC: %.4f\t'
            'KROCC: %.4f\t'
            'PLCC: %.4f\t'
            'RMSE: %.4f\t'
            'MAE: %.4f\t' % ((epoch + 1), args.epochs, srocc, krocc, plcc, rmse, mae))
        return plcc

# define train function 
def train(epochs, lr, weight_decay):
    train_loss = 0
    for batch_idx, (inputs_fr, inputs_nr, targets, targets_fr, targets_nr) in enumerate(train_loader):
        
        model_fr.train()
        model_nr.train()
        
        inputs_fr = inputs_fr.float()
        inputs_nr = inputs_nr.float()
        targets = targets.float()
        targets_fr = targets_fr.float()
        targets_nr = targets_nr.float()
        inputs_fr, inputs_nr, targets, targets_fr, targets_nr = inputs_fr.to(device), inputs_nr.to(device),targets.to(device), targets_fr.to(device), targets_nr.to(device)
        targets = torch.reshape(targets, (len(targets), 1))
        targets_fr = torch.reshape(targets_fr, (len(targets_fr), 1))
        targets_nr = torch.reshape(targets_nr, (len(targets_nr), 1))
        
        outputs_fr = model_fr(inputs_fr)
        outputs_nr = model_nr(inputs_nr)
        outputs = (outputs_fr * outputs_nr) / 100     # score fusion
        
        Loss_human = loss_fn(outputs, targets)
        Loss_fr = loss_fn(outputs_fr, targets_fr)
        Loss_nr = loss_fn(outputs_nr, targets_nr)
        loss = Loss_human# + 0.2 * Loss_fr + 0.2 * Loss_nr
        loss_fr = Loss_human# + 0.2 * Loss_fr + 0.2 * Loss_nr
        loss_nr = Loss_human# + 0.2 * Loss_fr + 0.2 * Loss_nr
        
        # Update the network parameters of the FR part
        # 同时清零两个优化器的梯度
        optimizer_fr.zero_grad()
        optimizer_nr.zero_grad()

        # 只做一次反向传播
        loss.backward()

        # 同时更新两个模型参数
        optimizer_fr.step()
        optimizer_nr.step()
        
        train_loss += loss.item()

        # Create a folder and save the model (using BM3D as the denoising algorithm)
        ensure_dir('model_save/seed_' + '%02d' %seed_id + '/model_bm3d_' + '%d' %ker_size + '_' + '%d' %n_kers + '/fr')
        ensure_dir('model_save/seed_' + '%02d' %seed_id + '/model_bm3d_' + '%d' %ker_size + '_' + '%d' %n_kers + '/nr')
        torch.save(model_fr.state_dict(), 'model_save/seed_' + '%02d' %seed_id + '/model_bm3d_' + '%d' %ker_size + '_' + '%d' %n_kers + '/fr/CNN_FR_epoch%d.pkl' % (epoch+1))
        torch.save(model_nr.state_dict(), 'model_save/seed_' + '%02d' %seed_id + '/model_bm3d_' + '%d' %ker_size + '_' + '%d' %n_kers + '/nr/CNN_NR_epoch%d.pkl' % (epoch+1))
    print('Epoch: [%d/%d]\t''Loss: %.4f\t'  % ((epoch + 1), args.epochs, train_loss/(batch_idx+1)))
    return (train_loss/(batch_idx+1))


if __name__ == "__main__":
    
    # Optimal network model parameters
    ker_size = 3
    n_kers = 30
    
    parser = ArgumentParser(description='PyTorch CNNIQA')
    parser.add_argument("--seed", type=int, default=19920517)
    parser.add_argument('--batch_size', type=int, default=1024,
                        help='input batch size for training (default: 128)')
    parser.add_argument('--epochs', type=int, default=100,
                        help='number of epochs to train (default: 500)')
    parser.add_argument('--lr', type=float, default=0.001,
                        help='learning rate (default: 0.001)')
    parser.add_argument('--weight_decay', type=float, default=0.0,
                        help='weight decay (default: 0.0)')
    parser.add_argument("--log_dir", type=str, default="logger",
                        help="log directory for Tensorboard log output")
    parser.add_argument('--disable_gpu', action='store_true',
                        help='flag whether to disable GPU')
    parser.add_argument('--prefetch', type=int, default=0, help='Pre-fetching threads.')
    parser.add_argument('--seed_id', type=int, default=0, help='seed_id') # seed_id is the random seed number for the training set, validation set and test set divided

    args = parser.parse_args()
    seed_id = args.seed_id
    args.disable_gpu = False
    device = torch.device("cuda" if not args.disable_gpu and torch.cuda.is_available() else "cpu")
    
    torch.manual_seed(args.seed)  #
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    np.random.seed(args.seed)
    random.seed(args.seed)

    torch.utils.backcompat.broadcast_warning.enabled = True
    
    # Initialize the network model of the FR and NR part
    model_fr = CNNIQAnet(ker_size,
                      n_kers,
                      n1_nodes=800,
                      n2_nodes=800)
    model_fr = model_fr.cuda()
    optimizer_fr = Adam(model_fr.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    
    model_nr = CNNIQAnet(ker_size,
                      n_kers,
                      n1_nodes=800,
                      n2_nodes=800)
    model_nr = model_nr.cuda()
    optimizer_nr = Adam(model_nr.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    
    train_loader = build_dataset()
        
    max_plcc_val = -2
    max_plcc_test = -2
    loss = []
    PLCC_train = []
    PLCC_val = []
    PLCC_test = []
    # strat train
    for epoch in range(args.epochs):
        train_loss = train(args.epochs, args.lr, args.weight_decay)
        loss.append(train_loss)
        plcc_train = test(args.epochs, data_folder = 'train')   # Calculate the PLCC on the training set
        PLCC_train.append(plcc_train)
        
        plcc_val = test(args.epochs, data_folder = 'val')       # Calculate the PLCC on the validation set
        PLCC_val.append(plcc_val)
        # Calculate the optimal PLCC_val and save the corresponding Epoch
        if plcc_val > max_plcc_val:
            max_plcc_val = plcc_val
            max_epoch_val = epoch+1
            
        plcc_test = test(args.epochs, data_folder = 'test')     # Calculate the PLCC on the test set
        PLCC_test.append(plcc_test)
        # Calculate the optimal PLCC_test and save the corresponding Epoch
        if plcc_test > max_plcc_test:
            max_plcc_test = plcc_test
            max_epoch_test = epoch+1

    # Save the loss, plcc and other parameters of the training process           
    with open('model_save/seed_10/model_bm3d_5_30_3_60/train_information.txt', 'wb') as file_pi:
        pickle.dump(loss, file_pi)    # 保存训练损失
        pickle.dump(PLCC_train,file_pi)
        pickle.dump(PLCC_val,file_pi)
        pickle.dump(PLCC_test,file_pi)
    #  Display the optimal parameters 
    print('Best_Epoch_val: [%d]\t' 'Best_PLCC_val: %.4f\t' % (max_epoch_val, max_plcc_val))
    print('Best_Epoch_test: [%d]\t' 'Best_PLCC_test: %.4f\t' % (max_epoch_test, max_plcc_test))
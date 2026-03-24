%% Generate mean opinion scores(MOS)
clear all
clc

addpath('function')

%% Read the radiologist's score
h1 = xlsread('.\human_scores\h1.xlsx');
m1 = xlsread('.\human_scores\m1.xlsx');
w1 = xlsread('.\human_scores\w1.xlsx');

%% Calculate the average score of 5 terms
h1 = (h1(:,1)+h1(:,2)+h1(:,3)+h1(:,4)+h1(:,5))/5;
m1 = (m1(:,1)+m1(:,2)+m1(:,3)+m1(:,4)+m1(:,5))/5;
w1 = (w1(:,1)+w1(:,2)+w1(:,3)+w1(:,4)+w1(:,5))/5;

%% Normalized scores to 0-1
h1 = Normalize_scores(h1);
m1 = Normalize_scores(m1);
w1 = Normalize_scores(w1);

%% Calculate MOS and scale to 0-100
Mos = (h1+m1+w1)/3;
Mos = scale_self(Mos,100,0);
save('Mos.mat', 'Mos','-v7.3')
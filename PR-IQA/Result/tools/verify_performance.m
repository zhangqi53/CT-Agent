%this script is used to calculate the pearson linear correlation
%coefficient and root mean sqaured error after regression

%get the objective scores computed by the IQA metric and the subjective
%scores provided by the dataset

function [plcc,srocc,rmse,ypre,y] = verify_performance(mos,predict_mos)

predict_mos = predict_mos(:);
mos = mos(:);

%initialize the parameters used by the nonlinear fitting function
beta(1) = 10;
beta(2) = 0;
beta(3) = mean(predict_mos);
beta(4) = 0.1;
beta(5) = 0.1;
 
% options = optimoptions('lsqcurvefit','Display','none');  
% lb = [];
% ub = [];
% bayta =  lsqcurvefit(@logistic,beta,predict_mos,mos,lb,ub, options);
% fun = @logistic;
% ypre = fun(bayta,predict_mos);
% x = 0:0.01:100;
% y = fun(bayta,x);

% %fitting a curve using the data
warning off
[bayta ehat,J] = nlinfit(predict_mos,mos,@logistic,beta);
% %given a ssim value, predict the correspoing mos (ypre) using the fitted curve
[ypre junk] = nlpredci(@logistic,predict_mos,bayta,ehat,J);
% 
x = 0:0.01:100;
y = nlpredci(@logistic,x,bayta,ehat,J);
warning on

rmse = sqrt(sum((ypre - mos).^2) / length(mos));%root meas squared error
plcc = corr(mos, ypre, 'type','Pearson'); %pearson linear coefficient
srocc = corr(mos, ypre, 'type','spearman');
%krocc = corr(mos, predict_mos, 'type','Kendall');
end
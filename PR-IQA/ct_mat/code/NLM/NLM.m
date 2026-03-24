%% ×Ô¼ºÐ´µÄ

function denoise_im = NLM(im)
denoise_im = im;
[m,n] = size(im);
patch = 3;
block = 21;
deta = 6;%4;
h = 0.4*deta;

%for i = 1+patch+block:m-patch-block
    %for j =1+patch+block:n-patch-block
        zz = 0;
        ff = 0;
        for c = i-patch:i+patch
            for d = j-patch:j+patch
                dd = (i-c)^2+(j-d)^2;
                w = exp((-(dd - 2*deta*deta))/(h*h));
                zz = zz + w;
                ff = ff + w * denoise_im(c,d);
            end
        end
        f = (1/zz) * ff;
        denoise_im(i,j) = f;
    end
end
end
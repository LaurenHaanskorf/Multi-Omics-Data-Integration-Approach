tic
    A = readmatrix('.../MDICC-main/MDICC-main/data1/data1/fusion_affin.csv');
    dynType=1; 
    maxIters=1000;
    x=ones(size(A,1),1)./size(A,11); 
    theta=10^-5; 
    
    result = zeros(465,175);
    p = 1;
    
    % evaluation of precision values
    for k = 0.01:0.0001:0.05
     precision=k;   
     [C]=dominantset(A,x,theta,precision,maxIters,dynType); 
     result(:,p) = C;
     p = p+1;
    end
toc    

% resulting clusterings for all precision values transformed into a matrix
% that can be used as input into 
writematrix(result,'.../MDICC-main/MDICC-main/data1/data1/clust.csv')

% Dominant Set Clustering with a specific precision value
%   precision = ...;
%   [C] = dominantset(A,x,theta,precision,maxIters,dynType); 
%   writematrix(C,'.../MDICC-main/MDICC-main/data1/data1/clust2.csv')



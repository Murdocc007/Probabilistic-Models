function [theta] = LR(D)
% D is the data having feature variables and class labels

% Now decompose D into X and C 
%Note that dimensions of X =  , C = 

C = D(:,1);
C = C';
size(C)
X = D(:,2:size(D,2));
size(X)
alpha = .00001;

theta_new = .001.*ones(1,size(D,2)-1);
count = 1;
for count = 1:100000
    theta_new = theta_new + alpha*(C-sigmoid(X*theta_new')')*X;
end
theta = theta_new
end


function a = LLR( z )
a= 1.*log(1.0 + exp(-z));
end

function a = sigmoid(z)
 a = 1.0 ./ (1.0 + exp(-z));
 end



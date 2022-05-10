clear; clear path; clc;
%% Notes and in-prog code
addpath('./funcs/')

n = 4; % user count 
v = [0.1 0.5 0.4 0.2]';
t = 1;
T = 50;

zi = zeros(n,T); 

A = ones(n,n); % user connectivity
x = zeros(n,T); %initial states of users
x(:,1) = [0 0 0 0]';



T = 50;
q = 0.6;
c = 0.1;

% Solve min_{x in X} [sum{i=1-->n} f_{i}(x) ]
%                                  f_{i}(x) = ||x_i-v_i||^2

% where i is a user and f is cost function
% x is state in 

for t=1:T % not T-1 because not zero-indexing
    gamma = c*q^(t-1); % t-1 for index correction
    zi(:,t) = (A*x(:,t)); % matrix prod solves sum.

    %x(t+1) = zi(:,t)-gamma*fgrad(zi(:,t)); % projection?


end

clear; clear path; clc;
%% Notes and in-prog code
addpath('./funcs/')

n = 4; % user count 
v = [0.1 0.5 0.4 0.2]';

% Solve min_{x in X} [sum{i=1-->n} f_{i}(x) ]
%                                  f_{i}(x) = ||x_i-v_i||^2

% where i is a user and f is cost function
% x is state in 



clear; clear path; clc;
%% Notes and in-prog code
addpath('./funcs/')

n = 4; % user count 
v = [0.1 0.5 0.4 0.2]';
T = 50;

zi = zeros(n,T);
gamma = zeros(1,T);

% A = ones(n,n)/4; % user connectivity !row&col sum =1!
%A = [1/2 1/8 1/8 1/4; 1/8 1/8 1/4 1/2; 1/8 1/4 1/2 1/8; 1/4 1/2 1/8 1/8]; % unequal connectivity
A = magic(4); % random connectivity
A = A/sum(A(1,:)); 

x = zeros(n,T); %initial states of users
x(:,1) = [.6 .4 .9 0]';

T = 50;
q = 0.6;
c = 0.1;

% Solve min_{x in X} [sum{i=1-->n} f_{i}(x) ]
%                                  f_{i}(x) = ||x_i-v_i||^2

% where i is a user and f is cost function
% x is state in 

for t=1:T-1
    gamma(t) = c*q^(t-1); % t-1 for index correction
    zi(:,t) = (A*x(:,t)); % matrix prod solves sum.

    x(:,t+1) = zi(:,t)-gamma(t)*fgrad(x(:,t),v);
    for i=1:4
        x(i,t+1) = min(1,x(i,t+1));
        x(i,t+1) = max(-1,x(i,t+1));
    end
end

figure(1)
plot(0:T-1,x,'-o')
legend("x1","x2","x3","x4")
axis([0 6 0 1])

mean(v)
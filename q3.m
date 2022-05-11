clear; clear path; clc; clf;
%% Notes and in-prog code
addpath('./funcs/')

n = 8; % user count 
v = [0.1 0.5 0.4 0.2 0.1 0.5 0.4 0.2]';
T = 50;

zi = zeros(n,T);
gamma = zeros(1,T);

% A = ones(n,n)/4; % user connectivity !row&col sum =1!
%A = [1/2 1/8 1/8 1/4; 1/8 1/8 1/4 1/2; 1/8 1/4 1/2 1/8; 1/4 1/2 1/8 1/8]; % unequal connectivity
A = magic(n); % random connectivity
A = A/sum(A(1,:)); 

x = zeros(n,T); %initial states of users
x(:,1) = [0.6 .4 .9 0 0.4 0.7 0.1 0.5]';

T = 50;
q = 0.6;
c = 1;

for t=1:T-1
    gamma(t) = c*q^(t-1); % t-1 for index correction
    zi(:,t) = (A*x(:,t)); % matrix prod solves sum.

    x(:,t+1) = zi(:,t)-gamma(t)*fgrad(x(:,t),v);
    x(:,t+1) = projX(x(:,t+1),1,-1);
end

figure(1)
plot(0:T-1,x,'-o')
legend('x1','x2','x3','x4', 'x5','x6','x7','x8')
axis([0 20 0 1])
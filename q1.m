clear; clear path; clc; clf;
%% Notes and in-prog code
addpath('./funcs/')

n = 4; % user count 
v = [0.1 0.5 0.4 0.2]';
T = 50;

zi = zeros(n,T);
gamma = zeros(1,T);

% A = ones(n,n)/4; % user connectivity !row&col sum =1!
%A = [1/2 1/8 1/8 1/4; 1/8 1/8 1/4 1/2; 1/8 1/4 1/2 1/8; 1/4 1/2 1/8 1/8]; % unequal connectivity
A = magic(n); A = A/sum(A(1,:)); 

x = zeros(n,T); %initial states of users
x(:,1) = [0.6 .4 .9 0]';

T = 50;
q = 0.6;
c = 0.1;

for t=1:T-1
    gamma(t) = c*q^(t-1); % t-1 for index correction
    zi(:,t) = (A*x(:,t)); % matrix prod solves sum.

    x(:,t+1) = zi(:,t)-gamma(t)*fgrad(x(:,t),v);
    x(:,t+1) = projX(x(:,t+1),1,-1);
end

%% plot
figure(1); hold on;
plot(0:T-1,x,'-o')

axis([0 10 0 1])
title("values of x per iteration")
xlabel("Iterations")
ylabel("values of x")

vh = 0.3*ones(1,length(x));
plot(0:T-1,vh,"r--")
legend('x1','x2','x3','x4','$v_{avg}$','interpreter','latex')
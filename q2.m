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
eps = 1E-3;
C2 = 2.2;

% Solve min_{x in X} [sum{i=1-->n} f_{i}(x) ]
%                                  f_{i}(x) = ||x_i-v_i||^2

% where i is a user and f is cost function
% x is state in 

for t=1:T-1
    gamma(t) = c*q^(t-1); % t-1 for index correction 
    p = .95; % FIXME: slection of p not understood
    
    lambda = 2*C2*sqrt(n)*c*p^(t)/(eps*(p-q));
    zi(:,t) = (A*(x(:,t)+diag(randlap(4,lambda)))); % matrix prod solves sum.


    x(:,t+1) = zi(:,t)-gamma(t)*fgrad(x(:,t),v);
    x(:,t+1) = projX(x(:,t+1),1,-1);
end

abs(round(x(:,end),3)-.3)

%% plot
figure(1); hold on;
% subplot(1,2,1); hold on;
title("Values of x_i over iterations")
plot(0:T-1,x,'-o')

xlabel("iterations")
ylabel("values of x_i")

vh = 0.3*ones(1,length(x));
plot(0:T-1,vh,"r--")
legend('x_1','x_2','x_3','x_4','$v_{avg}$','interpreter','latex')
axis([0 50 0 1])

% subplot(1,2,2); hold on;
% title("Values of x_i over iterations")
% plot(0:T-1,x,'-o')
% 
% xlabel("iterations")
% ylabel("values of x_i")
% 
% plot(0:T-1,vh,"r--")
% legend('x_1','x_2','x_3','x_4','$v_{avg}$','interpreter','latex')
% axis([0 10 0 1])

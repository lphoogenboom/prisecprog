clear; clear path; clc; clf;
%% Notes and in-prog code
addpath('./funcs')

n = 8; % user count 
v = [0.1 0.5 0.4 0.2 0.1 0.5 0.4 0.2]';
T = 50;

zi = zeros(n,T);
gamma = zeros(1,T);

% A = ones(n,n)/n; % user connectivity !row&col sum =1!
%A = [1/2 1/8 1/8 1/4; 1/8 1/8 1/4 1/2; 1/8 1/4 1/2 1/8; 1/4 1/2 1/8 1/8]; % unequal connectivity
A = magic(n); A = A/sum(A(1,:)); 

x = zeros(n,T); %initial states of users
x(:,1) = [0.6 .4 .9 0 -0.3 -0.5 -0.2 -0.1]';

T = 50;
q = 0.6;
c = 1;
eps = 1E-3;
C2 = 2.2;
% Solve min_{x in X} [sum{i=1-->n} f_{i}(x) ]
%                                  f_{i}(x) = ||x_i-v_i||^2

% where i is a user and f is cost function
% x is state in 


for t=1:T-1
    gamma(t) = c*q^(t-1); % t-1 for index correction
   
    lambda = 2*sqrt(n)*C2*c*q^(t-1)/eps;   % parameter b_t [other formula then in the paper]
    p = 0.90;
    lambda = 2*C2*sqrt(n)*c*p^(t)/(eps*(p-q));

    
    zi(:,t) = (A*(x(:,t)+diag(randlap(n,lambda)))); % matrix prod solves sum.

    % mechanism
%     in: x, t
%         addative noise
%     out: y

    x(:,t+1) = zi(:,t)-gamma(t)*fgrad(x(:,t),v);
    x(:,t+1) = projX(x(:,t+1),1,-1);
end

abs(round(x(:,end),3)-.3)

figure(2)
plot(0:T-1,x,'-o')
lgd.Layout.Tile = 'southeast';
legend('x1','x2','x3','x4','x5','x6','x7','x8','Location','northeastoutside')

%axis([0 6 0 1])
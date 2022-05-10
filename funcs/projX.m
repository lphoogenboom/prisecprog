function [x] = projX(x,max,min)
%PROJX Summary of this function goes here
%   Detailed explanation goes here
    for i=1:4
        x(i,t+1) = min(max,x(i,t+1));
        x(i,t+1) = max(min,x(i,t+1));
    end
end


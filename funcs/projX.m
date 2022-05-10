function [x] = projX(x,uBound,lBound)
%PROJX Summary of this function goes here
%   Detailed explanation goes here
    for i=1:4
        x = min(uBound,x);
        x = max(lBound,x);
    end
end


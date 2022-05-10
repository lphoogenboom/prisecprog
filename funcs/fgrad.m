function gradient = fgrad(x,v)
    % Cost function of user
    diff = x-v;
    gradient = 2*sum(diff);
end


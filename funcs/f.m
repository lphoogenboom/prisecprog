function cost = f(x,v)
    % Cost function of user
    diff = x-v;
    fi = diff.^2;
    cost = sum(fi);
end


-- Babylonian Method

x = 24

if x<=1:
    x
else:
    x_n = 0.5 * x
    change = 1
    
    while change >0.1:
        next_n = 0.5 * (x_n + x/x_n)
        change = abs(x_n - next_n)
        x_n = next_n
    print (int(x_n))

-- 
return int(x**(1/2))

--

import math
math.sqrt(x)

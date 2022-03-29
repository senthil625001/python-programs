# Elegant solution
if n == 0:
    print (1)
elif x == 0:
    print(0)

return x**n

# T= 0(1) , S= 0(1)

x = 2
n = 10

if n == 0:
    print (1)
elif x == 0:
    print(0)
    
flag = False # to identify negative & positive

if n < 0:
    flag = True
    n = -n

res = 1

while n > 0:    
    if n % 2 == 1:
        res *= x
        n -= 1

    else:
        x = x * x
        n /= 2
        
if flag:
    print(1 / res)
else:
    print(res)

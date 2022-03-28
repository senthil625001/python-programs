###### EXAMPLE ###############
### arr = [23,2,4,6,6], k= 7 ######
# idx     n       prefix_sum  dict key=(prefix_sum%k), value=current_element_idx
#                                 {0:-1}   # Initialization
# 0      23          23           {0:-1, 2:0}
# 1      2           25           {0:-1, 2:0, 4:1}
# 2      4           29           {0:-1, 2:0, 4:1, 1:2}
# 3      6           35           35%7 == 0, 0 was present in dict and idx - dict[0] > 1 ret True 
# 4      6 


nums = [23,2,4,6,6]
k = 7

remainder = {0:-1}

total = 0

for i, v in enumerate (nums):
    if k!=0:
        total = (total + v)%k
    else:
        total+=n
    
    if total not in remainder:
        remainder[total] = i
    elif i - remainder[total] >1:
        print(True)
print(False)


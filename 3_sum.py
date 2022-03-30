nums = [-1,0,1,2,-1]

res = []
nums.sort() # sort the numbers 
print ("nums is", nums) # [-1, -1, 0, 1, 2]

for item, value in enumerate(nums):
    if item > 0 and value == nums[item-1]:
        continue
        
    l, r = item+1, len(nums)-1
    
    while l<r:
        threeSum = value + nums[l] + nums[r]
        
        print ("threeSum", threeSum)
        print ("l is", l)
        print ("r is", r)
        print ("Value is", value)
        print ("Left is", nums[l])
        print("Right is", nums[r])
        
        
        if threeSum > 0:
            r-=1
        elif threeSum <0:
            l+=1
        else:
            res.append([value, nums[l], nums[r]])
        
            print (res)
            
            l+=1
            
            while nums[l] == nums [l-1] and l <r:
                l+=1
print (res)
        

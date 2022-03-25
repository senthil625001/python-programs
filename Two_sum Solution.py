# Using Hashmap
def two_sum(nums,target):
  
  hashmap = {}
  
  for item, value in enumerate (nums):
    result = target - value
    if result in hashmap:
      return [i, hashmap(result)]
    hashmap[value] = result
    
  return

a = [1,2,3,4,5,6] 
target = 8

print (two_sum(a,target))
  
  

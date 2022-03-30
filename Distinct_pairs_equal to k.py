arr = [8, 10, 16, 4, 0, 20]
n = len(arr)
k = 4
count =0
 
# Sort array elements
arr.sort()

stack = []
l = 0
r = 1

while r<n:
    if arr[r]-arr[l]==k:
        stack.append([arr[r], arr[l]])
        count+=1
        l+=1
        r+=1
         
    
    elif arr[r]-arr[l]>k:
        l+=1
    else:
        r+=1
print (count)
print (stack)

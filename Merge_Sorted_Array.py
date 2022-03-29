nums1 = [2,3,5,6,0,0,0]
nums2 = [1,4,5]

last = len(nums1)-1
m = len(nums1) - len(nums)
n = len(nums2)

print (last)
print(m)
print(n)

while m > 0 and n>0:
    if nums1[m-1] > nums2[n-1]:
        nums1[last] = nums1[m-1]
        m-=1
    else:
        nums1[last] = nums2[n-1]
        n-=1
    
    last-=1
    
while n >0:
    nums1[last] = nums2[n-1]
    n, last = n-1, last-1

print (nums1)
print (nums2)

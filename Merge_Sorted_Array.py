nums1 = [2,3,5,6,0,0,0]
nums2 = [1,4,5]

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = len(nums1) - len(nums2) #7-3 = 4
        p2 = len(nums2) - 1 # 3-1=2
    
        # And move p backwards through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(p1+p2, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1

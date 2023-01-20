import collections
class Solution(object):
    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        c = collections.Counter(nums1)
        ans = []
        for x in nums2:
            if c[x] > 0:
                ans += x,
                c[x] -= 1
        print ('The intersection of two sets:', x)
        
adding = Solution()
nums1 = list(map(int,input('list1: ').split()))
nums2 = list(map(int,input('list2: ').split()))
x= adding.intersect(nums1, nums2)

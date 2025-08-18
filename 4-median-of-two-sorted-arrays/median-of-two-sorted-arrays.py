class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        x = sorted(nums1)
        y = sorted(nums2)
        merge = sorted(nums1 + nums2)
        n = len(merge)
        if n % 2 == 0:
            p = merge[n//2-1]
            q = merge[n//2]
            r = (p+q)/2.0
            return r
        else:
            return merge[n//2]

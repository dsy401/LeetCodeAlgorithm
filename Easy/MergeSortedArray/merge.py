class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums2[j] > nums1[i]:
                    nums1.insert(i+1,nums2[j])
                    nums2[j] =0
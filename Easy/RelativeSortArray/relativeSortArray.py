class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        return sorted((x for x in arr1 if x in arr2), key=arr2.index) + sorted([x for x in arr1 if x not in arr2])
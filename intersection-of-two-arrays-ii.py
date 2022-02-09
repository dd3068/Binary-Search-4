'''
TC: O(nlogm)
SC: O(1)
'''
class Solution:
    
    def bs(self, low, high, arr, target):
        final = -1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == target:
                final = mid
                high = mid - 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return final
    
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        
        n = len(nums1)
        m = len(nums2)
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        res = list()
        
        low, high = 0, len(nums2) - 1
        
        for n in nums1:
            idx = self.bs(low, high, nums2, n)
            if idx != -1:
                res.append(n)
                low = idx + 1
        
        return res
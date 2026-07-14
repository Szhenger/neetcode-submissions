class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Get the size of the merged array 
        size = len(nums1) + len(nums2)
        half = size // 2
        # Order the input arrays
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        # Binary search on the smaller input
        l, r = 0, len(nums1) - 1
        while True:
            m = (l + r) // 2 # nums1
            n = half - m - 2 # nums2

            left1 = nums1[m] if m >= 0 else float('-inf') # nums1
            right1 = nums1[m + 1] if m + 1 < len(nums1) else float('inf') # nums1
            left2 = nums2[n] if n >= 0 else float('-inf') # nums2
            right2 = nums2[n + 1] if n + 1 < len(nums2) else float('inf') # nums2

            # partition is correct
            if left1 <= right2 and left2 <= right1:
                # odd
                if size % 2:
                    return min(right1, right2)
                # even
                return (max(left1, left2) + min(right1, right2)) / 2
            # partition is too large
            elif left1 > right2:
                r = m - 1
            # partition is too small
            else:
                l = m + 1

        
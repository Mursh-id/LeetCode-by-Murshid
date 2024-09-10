from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, p = m - 1, n - 1, m + n - 1  # Pointers for nums1, nums2, and the end of merged nums1

        while p2 >= 0:  # Continue until all elements of nums2 are merged
            if p1 >= 0 and nums1[p1] > nums2[p2]:  # Compare elements from nums1 and nums2
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # nums1 is modified in-place
        print(nums1)

        
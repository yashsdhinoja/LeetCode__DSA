from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        last = nums[-1]  # Our "ruler" value for comparison

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > last:
                # "No": mid is on the big staircase
                # the minimum is to the right of mid
                left = mid + 1
            else: 
                # "Yes": mid is on the small staircase
                # the minimum is mid itself or to its left
                right = mid       
                
        return nums[left]
        # left and right met at the minimum

# Test cases passed as lists
print(Solution().findMin([3, 4, 5, 1, 2]))      # Output: 1
print(Solution().findMin([4, 5, 6, 7, 0, 1, 2])) # Output: 0
print(Solution().findMin([11, 13, 15, 17]))    # Output: 11